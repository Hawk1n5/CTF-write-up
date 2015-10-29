from pwn import *
import sha, socket, re, itertools, sys

def pow(base):
        letters = [' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')',
                '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5',
                '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A',
                'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}',
                '~']

        for c in itertools.combinations_with_replacement(letters, 5):
                a = "".join(c)
                if sha.new(base+a).digest().endswith("\xff\xff\xff"):
                        return base+a
#r = remote('127.0.0.1',4444)
#r = process('./web_of_science3')
res = str(pow(sys.argv[1]))
print res
