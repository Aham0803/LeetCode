class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freq ={}
        
        # for word in strs:
        #     key = ''.join(sorted(word))
        #     if key not in freq:
        #         freq[key] = []
            
        #     freq[key].append(word)
        # return list(freq.values())

        # freq = {}
        # for word in strs:
        #     key = ''.join(sorted(word))
        #     if key not in freq:
        #         freq[key] = []
        #     freq[key].append(word)
        # return list(freq.values())

        d={}
        for word in strs:
            key=''.join(sorted(word))
            if key in d:
                d[key].append(word)
            else:
                d[key]=[word]
        return list(d.values())











