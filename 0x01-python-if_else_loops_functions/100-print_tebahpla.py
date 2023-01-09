#!/usr/bin/python3
for ch in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(ch, chr(ch - 33)), end="")
