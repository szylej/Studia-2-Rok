b1 = "0011"
b2 = "1100"

b3 = bytes(b1, encoding='bin')

byte_val = b3
int_val = int.from_bytes(byte_val, "big")
print(int_val)


