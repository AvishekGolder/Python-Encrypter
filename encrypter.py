from hashlib import sha512

a = input("Enter anything: ")

print(sha512(a.encode('utf-8')).hexdigest())
