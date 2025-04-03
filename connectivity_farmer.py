import mysql.connector
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
import re
import smtplib
import random
import string
otp=None
def connect_to_database():

    connection = mysql.connector.connect(
        host='localhost',
        database='kivy',
        user='root',
        password='krrish1234'
        )
    return connection
def is_valid_email_farmer(email):
    # Regular expression to validate email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None
def signup_check_farmer(self,new_username_farmer,new_email_farmer,new_password_farmer):
    global otp
    if not is_valid_email_farmer(new_email_farmer):
        self.show_error_email_format_farmer("Invalid email format.")
        return
    #  if new_username:
    if new_email_farmer:
        if email_registered_farmer(new_email_farmer):
                print("Already registered")
                self.show_already_registered_dialog_farmer()
        else:
                if new_password_farmer and new_email_farmer and new_username_farmer:
                     
                    print("Not registered")
                    # self.root.current="login"
                    insert_user_farmer(new_username_farmer,new_email_farmer, new_password_farmer)
                    self.receiver_email=new_email_farmer
                    otp= self.generate_otp_farmer()  # Generate an OTP
                    receiver_email = new_email_farmer
                    send_otp_via_email_farmer(self.receiver_email, otp)
                    self.handle_successful_signup_farmer()
    else:
        print("Please enter email")
def check_login_farmer(self,email_farmer,password_farmer):
    if not is_valid_email_farmer(email_farmer):
        self.show_error_email_format_farmer("Invalid email format.")
        return

    if email_farmer and password_farmer:
        if email_registered_farmer(email_farmer):
            if check_password_farmer(self,email_farmer, password_farmer):
                l_farmer(self,email_farmer,password_farmer)
                self.root.current = "homef"
                print("Correct")
            else:
                print("Error", "Invalid password.")
                self.show_wrong_password_farmer("password inserted is wrong")
        else:
            print("Error", "Email not registered.")
            self.show_wrong_password_email_farmer("Email and password are not registered")
    else:
            print("Error", "Please enter both email and password.")

def email_registered_farmer(new_email_farmer):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM farmer WHERE email = %s"
    cursor.execute(query, (new_email_farmer,))
    result = cursor.fetchone()
   
    cursor.close()
    connection.close()
    return result[0] > 0 if result else False
    
def insert_user_farmer(new_username_farmer, new_email_farmer,new_password_farmer):
    connection = connect_to_database()
    cursor = connection.cursor()
    # Only include columns `username`, `email`, and `password`
    query = "INSERT INTO farmer (user, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (new_username_farmer, new_email_farmer, new_password_farmer))
    connection.commit()
    print("User inserted successfully.")
    cursor.close()
    connection.close()
def check_password_farmer(self, email_farmer, password_farmer):
    # Connect to the MySQL database and validate the password
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT password FROM farmer WHERE email = %s"
    cursor.execute(query, (email_farmer,))
    result = cursor.fetchone()
    if result:
        stored_password = result[0]
        return stored_password == password_farmer  # You should hash and compare passwords in a real-world application
    return False

def show_already_registered_dialog_farmer(app):
    # Call the method from the app instance to show the dialog
    app.show_already_registered_dialog_farmer()

def l_farmer(self,email_farmer,password_farmer):
        # Email= email_customer.text  # Get the entered username
        # passwordw = password_customer.text
        # print(Email)
        # print(passwordw)
        
    
        db = mysql.connector.connect(
            host='localhost', user='root', password='krrish1234', database='kivy'
        )
        cursor = db.cursor()
        cursor.execute("SELECT user FROM farmer WHERE email=%s AND password=%s", (email_farmer, password_farmer))
        result = cursor.fetchone()
        User=str(result[0])
        print(result)
        
        self.screen_manager.get_screen("accountf").ids.welcome_label_farmer.text=User
        # Pass username to account screen
    
def generate_otp_farmer(self,length=6):
    # Generate a random OTP of the given length
    digits = string.digits
    otp = ''.join(random.choice(digits) for i in range(length))
    print(otp)
    
    return otp
    

def send_otp_via_email_farmer(receiver_email, otp):
    # Your email credentials
    sender_email = "farmazon.in@gmail.com"
    app_password = "xtps kifr lbtr oaum"  # Replace with the App Password
    # Setting up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)

    # Craft the message
    subject = "Your OTP Code"
    body = f"Your OTP code is {otp}. It is valid for 10 minutes."
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    server.sendmail(sender_email,receiver_email, message)
    print('OTP Sent')

    # Close the SMTP server connection
    server.quit()
def otp_farmer(self,otp_id,):
    global otp
    value=otp_id
    print(value)
    # print(krrish)
    if otp==value:
         self.show_welcome_email(self.receiver_email)
         self.root.current="loginf"
         
    else:
         self.show_wrong_otp_farmer("Wrong otp inserted")  
def show_welcome_email(self,receiver_email):
    sender_email = "farmazon.in@gmail.com"
    app_password = "xtps kifr lbtr oaum"  # Replace with the App Password
    # Setting up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)

    # Craft the message
    subject = "Welcome to Farmazon! "
    body ="""
We're thrilled to have you join our community of passionate farmers and buyers
Get ready to explore and connect with a vibrant marketplace designed just for you.\nWhether you're here to sell your produce or discover fresh, local products, we're here to help you every step of the way.
Thank you for choosing Farmazon. We're excited to support your journey!
Best Regards
The Farmazon Team"""
    message = f"Subject: Dear {receiver_email}\n{subject}\n\n{body}"

    # Send the email
    server.sendmail(sender_email,receiver_email, message)
    server.quit()
     

