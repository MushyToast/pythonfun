from Crypto.Cipher import AES

message = input("Enter your message: ")
key = input("Enter your key: ")

obj = AES.new(key)
text = obj.encrypt(message)

print(text)
with open ('encrypted.txt', 'w') as f:
    f.write(str(text))