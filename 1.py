# Write a program in python to generate MD5 of string data.
#  python to generate MD5 of string data is as follows:
 import hashlib
 given-str=b"hellow world"
 given-str-2=b"hellow world!!"
 md5-value=hashlib.md5(given-str) 
 md5-value-2=hashlib.md5(given-str-2)
 print(md5-value.hexdigest())
  print(md5-value-2.hexdigest())
  #output:3e25960a79dbc69b674cd4ec67a72c62
  #10f73d16d32cf89e1f7cab7589be965b