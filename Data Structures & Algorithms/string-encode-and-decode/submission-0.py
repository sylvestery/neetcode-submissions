class Solution:

    def encode(self, strs: List[str]) -> str:
        delimit = "@"
        output = []
        sizes = []
        for s in strs:
            l = len(s)
            sizes.append(l)
            
        output = [f"{str(size)}," for size in sizes]
        output.append('@')
        output.extend(strs)
        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        szs, output, i = [], [], 0
        while s[i] != '@' and i < len(s):
            j = i
            while s[j] != ',':
                j+=1
            szs.append(int(s[i:j]))
            i = j + 1
        i+=1 # skip @
        for sz in szs:
            output.append(s[i: i + sz])
            i+= sz

                    


        return output
