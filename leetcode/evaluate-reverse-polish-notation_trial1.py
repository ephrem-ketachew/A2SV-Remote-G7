class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                num_right = stack.pop()
                num_left = stack.pop()
                
                if token == '+':
                    res = num_left + num_right
                elif token == '-':
                    res = num_left - num_right
                elif token == '*':
                    res = num_left * num_right
                else:
                    res = int(num_left / num_right)
                    
                stack.append(res)
            
            else:
                stack.append(int(token))
      
        return stack[0]