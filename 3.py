#Add salting and iterartion to your hashes.
#ans:-

import uuid
import hashlib
def hash-password(password):
    salt=uuid.uuid4().hex
    return
    hashlib.sha256(salt.encode()+password
    .encode()).hexdigest()+':'+salt
    def check-password
    d(hashed-password,user-password):
    password,salt=hashed-password.split(':')
    return password== hashlib.sha256(salt.encode()+user-password.encode()).hexdigest()
    new-pass=input('please enter a password:')
    hashed-password=hash-password(new-pass)
    print('the string to store in the db is :'+hashed-password)
    old-pass=input('now please enter the password again to check:')
    if check-password( hashed-password,old-pass):
        print('you entered the right password')
    else:
        print('i am sorry but the password does not match')
