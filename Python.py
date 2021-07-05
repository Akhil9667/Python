import hashlib
text=input("Enter text: ")
message=hashlib.md5(text.encode())
print("Encrypted text is: ",message.hexdigest())

