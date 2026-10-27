import sys

try:
    print("hello, my name is", sys.argv[1])  #似乎野生windows很难搞这个
except IndexError:
    print("where is your name?")
