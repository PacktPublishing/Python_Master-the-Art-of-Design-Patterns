from random import random
import csv

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ListProperty


class ColorBox(Widget):
    color = ListProperty([random(), random(), random()])


class ColorClassifierApp(App):
    def __init__(self):
        super(ColorClassifierApp, self).__init__()
        self.file = csv.writer(open("colors.csv", "a"))

    def store_color(self, color_name):
        self.file.writerow(self.root.colorbox.color + [color_name])
        self.root.colorbox.color = [random(), random(), random()]

ColorClassifierApp().run()
