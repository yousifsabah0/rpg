#!/usr/bin/env python

import random
import string

import pyperclip

chars = string.ascii_letters + string.digits + string.punctuation

def rpg():
  pyperclip.copy("".join(random.choice(chars) for _ in range(12)))

if __name__ == "__main__":
  rpg()