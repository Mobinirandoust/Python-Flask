from collections.abc import Iterable
from random import randint
from random import choice
from string import ascii_lowercase

def unic():
    a = randint(10,30)
    b = randint(10,30)
    c = randint(10,30)
    d = randint(10,30)
    e = randint(10,30)
    return a * b * c*  d * e

def email_fake():
    ema = ""
    for i in [1,2,3,4,5]:
        ema = ema + choice(ascii_lowercase)
    return ema+"@email.com"

def password_fake():
    ema = ""
    for i in range(8):
        ema = ema + choice(ascii_lowercase)
    return ema