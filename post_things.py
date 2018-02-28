import json
import urllib2
import random
import time




while True:
	req = urllib2.Request(' http://demo.thingsboard.io:80/api/v1/aRHWzNoXF1fuCA097lvV/telemetry')
	req.add_header('Content-Type', 'application/json')
	data = {
    "Timestamp": time.ctime(),
    "Voltage": random.randint(1,24),
    "Current": random.randint(1,20),
    "Resistance": random.randint(1,100),
    "Battery": random.randint(1,24),
    "Starter": random.randint(1,100),
    "Alternator": random.randint(1,100),
    "Fuel /Oil  level/ Pressure": random.randint(1,100),
    "Braking pedal position": random.randint(1,100),
    "Accelerator pedal position and kick down": random.randint(1,100),
    "Brake pad condition and brake pedal temperature": random.randint(1,100),
    "Door interlock": random.randint(1,100),
    "Kneeling interlock (wherever provided)": random.randint(1,100),
    "Gas leakage detection (wherever provided)": random.randint(1,100),
    "Fire detection/suppression (wherever provided)": random.randint(1,100),
    "Engine CAN status": random.randint(1,100),
    "Engine oil pressure,": random.randint(1,100),
    "Engine coolant temperature,": random.randint(1,100),
    "Engine speed in RPM,": random.randint(1,10000),
    "Vehicle speed": random.randint(1,200),
    "Diagnostic message": random.randint(1,100),
    "Transmission CAN status": random.randint(1,100),
    "Transmission output shaft speed": random.randint(1,100),
    "Transmission input shaft speed": random.randint(1,100),
    "Transmission current gear": random.randint(1,100),
    "Transmission oil filter restriction switch": random.randint(1,100),
    "Transmission oil life remaining": random.randint(1,100),
    "Transmission service indicator": random.randint(1,100),
    "Transmission sump oil temperature": random.randint(1,100),
    "Transmission oil level high / low": random.randint(1,100),
    "Hydraulic retarderoil temperature": random.randint(1,100),
    "Accelerator pedal": random.randint(1,100),
    "Drivers demand of engine torque percentage": random.randint(1,100),
    "Actual engine torque percentage": random.randint(1,100),
    "Engine and retarder torque": random.randint(1,100),
    "Engine speed": random.randint(1,100),
    "Source address controlling device": random.randint(1,100),
    "Engine starter mode": random.randint(1,100),
    "Engine demand torque percentage": random.randint(1,100),
    "Accelerator pedal 2 low Idle switch": random.randint(1,100),
    "Road speed limit status": random.randint(1,100),
    "Accelerator pedal kickdown switch": random.randint(1,100),
    "Accelerator pedal low Idle Switch": random.randint(1,100),
    "Accelerator pedal position": random.randint(1,100),
    "Percent load at current speed": random.randint(1,100),
    "Remote accelerator pedal position": random.randint(1,100),
    "Accelerator pedal position 2": random.randint(1,100),
    "Vehicle acceleration rate limit status": random.randint(1,100),
    "Engine temperature": random.randint(1,100),
    "Engine coolant temperature": random.randint(1,100),
    "Fuel temperature": random.randint(1,100),
    "Engine oil temperature": random.randint(1,100),
    "Turbo oil temperature": random.randint(1,100),
    "Engine intercooler temperature": random.randint(1,100),
    "Engine intercooler thermostat opening": random.randint(1,100),
    "Engine fluid level pressure": random.randint(1,100),
    "Fuel delivery pressure": random.randint(1,100),
    "Extended crankcase blow by pressure": random.randint(1,100),
    "Engine oil level": random.randint(1,100),
    "Engine oil pressure": random.randint(1,100),
    "Crankcase pressure": random.randint(1,100),
    "Coolant pressure": random.randint(1,100),
    "Coolant level": random.randint(1,100),
    "Latitude": 0,
    "Longitude": 0
  }
	response = urllib2.urlopen(req, json.dumps(data))
	print response.getcode()
	time.sleep(10)
