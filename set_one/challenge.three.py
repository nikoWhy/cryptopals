hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#char_freq = b'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz '
hex_string_b = bytes.fromhex(hex_string)

for b1 in range(32,127):
    decrypted_b = b''
    for b2 in hex_string_b:
        xor = bytes([b1^b2])
        decrypted_b += xor
    if ('o' and 'i' and 'a' and 'e' and ' ') in decrypted_b.decode('UTF-8',errors='ignore'):
        print(decrypted_b.decode('UTF-8', errors='ignore'))
        print(bytes([b1]).decode('UTF-8'))