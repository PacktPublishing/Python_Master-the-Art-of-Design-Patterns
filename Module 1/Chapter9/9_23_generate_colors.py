from random import random


def generate_colors(count=100):
    for i in range(count):
        yield (random(), random(), random())

for color in generate_colors():
    print(color)
