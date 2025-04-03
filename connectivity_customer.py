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
def is_valid_email_customer(email):
    # Regular expression to validate email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None
def signup_check_customer(self,new_username_customer,new_email_customer,new_password_customer):
    global otp
    if not is_valid_email_customer(new_email_customer):
        self.show_error_email_format_customer("Invalid email format.")
        return
    #  if new_username:
    if new_email_customer:
        if email_registered_customer(new_email_customer):
                print("Already registered")
                self.show_already_registered_dialog_customer()
        else:
                if new_password_customer and new_email_customer and new_username_customer:
                     
                    print("Not registered")
                    insert_user_customer(new_username_customer,new_email_customer, new_password_customer)
                    self.receiver_email=new_email_customer
                    otp= self.generate_otp_customer()  # Generate an OTP
                    receiver_email = new_email_customer
                    send_otp_via_email_customer(self.receiver_email, otp) 
                    
                    self.handle_successful_signup_customer()
    else:
        print("Please enter email")
def check_login_customer(self,email_customer,password_customer):
    print(f"Email: {email_customer}")
    print(f"Password:{password_customer}")
    if not is_valid_email_customer(email_customer):
        self.show_error_email_format_customer("Invalid email format.")
        return
    if email_customer and password_customer:
        if email_registered_customer(email_customer):
            if check_password_customer(self,email_customer, password_customer):
                self.l_customer(email_customer, password_customer)
                self.root.current = "home"
                print("Correct")
            else:
                print("Error", "Invalid password.")
                self.show_wrong_password_customer("password inserted is wrong")
        else:
            print("Error", "Email not registered.")
            self.show_wrong_password_email_customer("Email and password are not registered")
    else:
            print("Error", "Please enter both email and password.")
            
def email_registered_customer(email_customer):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT  1 FROM customer WHERE email = %s"
    cursor.execute(query, (email_customer.strip(),))
    resultt = cursor.fetchone()
    print(resultt)
    return resultt is not None
    cursor.close()
    connection.close()
    
    
def insert_user_customer(new_username_customer, new_email_customer ,new_password_customer):
    connection = connect_to_database()
    cursor = connection.cursor()
    # Only include columns `username`, `email`, and `password`
    query = "INSERT INTO customer (user, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (new_username_customer, new_email_customer.strip() , new_password_customer))
    connection.commit()
    print("User inserted successfully.")
    cursor.close()
    connection.close()
def check_password_customer(self, email_customer, password_customer):
    # Connect to the MySQL database and validate the password
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "SELECT password FROM customer WHERE email = %s"
    cursor.execute(query, (email_customer,))
    result = cursor.fetchone()
    if result:
        stored_password = result[0]
        return stored_password == password_customer  # You should hash and compare passwords in a real-world application
    return False

def show_already_registered_dialog_customer(app):
    # Call the method from the app instance to show the dialog
    app.show_already_registered_dialog_customer()
def l_customer(self,email_customer,password_customer):
        
        db = mysql.connector.connect(
            host='localhost', user='root', password='krrish1234', database='kivy'
        )
        cursor = db.cursor()
        cursor.execute("SELECT user FROM customer WHERE email=%s AND password=%s", (email_customer, password_customer))
        result = cursor.fetchone()
        User=str(result[0])
        print(result)
        
        self.screen_manager.get_screen("account").ids.welcome_label.text=User
        # Pass username to account screen
def generate_otp_customer(self,length=6):
    # Generate a random OTP of the given length
    digits = string.digits
    otp = ''.join(random.choice(digits) for i in range(length))
    print(otp)
    
    return otp
    

def send_otp_via_email_customer(receiver_email, otp):
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
def otp_customer(self,otp_id,):
    global otp
    value=otp_id
    print(value)
    # print(krrish)
    if otp==value:
    
        self.show_welcome_email_customer(self.receiver_email)
        self.root.current = "login"

         
    else:
         self.show_wrong_otp_customer("Wrong otp inserted")
def show_welcome_email_customer(self,receiver_email):
    sender_email = "farmazon.in@gmail.com"
    app_password = "xtps kifr lbtr oaum"  # Replace with the App Password
    # Setting up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)

    # Craft the message
    subject = "Welcome to Farmazon! "
    body =""" """
    message = f"Subject: Dear {receiver_email}\n{subject}\n\n{body}"

    # Send the email
    server.sendmail(sender_email,receiver_email, message)
    server.quit()
     

              

    