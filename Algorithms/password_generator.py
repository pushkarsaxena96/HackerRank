########################################
# Created by pushkar saxena
# Password generator using RANDOM
##########################################

import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = int(input("Enter the password length: "))
p = "".join(random.sample(s,passlen))
print(p)
