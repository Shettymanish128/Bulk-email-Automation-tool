import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ID = '' #email id from which you need to send to others in bulk
EMAIL_PASSWORD = '' #16 character app password used to access to the google account 
 
# Image path
logo_path = r'C:\Users\ADMIN\OneDrive\Desktop\demogit\demo\istockphoto-1156623418-612x612.jpg' #put your logo or any image

# HTML content with purple theme and tagline
def create_html_content(name):
    html = f"""
<html>
  <body style="background-color: #2e2e2e; font-family: Arial, sans-serif; text-align: center; padding: 30px; color: #ffffff;">
    <img src="cid:logo_image" alt="Logo" style="width: 100px; margin-bottom: 20px;">

    <h2 style="color: #ffffff;">Hi {name},</h2>

    <p style="font-size: 18px; color: #90ee90;">
      Your registration for the <strong>King of Kings Picnic Point</strong> is confirmed!
    </p>

    <p style="font-size: 16px; color: #f5f5f5; margin-top: 25px;">
      Are you ready to let go and just chill?
    </p>

    <p style="font-size: 15px; color: #dddddd;">
      Get set for a day filled with laughter, memories, and pure island vibes.
    </p>

    <p style="margin-top: 40px; font-size: 14px; color: #cccccc;">
      Regards,<br><strong>Team CDC ❤️</strong>
    </p>
  </body>
</html>
"""
    return html



# Function to send email with inline logo
def send_email(to_email, name):
    msg = MIMEMultipart('related')
    msg['Subject'] = "Your Picnic Registration Confirmation"
    msg['From'] = EMAIL_ID
    msg['To'] = to_email

    # HTML part
    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    html_content = create_html_content(name)
    msg_alternative.attach(MIMEText(html_content, 'html'))

    # Attach logo image
    if os.path.exists(logo_path):
        with open(logo_path, 'rb') as f:
            logo = MIMEImage(f.read(), name=os.path.basename(logo_path))
            logo.add_header('Content-ID', '<logo_image>')
            logo.add_header('Content-Disposition', 'inline', filename="logo.png")
            msg.attach(logo)
    else:
        print("❌ Logo not found!")

    # Send the email
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ID, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ID, to_email, msg.as_string())
    server.quit()
    print(f"✅ Email sent to {name} ({to_email})")

# List of recipients
recipients = [
    ('Vishnu Shetty', 'shettymanishv@gmail.com')
    # Add more recipients if needed
]

# Sending the emails
for name, email in recipients:
    send_email(email, name)
