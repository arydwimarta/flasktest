from smtplib import SMTP
#from email.MIMEText import MIMEText
from email.mime.text import MIMEText
from email.Header import Header
from email.Utils import parseaddr, formataddr

def send_email(sender, recipient, subject, body):
	header_charset = 'ISO-8859-1'
	for body_charset in 'US-ASCII', 'ISO-8859-1', 'UTF-8':
		try:
			body.encode(body_charset)
		except UnicodeError:
			pass
		else:
			break

	sender_name, sender_addr = parseaddr(sender)
	recipient_name, recipient_addr = parseaddr(recipient)

	sender_name = str(Header(unicode(sender_name), header_charset))
	recipient_name = str(Header(unicode(recipient_name), header_charset))

	sender_addr = sender_addr.encode('ascii')
	recipient_addr = recipient_addr.encode('ascii')

	msg = MIMEText(body.encode(body_charset), 'plain', body_charset)
	msg['From'] = formataddr((sender_name, sender_addr))
	msg['To'] = formataddr((recipient_name, recipient_addr))
	msg['Subject'] = Header(unicode(subject), header_charset)

	smtp = SMTP("localhost")
	smtp.sendmail(sender, recipient, msg.as_string())
	smtp.quit()