import imaplib
import email
import serial,sys,smtplib
condn=""
i=0
while i!=1:	
	def reply():
		SMTP_SERVER = 'smtp.gmail.com'
		SMTP_PORT = 587
		 
		sender = 'librelabz@gmail.com'
		recipient = '%s'%From
		subject = '%s'%message
		body = ':) Python + Arduino'
		password = 'friendlyarm'
		 
		"Sends an e-mail to the specified recipient."
		 
		body = "" + body + ""
		 
		headers = ["From: " + sender,
				   "Subject: " + subject,
				   "To: " + recipient,
				   "MIME-Version: 1.0",
				   "Content-Type: text/html"]
		headers = "\r\n".join(headers)
		 
		session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		 
		session.ehlo()
		session.starttls()
		session.ehlo
		session.login(sender, password)
		 
		session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
		session.quit()

	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login('librelabz@gmail.com', 'friendlyarm')
	mail.list()
	# Out: list of "folders" aka labels in gmail.
	mail.select("inbox") # connect to inbox.
	result, data = mail.search(None, "ALL")
	
	ids = data[0] # data is a list.
	id_list = ids.split() # ids is a space separated string
	latest_email_id = id_list[-1] # get the latest
	result, data = mail.uid('search', None, "ALL") # search and return uids instead
	latest_email_uid = data[0].split()[-1]
	if condn!=latest_email_uid:
		condn=latest_email_uid
		print condn
		result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
		#print data
		raw_email = data[0][1]
		email_message = email.message_from_string(raw_email)
		subject=email_message['Subject']
		From=email_message['From']
		print subject
		SERIALPORT = "/dev/ttyUSB0" # Change this to your serial port!
		# Set up serial port
		try:
			ser = serial.Serial(SERIALPORT, 9600)
			print "serial ok"
		except serial.SerialException:
			print "serial fail"
			sys.exit()
		if subject=="turnon":
			ser.write('M')	
			print "M"
		elif subject=="turnoff": 
			ser.write('N')	
			print "N"
		elif subject=="status":
			ser.write('S')
			stat=ser.readline()
			stat=stat.strip()
			print stat
			if stat=="0":
				message="Device is in now OFF"
				print message
				x=reply()
			elif stat=="1":
				message="Device is now ON"
				print message
				x=reply()
	

		# Close serial port
		ser.close()
	else:
		print "Pass"
