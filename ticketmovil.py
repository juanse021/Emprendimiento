import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

LabelBase.register(
    name = "Roboto",
    fn_regular = "./font/Roboto-Thin.ttf",
    fn_bold = "./font/Roboto-Medium.ttf"
)


class Screen1(Screen):
    pass

class Screen2(Screen):
    saldos = [1800, 3600, 5400]
    pasaje = random.choice(saldos)
    ticket = 0
    
    def consultar_saldo(self):
        box = BoxLayout(orientation = "vertical")
        cerrar = Button(text = "Cerrar", size_hint_y = 0.1, bold = True)
        texto = Label(text = "su saldo es: " + str(self.pasaje), bold = True)
        box.add_widget(texto)
        box.add_widget(cerrar)
        popup = Popup(
            title = "Consular Saldo",
            content = box,
            auto_dismiss = False
            )
        cerrar.bind(on_press = popup.dismiss)
        popup.open()
        print("Su saldo es: ", self.pasaje)

    def generar_ticket(self):

        box = BoxLayout(orientation = "vertical")
        cerrar = Button(text = "Cerrar", size_hint_y = 0.1, bold = True)
        imagen = Image(source = "images/megatarjeta.jpg")
        box.add_widget(imagen)
        box.add_widget(cerrar)
        popup = Popup(
            title = "TicketMovil",
            content = box,
            auto_dismiss = False
            )
        cerrar.bind(on_press = popup.dismiss)
        popup.open()

        if (self.pasaje == 0):
            self.pasaje = 0
            self.ticket += 0
            print("Saldo insuficiente ...")

        elif (self.pasaje == 1800):
            self.pasaje -= 1800
            self.ticket += 1 
            print("Ha comprado: ", self.ticket, "tickets")   

        elif (self.pasaje == 3600):
            self.pasaje -= 1800
            self.ticket += 1 
            print("Ha comprado: ", self.ticket, "tickets")   

        elif (self.pasaje == 5400):
            self.pasaje -= 1800
            self.ticket += 1 
            print("Ha comprado: ", self.ticket, "tickets")      

class Screen3(Screen):
    pass

class Manager(ScreenManager):
    pass


kv = Builder.load_file("config/config.kv")



class MainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MainApp().run()