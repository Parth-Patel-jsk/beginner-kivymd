from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

def close_dialog_farmer(self, instance):
    self.dialog.dismiss()

def reload_signup_screen_farmer(self, instance):
    self.close_dialog_farmer(instance)
    screen_manager = self.root
    if 'signupf' in screen_manager.screen_names:
        signupf_screen = screen_manager.get_screen('signupf')
        if hasattr(self, 'saved_new_email_farmer'):
            signupf_screen.ids.new_email_farmer.text = self.saved_new_email_farmer
        if hasattr(self, 'saved_new_password_farmer'):
            signupf_screen.ids.new_password_farmer.text = self.saved_new_password_farmer

        # Clear the saved data
        self.saved_new_email_farmer = ""
        self.saved_new_password_farmer = ""
        screen_manager.current = 'signupf'
    else:
        print("Signup screen not found in ScreenManager")

def reload_login_screen_farmer(self, instance):
    self.close_dialog_farmer(instance)
    screen_manager = self.root
    loginf_screen = screen_manager.get_screen('loginf')

    # Restore saved email and password
    if self.saved_email_farmer:
        loginf_screen.ids.email_farmer.text = self.saved_email_farmer
    if self.saved_password_farmer:
        loginf_screen.ids.password_farmer.text = self.saved_password_farmer

    # Clear the saved data
    self.saved_email_farmer = ""
    self.saved_password_farmer = ""
    screen_manager.current = 'loginf'

def show_missing_dialog_farmer(self, message):
    self.dialog = MDDialog(
        title="Error",
        text=message,
        size_hint=(0.7, 1),
        buttons=[
            MDRaisedButton(
                text="OK",
                on_release=self.reload_current_screen_farmer
            )
        ]
    )
    self.dialog.shadow_color = [0, 0, 0, 0]
    self.dialog.open()

def show_already_registered_dialog_farmer(self):
    self.dialog = MDDialog(
        title="Email Already Registered",
        text="This email is already registered. Please use a different email.",
        size_hint=(0.5, 1),
        buttons=[
            MDRaisedButton(
                text="OK",
                on_release=self.reload_signup_screen_farmer
            )
        ]
    )
    self.dialog.shadow_color = [0, 0, 0, 0]
    self.dialog.open()

def reload_current_screen_farmer(self, instance):
    self.close_dialog_farmer(instance)
    screen_manager = self.root
    current_screen = screen_manager.current

    if current_screen == 'signupf':
        self.reload_signup_screen_farmer(instance)
    elif current_screen == 'loginf':
        self.reload_login_screen_farmer(instance)
def show_error_email_format_farmer(self, message):
        self.dialog = MDDialog(
                text=message,
                buttons=[MDRaisedButton(text="OK", on_release=self.reload_current_screen_farmer)]
        )
        self.dialog.shadow_color = [0, 0, 0, 0]
        self.dialog.open()


def handle_successful_signup_farmer(self):
    screen_manager = self.root
    signup_screen = screen_manager.get_screen('signupf')

    # Clear data in the signup screen
    signup_screen.ids.new_username_farmer.text = ""
    signup_screen.ids.new_email_farmer.text = ""
    signup_screen.ids.new_password_farmer.text = ""

    # Redirect to otp  screen
    screen_manager.current = 'otpf'

def show_wrong_password_farmer(self,message):
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
def show_wrong_password_email_farmer(self,message):
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
def reload_main_screen_farmer(self, instance):
    self.close_dialog_farmer(instance)
    screen_manager = self.root
    if 'main' in screen_manager.screen_names:
        main_screen = screen_manager.get_screen('main')
        self.saved_new_username_farmer=""
        # Clear the saved data
        self.saved_new_email_farmer = ""
        self.saved_new_password_farmer = ""
        screen_manager.current = 'main'
    else:
        print("Signup screen not found in ScreenManager")

def show_wrong_otp_farmer(self,message):
    self.dialog = MDDialog(
        title="Error",
        text=message,
        size_hint=(0.7, 1),
        buttons=[
            MDRaisedButton(
                text="OK",
                on_release=self.reload_main_screen_farmer
            )
        ]
    )
    self.dialog.shadow_color = [0, 0, 0, 0]
    self.dialog.open()
