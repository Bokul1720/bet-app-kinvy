
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

API_URL = "http://your-api-domain.com"  # Replace with your actual FastAPI backend URL

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.login_btn = Button(text='Login')
        self.message = Label()

        self.login_btn.bind(on_press=self.login)

        self.add_widget(Label(text='Bet App Login', font_size=24))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.login_btn)
        self.add_widget(self.message)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        try:
            res = requests.post(f"{API_URL}/login", json={
                "username": username,
                "password": password
            })
            if res.status_code == 200:
                data = res.json()
                self.message.text = f"Welcome {data['username']} | Coins: à§³{data['coins']}"
            else:
                self.message.text = "Login failed. Try again."
        except Exception as e:
            self.message.text = f"Error: {str(e)}"

class BetApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    BetApp().run()
