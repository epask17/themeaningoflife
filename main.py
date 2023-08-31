import base64

# Encoded message
encoded_message = "V291bGQgeW91IGxpa2UgdG8gZ28gdG8gZGlubmVyPw=="

# Decode and display
decoded_bytes = base64.b64decode(encoded_message)
decoded_message = decoded_bytes.decode('utf-8')
print(decoded_message)
