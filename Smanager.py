from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class Manager(ScreenManager):
    pass

app = Builder.load_file("config/config.kv")

class MainApp(App):
    def build(self):
        return app

if __name__ == "__main__":
    MainApp().run()
