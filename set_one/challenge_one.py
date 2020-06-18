import base64

string  = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
data = bytes.fromhex(string)

bs_data = base64.b64encode(data)

print(bs_data.decode('UTF-8'))