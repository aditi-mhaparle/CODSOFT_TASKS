import random
import string
length = int(input("Enter the length of password:"))
chars = string.ascii_letters + string.digits + string.punctuation 
Password = "".join(random.choices(chars,k=length))
print("Password: ",Password)