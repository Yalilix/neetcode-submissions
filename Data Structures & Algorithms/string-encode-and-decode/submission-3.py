class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''

        for s in strs:
            ret += str(len(s)) + '#' + s
        
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            k = i + 1
            while s[k] != '#':
                k += 1
            length = int(s[i:k])

            j = k + 1
            ret.append(s[j:j + length])
            i = j + length

        return ret
