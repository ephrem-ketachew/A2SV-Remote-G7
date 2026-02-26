n = int(input())

string = input()
# "ACTG"

A = ord('A') - 65
C = ord('C') - 65
T = ord('T') - 65
G = ord('G') - 65

min_ops = float('inf')
for i in range(len(string) - 3):
    a = ord(string[i]) - 65
    b = ord(string[i + 1]) - 65
    c = ord(string[i + 2]) - 65
    d = ord(string[i + 3]) - 65
    
    ops = 0
    
    ops += min(abs(a - A), 26 - abs(a - A))
    ops += min(abs(b - C), 26 - abs(b - C))
    ops += min(abs(c - T), 26 - abs(c - T))
    ops += min(abs(d - G), 26 - abs(d - G))
    
    min_ops = min(min_ops, ops)
    
print(min_ops)
    