from read_serial import ReadSerial
import time, sys, signal
from constants import *

prog_logs_dir = LOG_DIR
prog_log_file_name = prog_logs_dir + time.asctime().replace(' ', '_')
prog_log_file = open(prog_log_file_name, 'w')

stop_reading = False

def signal_handler(signal, frame):
  global stop_reading
  stop_reading= True
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def discover():
  xbee_port = None
  while xbee_port == None:
    xbee_port = ReadSerial.get_xbee_adapter_port()
    # print "Xbee not connected. Trying ..."
    prog_log_file.write("Xbee not connected. Trying ...")
  # print "Xbee discovered at %s" % xbee_port
  prog_log_file.write("Xbee discovered at %s" % xbee_port)
  try:
    xbee = ReadSerial(xbee_port, 57600)
  except:
    prog_log_file.write("Exception occured. Cannot open Serial Port")
    return None
  return xbee

def log_data(xbee):
  filename = DATA_DIR + time.asctime().replace(' ', '_')
  log_file_p = open(filename+'_P', 'w')
  log_file_p.write('Time,Piezo')
  log_file_m = open(filename+'_M', 'w')
  log_file_m.write('Time,Ax,Ay,Az,Gx,Gy,Gz\n')
  log_file_g = open(filename+'_G', 'w')

  while True and not stop_reading:
    try:
      line = xbee.read_line()
      if line == None:
        continue
      data = line.split(',')
      l =  len(data)
      ts = str(time.time())+','
      if l == 2:
        log_file_p.write(ts+line[2:])
      elif l == 7:
        log_file_m.write(ts+line[2:])
      else:
        log_file_g.write(ts+line[2:])

    except:
      # print "Xbee adapter disconnected"
      prog_log_file.write("Xbee adapter disconnected")
      log_file_p.close()
      log_file_g.close()
      log_file_g.close()
      return

if __name__ == '__main__':
  while True and not stop_reading:
    xbee = None
    while xbee == None:
      xbee = discover()
    log_data(xbee)






