#coding=utf-8
from io import StringIO, BytesIO
source_file = StringIO("an oft-repeated cliché")
dest_file = BytesIO()

char = source_file.read(1)
while char:
    dest_file.write(char.encode("ascii", "replace"))
    char = source_file.read(1)

print(dest_file.getvalue())

