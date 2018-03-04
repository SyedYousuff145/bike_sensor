import math

dir = '/Users/syesmohammed.yousuff/Work/bike_sensor/plots/sensor_raw_values/'
input_file = 'Bullet_raw'
output_file = 'Bullet_resultant_accel'

f_input = open(dir+input_file, 'r')
f_output = open(dir+output_file, 'w')

lines = f_input.readlines()

for line in lines[1:]:
  data = line.split(',')
  if len(data) != 7:
    continue

  resultant = pow(int(data[1]), 2) + pow(int(data[2]), 2) + pow(int(data[3]), 2)
  resultant = math.sqrt(resultant)

  f_output.write(data[0] + "," + str(resultant) + "\n")

f_input.close()
f_output.close()
