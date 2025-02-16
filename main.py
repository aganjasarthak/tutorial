import smtplib
from email.mime.text import MIMEText

sender_email = "sarthak.aganja12345@gmail.com"
sender_password = " yaha password rakhnu app password"  

# Recipient emails as an array (list)
recipients = ["ribikabaral7@gmail.com", "richagurung2007@gmail.com"]

# Email content
subject = "Simple Test Email"
body = (
    "Hello,\n\n"
    "This is a simple test email sent using Python's smtplib.\n\n"
    "Best regards,\n"
    "Sarthak"
)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)
    
   
    for recipient in recipients:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient 
        
        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"Email sent successfully to {recipient}!")
