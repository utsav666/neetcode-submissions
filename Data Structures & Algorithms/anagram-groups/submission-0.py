class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sample_dict = {}
        for val in strs:
            sample_key = "".join(sorted(val))
            if sample_key in sample_dict :
                sample_dict[sample_key].append(val)
            else:
                sample_dict[sample_key] = [val]
        return list(sample_dict.values())