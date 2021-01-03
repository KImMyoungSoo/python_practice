# import this
import sys

# python incoding
print(sys.stdin.encoding)
print(sys.stdout.encoding)

for i in range(1,10) :
    for j in range(1,10):
        print('%d * %d = ' % (i,j), i*j)
    print()
