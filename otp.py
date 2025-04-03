import smtplib
import random
import string

def generate_otp(length=6):
    # Generate a random OTP of the given length
    digits = string.digits
    otp = ''.join(random.choice(digits) for i in range(length))
    return otp

def send_otp_via_email(receiver_email, otp):
    # Your email credentials
    sender_email = "2021aditya29@gmail.com"
    app_password = "kpkt zohy wnza qnfv"  # Replace with the App Password

    # Setting up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)

    # Craft the message
    subject = "Your OTP Code"
    body = f"Your OTP code is {otp}. It is valid for 10 minutes."
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    server.sendmail(sender_email, receiver_email, message)
    print('OTP Sent')

    # Close the SMTP server connection
    server.quit()

if __name__ == "__main__":
    receiver_email = "krrishgurbani333@gmail.com"  # Replace with the recipient's email
    otp = generate_otp()
    send_otp_via_email(receiver_email, otp)
