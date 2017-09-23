import serial
import serial.tools.list_ports
from constants import XBEE_BRIDGE_DESCRIPTION

class ReadSerial():
  """This class provides methods to open
  a serial port and read/write data to it
  """

  def __init__(self, port, baudrate = 57600, timeout=2):
    """Initialization
    Args:
      serial_port - Serial port to open
      baud_rate - Baud rate to use
      timeout - Time to wait for data before aborting
    """
    self.port = port
    self.baudrate = baudrate
    self.timeout = timeout
    self.serial_port_handle = serial.Serial(port=self.port,
                                            baudrate=self.baudrate,
                                            timeout=self.timeout)
    self.serial_port_handle.reset_input_buffer()
    self.serial_port_handle.reset_output_buffer()

  def read_line(self):
    """Read a single line
     Returns:
       (str) Single line of data
       If no incoming data, return None
    """
    if self.serial_port_handle.in_waiting:
      return self.serial_port_handle.readline()
    else:
      return None

  def data_available(self):
    """Returns the bytes of data in the input buffer
    """
    return self.serial_port_handle.in_waiting

  def flush_buffers(self):
    self.serial_port_handle.reset_input_buffer()
    self.serial_port_handle.reset_output_buffer()

  def send_command(self, command):
    self.serial_port_handle.write(command)

  def close(self):
    self.serial_port_handle.close()

  @classmethod
  def get_xbee_adapter_port(cls):
    """Return the port where XBEE adapter is attached
    It searches for port with description of the device.
    """
    open_ports = serial.tools.list_ports.comports()
    for port in open_ports:
      if port.usb_description() == XBEE_BRIDGE_DESCRIPTION:
        return port.device
    print "No COM port device found that matches the description % s" % (XBEE_BRIDGE_DESCRIPTION)
    print "Following devices were found"
    for port in open_ports:
      print port.usb_description()
    return None





