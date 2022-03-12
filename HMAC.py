#! usr/bin/python
from Crypto.Hash import HMAC,SHA1


with open('hmac.txt','w') as message:
	message.write('This is a dummy text for generating HMAC using SHA-1 algorithm')
message.close()

with open('hmac.txt','r') as message:
	file_content=message.read()
message.close()


key = b'Ozair127565308890'
hash = HMAC.new(key, digestmod=SHA1)
msg =  bytes(file_content, 'utf-8')
hash.update(msg)
HMAC = hash.hexdigest()

print (f"{msg =}\n{HMAC =}")






