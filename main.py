from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime


Builder.load_file("design.kv")

class MainScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class  Mainapp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    Mainapp().run()