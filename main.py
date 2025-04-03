from kivy.core.text import LabelBase
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivy.lang import Builder
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.core.window import Window
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.boxlayout import MDBoxLayout
from connectivity_farmer import l_farmer,insert_user_farmer,check_login_farmer,email_registered_farmer,signup_check_farmer
from connectivity_farmer import is_valid_email_farmer,otp_farmer,send_otp_via_email_farmer,generate_otp_farmer,show_welcome_email
from connectivity_customer import is_valid_email_customer,l_customer,send_otp_via_email_customer,otp_customer,generate_otp_customer
from connectivity_customer import show_welcome_email_customer,insert_user_customer,check_login_customer,email_registered_customer,signup_check_customer
from farmer_sign import show_wrong_password_farmer, show_wrong_password_email_farmer,show_wrong_otp_farmer
from farmer_sign import close_dialog_farmer, reload_signup_screen_farmer, reload_login_screen_farmer, show_missing_dialog_farmer, show_already_registered_dialog_farmer
from farmer_sign import reload_current_screen_farmer, handle_successful_signup_farmer,show_error_email_format_farmer,reload_main_screen_farmer
from customer_sign import close_dialog_customer, reload_signup_screen_customer, reload_login_screen_customer, show_missing_dialog_customer, show_already_registered_dialog_customer
from customer_sign import reload_current_screen_customer, handle_successful_signup_customer,show_wrong_password_customer,show_wrong_password_email_customer
from customer_sign import show_wrong_otp_customer,reload_main_screen_customer
from customer_sign import show_error_email_format_customer
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
import mysql.connector
from kivymd.uix.button import MDRaisedButton    
from kivy.clock import Clock
from time import sleep
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.factory import Factory  # NOQA
from kivy.utils import rgba
from kivymd.uix.card import MDCard
from kivy.config import Config
from kivy.animation import Animation
from kivy.metrics import dp 

Window.size = (310, 580)
class SplashScreen(Screen):
    pass

class Content(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager = None              # This line will hold the screen manager reference/see all button k liye

    def set_manager(self, manager):
        self.manager = manager

class Farmazon(MDApp):
     
     
     def build(self):
        self.saved_email_farmer = ""
        self.saved_new_username_customer=""
        self.saved_password_farmer = ""
        self.saved_new_email_farmer = ""
        self.saved_new_password_farmer = ""
        self.saved_email_customer = ""
        self.saved_password_customer = ""
        self.saved_new_email_customer = ""
        self.saved_new_passwordcustomer = ""


        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_palette = "Blue"
        
        self.screen_manager = ScreenManager()

        Builder.load_file("element_card.kv")

        self.theme_cls.primary_palette = 'Teal'
        self.screen_manager.add_widget(Builder.load_file("splash.kv"))

        self.screen_manager.add_widget(Builder.load_file("main.kv"))

        self.screen_manager.add_widget(Builder.load_file("inventory.kv"))

        self.screen_manager.add_widget(Builder.load_file("login.kv"))

        self.screen_manager.add_widget(Builder.load_file("loginf.kv"))
        self.screen_manager.add_widget(Builder.load_file("faddproduct.kv"))

        self.screen_manager.add_widget(Builder.load_file("signupf.kv"))

        self.screen_manager.add_widget(Builder.load_file("homef.kv"))

        self.screen_manager.add_widget(Builder.load_file("signup.kv"))

        self.screen_manager.add_widget(Builder.load_file("asssk.kv"))

        self.screen_manager.add_widget(Builder.load_file("asksign.kv"))

        self.screen_manager.add_widget(Builder.load_file("home.kv"))

        self.screen_manager.add_widget(Builder.load_file("category.kv"))

        self.screen_manager.add_widget(Builder.load_file("account.kv"))

        self.screen_manager.add_widget(Builder.load_file("accountf.kv"))

        self.screen_manager.add_widget(Builder.load_file("orders.kv"))

        self.screen_manager.add_widget(Builder.load_file("cart.kv"))

        self.screen_manager.add_widget(Builder.load_file("product_details.kv"))
        self.screen_manager.add_widget(Builder.load_file("otp.kv"))
        self.screen_manager.add_widget(Builder.load_file("otpf.kv"))
        self.screen_manager.add_widget(SplashScreen(name="splash"))
        self.screen_manager.add_widget(Builder.load_file("search_result.kv"))
        
        # Start the splash screen
        Clock.schedule_once(self.start_progress, 0)
        return self.screen_manager
     def trigger_animation(self, *args):
         login_screen = self.root.get_screen("login")
         self.anim(login_screen.ids.back)
         self.anim1(login_screen.ids.back1)     

     def start_progress(self, *args):
        # Start updating the progress bar
        Clock.schedule_interval(self.update_progress_bar, 0.05)

     def update_progress_bar(self, dt):
        splash_screen = self.root.get_screen("splash")
        progress_bar = splash_screen.ids.progress_bar

        if progress_bar.value < 100:
            progress_bar.value += 1
        else:
            Clock.unschedule(self.update_progress_bar)
            # Transition to the main screen when the progress bar completes
            self.root.current = "main"  # Replace "main" with your actual main screen name

       
    
     def change_screen(self, screen_name):
        self.root.current = screen_name

     def on_start(self):
        content1 = Content()
        content2 = Content()

        # Retrieve the orders screen
        orders_screen = self.root.get_screen('orders')

        # Add first order with cards for Refund and Return
        orders_screen.ids.expansion_panel.add_widget(
            MDExpansionPanel(
                content=content1,
                panel_cls=MDExpansionPanelOneLine(text="Order 1"),
            )
        )

        # Add second order with cards for Refund and Return
        orders_screen.ids.expansion_panel.add_widget(
            MDExpansionPanel(
                content=content2,
                panel_cls=MDExpansionPanelOneLine(text="Order 2"),
            )
        )


     def show_data(self,text):
        print(f"Recieved Text: {text}")
     def check_otp_customer(self,otp_id):
        otp_customer(self,otp_id.text)
     def check_otp_farmer(self,otp_id):
        otp_farmer(self,otp_id.text)

   #------------Function to take data from user and add to sql table for farmer----------#
     def check_farmer(self,new_username_farmer,new_email_farmer,new_password_farmer):
        if not new_username_farmer.text or not new_email_farmer.text or not new_password_farmer.text:
             self.saved_new_email_farmer = new_email_farmer.text
             self.saved_new_password_farmer = new_password_farmer.text
             self.show_missing_dialog_farmer("All fields are required")
             
        else:
            signup_check_farmer(self,new_username_farmer.text, new_email_farmer.text, new_password_farmer.text)
    # Function to check where login details of user are correct are not
     def login_farmer(self,email_farmer,password_farmer):
        if not email_farmer.text or not password_farmer.text:
            # Show error dialog
            self.show_missing_dialog_farmer("Both email and password are required for login.")
        else:
            check_login_farmer(self,email_farmer.text,password_farmer.text)
    # Use the methods from main2.py
     is_valid_email_farmer=is_valid_email_farmer
     show_error_email_format_farmer=show_error_email_format_farmer
     close_dialog_farmer = close_dialog_farmer
     l_farmer=l_farmer
     show_welcome_email=show_welcome_email
     show_missing_dialog_farmer=show_missing_dialog_farmer
     show_wrong_otp_farmer=show_wrong_otp_farmer
     reload_main_screen_farmer=reload_main_screen_farmer
     otp_farmer=otp_farmer
     generate_otp_farmer=generate_otp_farmer
     send_otp_via_email_farmer=send_otp_via_email_farmer
     reload_signup_screen_farmer = reload_signup_screen_farmer
     reload_login_screen_farmer = reload_login_screen_farmer
     show_wrong_password_farmer=show_wrong_password_farmer
     show_wrong_password_email_farmer=show_wrong_password_email_farmer
     show_already_registered_dialog_farmer = show_already_registered_dialog_farmer
     reload_current_screen_farmer = reload_current_screen_farmer
     handle_successful_signup_farmer = handle_successful_signup_farmer


    #------------Function to take data from user and add to sql table for Customer----------# 
     def check_customer(self,new_username_customer,new_email_customer,new_password_customer):
        if not new_username_customer.text or not new_email_customer.text or not new_password_customer.text:
             self.saved_new_email_customer = new_email_customer.text
             self.saved_new_password_customer = new_password_customer.text
             self.show_missing_dialog_customer("All fields are required")
             
        else:
            signup_check_customer(self,new_username_customer.text, new_email_customer.text, new_password_customer.text)
    # Function to check where login details of user are correct are not
     def login_customer(self,email_customer,password_customer):
        if not email_customer.text or not password_customer.text:
            # Show error dialog
            self.show_missing_dialog_customer("Both email and password are required for login.")
        else:
            check_login_customer(self,email_customer.text,password_customer.text)
    # Use the methods from main2.py
     close_dialog_customer = close_dialog_customer
     is_valid_email_customer=is_valid_email_customer
     show_error_email_format_customer=show_error_email_format_customer
     l_customer=l_customer
     show_welcome_email_customer=show_welcome_email_customer
     generate_otp_customer=generate_otp_customer
     show_wrong_otp_customer=show_wrong_otp_customer
     reload_main_screen_customer=reload_main_screen_customer
     send_otp_via_email_customer=send_otp_via_email_customer
     reload_signup_screen_customer = reload_signup_screen_customer
     reload_login_screen_customer = reload_login_screen_customer
     show_missing_dialog_customer = show_missing_dialog_customer
     show_wrong_password_customer=show_wrong_password_customer
     show_wrong_password_email_customer=show_wrong_password_email_customer
     show_already_registered_dialog_customer = show_already_registered_dialog_customer
     reload_current_screen_customer = reload_current_screen_customer
     handle_successful_signup_customer = handle_successful_signup_customer

     def show_data(self,text):
         print(f"Recieved Text: {text}")

    # HOME UI CARD-IMAGES SWIPE FEATURE CODE.

     current_image = 0
     images = ['image1', 'image2', 'image3']  # List of screen names for images

     def change_image(self, direction):
         self.current_image = (self.current_image + direction) % len(self.images)

        # Access image_manager through root.ids and update the current screen
         self.root.get_screen('home').ids.image_manager.current = self.images[self.current_image]

class ClickableMDCard(MDCard):
     def on_touch_down(self, touch):
         if self.collide_point(*touch.pos):
             self.on_press()
             return super().on_touch_down(touch)

     def on_press(self):
        # Define the behavior when the card is pressed
         pass

# Define MainScreen and CategoryScreen classes
class MainScreen(Screen):
     pass

class CategoryScreen(Screen):
     pass

 


if __name__ == "__main__":
    LabelBase.register(name="MPoppins", fn_regular="Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins ", fn_regular="Poppins-SemiBold.ttf")

    Farmazon().run()
