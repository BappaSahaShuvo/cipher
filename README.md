🔑 Caesar Cipher (Python)

A simple Python implementation of the Caesar Cipher, one of the oldest encryption techniques.
This program lets you encode and decode messages by shifting letters of the alphabet while keeping spaces, numbers, and punctuation unchanged.

🚀 Features

Encode and decode messages with a shift key

Works with uppercase and lowercase letters

Keeps spaces, numbers, and punctuation unchanged

Simple interactive CLI

Loop support (encrypt/decrypt multiple times without restarting)

📂 Project Structure
caesar-cipher/
│── cipher.py   # Main Caesar Cipher script
│── README.md   # Project documentation
│── LICENSE     # License file (MIT recommended)

▶️ How to Run

Clone this repository:

git clone https://github.com/YourUsername/caesar-cipher.git
cd caesar-cipher


Run the program:

python cipher.py


Example interaction:

🔑🔡➡️ Welcome to Caesar Cipher 🔡🔑
Type 'encode' to encrypt or 'decode' to decrypt:
encode
Type your message:
Hello World!
Type the shift number:
5
The encoded text is: Mjqqt Btwqi!
Do you want to go again? Type 'yes' or 'no':

📝 Examples

Encoding

Message: hello world!
Shift: 5
Output: mjqqt btwqi!


Decoding

Message: mjqqt btwqi!
Shift: 5
Output: hello world!

📌 Future Improvements

Add GUI or Web version

Support for different ciphers (Vigenère, ROT13, etc.)

File encryption & decryption

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.
