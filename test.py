# import random
# print (random.randrange(60000, 65535, 3))
# message="hello"
# processed_input=message.split()
# if(processed_input[0]=="hello"):
# 	print("inside if")
# print(processed_input[0])

# a=10
# d={}
# def some():
# 	globals()['d[p]']=10
# 	# print(a)

# some()
# print(d[p])
# print(a)


import sympy   
import random
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import hashlib
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
 
# p=(sympy.randprime(100000, 1000000))
# print(p)
# g=(sympy.randprime(10000, 100000))
p=23
g=9

# alice side

a = random.randint(10000,50000)
# print(a)
ka=pow(g,a)
ka=ka%p
# print(ka)

# for bob
b=random.randint(10000,50000)
kb=pow(g,b)
kb=kb%p


# at alice
sharedkeyatA=(pow(kb,a))%p
# print(sharedkeyatA)
# at bob
sharedkeyatB=(pow(ka,b))%p
# print(sharedkeyatB)

#  encrypting at alice side
print ("share key at a: ", sharedkeyatA)
print ("shared keya t b : ", sharedkeyatB)

# repr(sharedkeyatA).encode('utf-8')
theHash = hashlib.sha256(str(sharedkeyatA).encode("utf-8")).hexdigest()

key = theHash[0:16]
# (theHash.is_triple())
# print(key)
cipher = DES3.new(key, DES3.MODE_ECB)
plaintext = 'Hello india'
while(len(plaintext)%8!=0):
	plaintext+=' '
plaintext = str.encode(plaintext)

# bytes(plaintext, 'utf-8') 
print(type(plaintext))
print(len(plaintext))
msg = cipher.encrypt((plaintext))
print((msg))


# decrypt at bob side
theHash1 = hashlib.sha256(str(sharedkeyatB).encode("utf-8")).hexdigest()

key1 = theHash1[0:16]
# print(key1)
cipher1 = DES3.new(key1, DES3.MODE_ECB)
plaintext1 = msg
print(plaintext1)
msg1 = cipher1.decrypt((plaintext1))
# msg1= str(msg1, errors='ignore')
# .decode(iso8859-1)
# msg1.decode('latin-1')
# msg1=msg1[:-ord(msg1[len(msg1)-1:])]
print((msg1.strip()))

# errors='ignore'