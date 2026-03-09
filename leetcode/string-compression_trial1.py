class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        cnt = 1
        for right in range(1, len(chars)):
            if chars[right] == chars[right - 1]:
                cnt += 1
            else:
                chars[left] = chars[right - 1]
                left += 1
                if cnt > 1:
                    num = list(str(cnt))
                    for d in num:
                        chars[left] = d
                        left += 1

                cnt = 1

        chars[left] = chars[-1]
        left += 1
        if cnt > 1:
            num = list(str(cnt))
            for d in num:
                chars[left] = d
                left += 1

        return left