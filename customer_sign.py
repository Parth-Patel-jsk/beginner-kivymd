from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

def close_dialog_customer(self, instance):
    self.dialog.dismiss()

def reload_signup_screen_customer(self, instance):
    self.close_dialog_customer(instance)
    screen_manager = self.root
    if 'signup' in screen_manager.screen_names:
        signup_screen = screen_manager.get_screen('signup')
        if hasattr(self, 'saved_new_email_customer'):
            signup_screen.ids.new_email_customer.text = self.saved_new_email_customer
        if hasattr(self, 'saved_new_password_customer'):
            signup_screen.ids.new_password_customer.text = self.saved_new_password_customer

        # Clear the saved data
        self.saved_new_email_customer = ""
        self.saved_new_password_customer = ""
        screen_manager.current = 'signup'
    else:
        print("Signup screen not found in ScreenManager")

def reload_login_screen_customer(self, instance):
    self.close_dialog_customer(instance)
    screen_manager = self.root
    login_screen = screen_manager.get_screen('login')

    # Restore saved email and password
    if self.saved_email_customer:
        login_screen.ids.email_customer.text = self.saved_email_customer
    if self.saved_password_customer:
        login_screen.ids.password_customer.text = self.saved_password_customer

    # Clear the saved data
    self.saved_email_customer = ""
    self.saved_password_customer = ""
    screen_manager.current = 'login'

def show_missing_dialog_customer(self, message):
    self.dialog = MDDialog(
        title="Error",
        text=message,
        size_hint=(0.7, 1),
        buttons=[
            MDRaisedButton(
                text="OK",
                on_release=self.reload_current_screen_customer
            )
        ]
    )
    self.dialog.shadow_color = [0, 0, 0, 0]
    self.dialog.open()
def show_error_email_format_customer(self, message):
        self.dialog = MDDialog(
                text=message,
                buttons=[MDRaisedButton(text="OK", on_release=self.reload_current_screen_customer)]
        )
        self.dialog.shadow_color = [0, 0, 0, 0]
        self.dialog.open()

def show_already_registered_dialog_customer(self):
    self.dialog = MDDialog(
        title="Email Already Registered",
        text="This email is already registered. Please use a different email.",
        size_hint=(0.5, 1),
        buttons=[
            MDRaisedButton(
                text="OK",
                on_release=self.reload_signup_screen_customer
            )
        ]
    )
    self.dialog.shadow_color = [0, 0, 0, 0]
    self.dialog.open()
def show_wrong_password_customer(self,message):
    self.dialog = MDDialog(
        title="Error",
        text=message,
        size_hint=(0.7, 1),
        buttons=[
            MDRaisedButton(
                text="OK",
                on_release=lambda x: self.dialog.dismiss()
            )
        ]
    )
    self.dialog.shadow_color = [0, 0, 0, 0]
    self.dialog.open()
def show_wrong_password_email_customer(self,message):
    self.dialog = MDDialog(
        title="Error",
        text=message,
        size_hint=(0.7, 1),
        buttons=[
            MDRaisedButton(
                text="OK",
                on_release=lambda x: self.dialog.dismiss()
            )
        ]
    )
    self.dialog.shadow_color = [0, 0, 0, 0]
    self.dialog.open()


def reload_current_screen_customer(self, instance):
    self.close_dialog_customer(instance)
    screen_manager = self.root
    current_screen = screen_manager.current

    if current_screen == 'signup':
        self.reload_signup_screen_customer(instance)
    elif current_screen == 'login':
        self.reload_login_screen_customer(instance)

def handle_successful_signup_customer(self):
    screen_manager = self.root
    signup_screen = screen_manager.get_screen('signup')

    # Clear data in the signup screen
    signup_screen.ids.new_username_customer.text = ""
    signup_screen.ids.new_email_customer.text = ""
    signup_screen.ids.new_password_customer.text = ""

    # Redirect to login screen
    screen_manager.current = 'otp'

def reload_main_screen_customer(self, instance):
    self.close_dialog_customer(instance)
    screen_manager = self.root
    if 'main' in screen_manager.screen_names:
        main_screen = screen_manager.get_screen('main')
        self.saved_new_username_customer=""
        # Clear the saved data
        self.saved_new_email_customer = ""
        self.saved_new_password_customer = ""
        screen_manager.current = 'main'
    else:
        print("Signup screen not found in ScreenManager")

def show_wrong_otp_customer(self,message):
    self.dialog = MDDialog(
        title="Error",
        text=message,
        size_hint=(0.7, 1),
        buttons=[
            MDRaisedButton(
                text="OK",
                on_release=self.reload_main_screen_customer
            )
        ]
    )
    self.dialog.shadow_color = [0, 0, 0, 0]
    self.dialog.open()

def show_incorrect_pass(self):
    pass