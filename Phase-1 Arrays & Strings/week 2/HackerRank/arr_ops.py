# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

n = int(input())

arr = []
for _ in range(n):
    line = input().strip().split()
    command = line[0]
    if command == 'insert':
        i, e = int(line[1]), int(line[2])
        arr.insert(i, e)
    elif command == 'print':
        print(arr)
    elif command == 'remove':
        e = int(line[1])
        arr.remove(e)
    elif command == 'append':
        e = int(line[1])
        arr.append(e)
    elif command == 'sort':
        arr.sort()
    elif command == 'pop':
        arr.pop()
    else:
        arr.reverse()