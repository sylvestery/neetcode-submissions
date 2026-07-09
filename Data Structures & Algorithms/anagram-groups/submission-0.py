class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            count[key].append(word)
        return list(count.values())