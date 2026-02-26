password = input()
n = int(input())

words = []
for _ in range(n):
    words.append(input())
    
found = False
for i in range(len(words)):
    if found:
        break
    for j in range(len(words)):
        new_word = words[i] + words[j]
        if password in new_word:
            print('YES')
            found = True
            break
if not found:
    print('NO')