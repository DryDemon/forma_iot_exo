#!/usr/bin/env python3
import os
from Crypto.Util.number import inverse
from Crypto.PublicKey import RSA


modulus = 0

e = 0

p = 0 
q = 0


 
privkey = RSA.construct(...)
 
with open("privkey.pem", "wb") as fp:
    fp.write(privkey.exportKey())