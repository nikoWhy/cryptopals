string_one = '1c0111001f010100061a024b53535009181c'

string_one_b = bytes.fromhex(string_one)

string_two = '686974207468652062756c6c277320657965'
string_two_b = bytes.fromhex(string_two)

xor1 = b''
for byte in range(0,len(string_one_b)):
    xor = bytes([string_one_b[byte]^string_two_b[byte]])
    xor1 += xor

print(xor1.hex())