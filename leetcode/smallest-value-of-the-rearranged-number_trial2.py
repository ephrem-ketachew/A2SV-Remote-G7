class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        arr_num = list(str(num))
        if num < 0:
            arr_num.sort(reverse=True)
            return int('-' + ''.join(arr_num[:-1]))
        
        arr_num.sort()
        if arr_num[0] == '0':
            i = 1
            while arr_num[i] == '0':
                i += 1
            arr_num[0], arr_num[i] = arr_num[i], arr_num[0]
        
        return int(''.join(arr_num))