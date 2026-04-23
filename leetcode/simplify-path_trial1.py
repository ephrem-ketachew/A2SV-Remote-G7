class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path + '/'
        stack = []
        n, i = len(path), 0
        buffer = []
        while i < n:
            if path[i] == '/':
                if len(buffer) == 2 and buffer[0] == buffer[1] == '.':
                    if stack:
                        stack.pop()
                elif len(buffer) > 1 or len(buffer) == 1 and buffer[0] != '.':
                    stack.append(''.join(buffer))    
                buffer = []
            else:
                buffer.append(path[i])

            i += 1
                
        return '/' + '/'.join(stack)