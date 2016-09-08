b = bytearray(b"abcdefgh")
b[4:6] = b"\x15\xa3"
print(b)
