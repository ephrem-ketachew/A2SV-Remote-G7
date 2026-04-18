class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        result = []
        for i, char in enumerate(expression):
            if char in '+*-':
                left_result = self.diffWaysToCompute(expression[:i])
                right_result = self.diffWaysToCompute(expression[i + 1:])
                
                for l in left_result:
                    for r in right_result:
                        if char == '*':
                            result.append(l * r)
                        elif char == '+':
                            result.append(l + r)
                        elif char == '-':
                            result.append(l - r)
                            
        return result