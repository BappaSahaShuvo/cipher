# 🔑 Caesar Cipher - Encode & Decode

alphabet = [chr(i) for i in range(97, 123)]  # a-z

def caesar(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():  # only shift letters
            position = alphabet.index(char.lower())
            if direction == "encode":
                new_position = (position + shift) % 26
            else:  # decode
                new_position = (position - shift) % 26
            new_char = alphabet[new_position]
            result += new_char if char.islower() else new_char.upper()
        else:
            # Keep spaces, numbers, punctuation unchanged
            result += char
    return result

print("🔑🔡➡️ Welcome to Caesar Cipher 🔡🔑")

while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    output = caesar(text, shift, direction)
    print(f"The {direction}d text is: {output}")

    again = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
    if again != "yes":
        print("Goodbye! 👋")
        break
