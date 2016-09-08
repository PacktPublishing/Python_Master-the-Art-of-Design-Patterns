import csv

dataset_filename = 'colors.csv'


def load_colors(filename):
    with open(filename) as dataset_file:
        lines = csv.reader(dataset_file)
        for line in lines:
            yield tuple(float(y) for y in line[0:3]), line[3]

for color, name in load_colors(dataset_filename):
    print("RGB {} is named {}".format(color, name))
