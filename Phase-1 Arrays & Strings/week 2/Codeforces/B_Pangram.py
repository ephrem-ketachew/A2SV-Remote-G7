n = int(input())
word = input().lower()

if len(set(word)) == 26:
    print('YES')
else:
    print('NO')