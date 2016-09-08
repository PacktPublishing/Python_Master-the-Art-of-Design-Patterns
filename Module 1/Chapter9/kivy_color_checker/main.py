from random import random
import csv

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty, StringProperty


class ColorBox(Widget):
    color = ListProperty([random(), random(), random()])


class ColorCheckerApp(App):
    score = NumericProperty()
    color_name = StringProperty()
    color = ListProperty([0, 0, 0])
    total = NumericProperty()
    correct = NumericProperty()

    def __init__(self):
        super(ColorCheckerApp, self).__init__()
        self.file = csv.reader(open("output.csv", "r"))
        self.advance_color()

    def advance_color(self):
        try:
            r, g, b, name = next(self.file)
        except StopIteration:
            self.root.disabled = True
        else:
            self.color = float(r), float(g), float(b)
            self.color_name = name

    def process_response(self, is_correct):
        if is_correct:
            self.correct += 1
        self.total += 1
        self.score = 100.0 * self.correct / self.total
        self.advance_color()


ColorCheckerApp().run()
