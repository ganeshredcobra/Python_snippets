import httplib, urllib
import serial

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
while True:
    data=ser.readline()
    params = urllib.urlencode({'rdata' : '%s\n'%data})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("c11.space-kerala.org:80")
    conn.request("POST", "/data.php",params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
