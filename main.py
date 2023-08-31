def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Encrypted message
encrypted_message = "Jxdii dtz tlqj yt ijqijsi?"

# Decrypt and display
decrypted_message = caesar_decrypt(encrypted_message, 3)
print(decrypted_message)
