import glob
import struct
import sys
import threading
from queue import Queue
from time import sleep
import numpy as np
import serial
import time


def _list_serial_ports():
    # list of available serial port
    if sys.platform.startswith("win"):
        ports = ["COM" + str(i + 1) for i in range(256)]

    elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob("/dev/tty[A-Za-z]*")

    elif sys.platform.startswith("darwin"):
        ports = glob.glob("/dev/tty.*")

    else:
        raise EnvironmentError("Unsupported platform")

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


a = _list_serial_ports()[-1]
print(a)


def return_byte_array():
    return serial.Serial(port=a).readline()


# implementing moving average here
arr_new = [[[0 for x in range(8)] for y in range(8)] for z in range(8)]
arr_avg = [[0 for x in range(8)] for y in range(8)]

def movingAverage(arg1_list, arg2_pos):

    for i in range(8):
        for j in range(8):
            arr_avg[i][j] = arr_avg[i][j] - arr_new[arg2_pos][i][j] + arg1_list[i][j]

    arr_new[arg2_pos] = arg1_list

    return arr_avg


count = 0
file = open("Data.txt", 'w')
start = time.time()

window = 8
pos_avg = 0
while(1):
    serial_data_in_bytes = return_byte_array()
    arr = []

    new_var = (serial_data_in_bytes[4] << 8 | serial_data_in_bytes[3])*0.0625
    arr = [(serial_data_in_bytes[i] << 8 | serial_data_in_bytes[i-1])* 0.25 for i in range(6, 134, 2)]
    data = [[0 for x in range(8)]for y in range(8)]
    k = 0
    for i in range(8):
        for j in range(8):
            data[i][j] = arr[k]
            k = k+1
    '''for i in range(8):
        for j in range(8):
            print(data[i][j], "\t", end=" ")
        print('\n')'''

    m_avg = movingAverage(data, pos_avg)
    pos_avg = (pos_avg+1)%window #8
    print(m_avg)
    
    
    file.write(str(data))
    file.write('\n')

    count += 1
    if (count == 20):
        break
# m_avg = movingAverage(data)[1
for i in range(8):
    for j in range(8):
        m_avg[i][j] = round(m_avg[i][j]/window, 2)
        print(m_avg[i][j], "\t", end=" ")
    print("\n")

