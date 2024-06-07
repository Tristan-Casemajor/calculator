from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.label import Label

Config.set('graphics', 'width', '340')
Config.set('graphics', 'height', '506')
Config.set('graphics', 'minimum_width', '340')
Config.set('graphics', 'minimum_height', '506')
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty, ColorProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from math import sqrt


class CalcButton(Button):
    display = StringProperty("")
    calc = StringProperty("")

class BodyCalc(BoxLayout):
    pass


class MainGui(BoxLayout):
    current_calc_text = StringProperty("")
    previous_calc_text = StringProperty("history")
    previous_text_color = ColorProperty((0.524, 0.54, 0.575, 1))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.display_list = []
        self.calc_list = []
        self.display_list_previous = []
        self.calc_list_previous = []

    def build_display_calc_list(self, display, calc):
        if calc in ["sqrt(", "("] and len(self.calc_list) > 0:
            self.calc_list.append(f"*{calc}")
        else:
            self.calc_list.append(calc)

        self.display_list.append(display)
        self.current_calc_text = "".join(self.display_list)
        print(self.calc_list)

    def delete_last(self):
        if len(self.display_list) >= 1:
            del self.display_list[-1]
            del self.calc_list[-1]
            self.current_calc_text = "".join(self.display_list)

    def delete_all(self):
        if len(self.display_list) >= 1:
            self.display_list = []
            self.calc_list = []
            self.current_calc_text = ""

    def use_history(self):
        self.calc_list = self.calc_list_previous
        self.display_list = self.display_list_previous
        self.current_calc_text = "".join(self.display_list)

    def equal(self):
        calc_str = "".join(self.calc_list)
        try:
            result = round(eval(calc_str), 6)
        except:
            self.display_list = []
            self.calc_list = []
            self.current_calc_text = "Error"
        else:
            self.calc_list_previous = self.calc_list
            self.display_list_previous = self.display_list
            self.previous_calc_text = f"{self.current_calc_text} = {result}"
            self.previous_text_color = (1, 1, 1, 1)
            self.display_list = [str(result)]
            self.calc_list = [str(result)]
            self.current_calc_text = str(result)


class HeadCalc(BoxLayout):
    current_calc_label = ObjectProperty(None)
    previous_calc_label = ObjectProperty(None)

    def on_size(self, *args):
        if self.width <= 620:
            self.current_calc_label.size_hint = None, 0.6
            self.previous_calc_label.size_hint = None, 0.4
            self.current_calc_label.width = self.width-dp(8)
            self.previous_calc_label.width = self.width-dp(8)
        else:
            self.current_calc_label.size_hint = 0.8, 0.6
            self.previous_calc_label.size_hint = 0.8, 0.4



class Calculatrice(App):
    def build(self):
        return MainGui()


Calculatrice().run()