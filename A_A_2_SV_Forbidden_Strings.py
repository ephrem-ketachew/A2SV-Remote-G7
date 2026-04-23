n = int(input())

letters = "ASV"

sub_strings = []
def backrack(current_state: list[str]) -> None:
    if len(current_state) == n:
        sub_strings.append(''.join(current_state[:]))
        return
    
    for i in range(3):
        if not current_state or (current_state[-1] != letters[i]):
            current_state.append(letters[i])
            if len(current_state) < 3 or not(current_state[-3] == 'S' and current_state[-2] == 'V' and current_state[-1] == 'A'):
                backrack(current_state)
            current_state.pop()
            
backrack([])
print(len(sub_strings))