# Write a program in python to generate hashes of string data using three algrothm from hislib.
#a) using MD5 algorithm
import hashlib
hash-object=hashlib.md5(b"hellow world")
print(hash-object.hexdigest()
#output:3e25960a79dbc69b674cd4ec67a72c62

#b) using SHA 1 algorithm:
import hashlib
hash-object= hashlib.sha1(b"hellow world")
hex-dig=hash-object.hexdigest()
print(hex-dig)
#7b502c3a1f48c8609ae212cdfb639dee39673f5e

#c) using OPENSSL algorithm:
import hashlib
hash-object=hashlib.new("ripemd160")
hash-object.hexdigest()
print(hash-object.hexdigest())
#output:- dbea7bd24eef40a2e79387542e36dd408b77b21a