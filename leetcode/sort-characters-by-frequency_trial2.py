class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        arr = []
        for ch in counter:
            arr.append(ch * counter[ch])

        return ''.join(sorted(arr, key=len, reverse=True))