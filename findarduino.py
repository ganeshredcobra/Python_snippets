import commands

raw=commands.getoutput("dmesg | grep 'GSM modem (1-port) converter now attached to'")
port=raw.splitlines()[0][-7:]
print port
raw=commands.getoutput("dmesg | grep 'FTDI USB Serial Device converter now attached to'")
ardu=raw[-7:]
print ardu
