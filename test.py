# to create a virtual environment
# python -m venv virtual_env1

import math
import os
import sys

import requests

name = input("Your name? ")
print("Hello ", name)

# print(sys.version)
# print(sys.executable)


def greet(who):
    greeting = "Hello {}".format(who)
    return greeting


r = requests.get("https://www.google.com")
print(r.status_code)
