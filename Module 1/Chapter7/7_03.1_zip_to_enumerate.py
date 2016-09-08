
def zip_enumerate(container):
    return zip(range(len(container)), container)

for idx, val in zip_enumerate("hello world"):
    print(idx, val)
