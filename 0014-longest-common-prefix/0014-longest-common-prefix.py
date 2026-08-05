class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        res = ""
        first = strs[0]

        for i in range(len(first)):

            for j in range(1, len(strs)):

                if i >= len(strs[j]) or strs[j][i] != first[i]:
                    return res

            res += first[i]

        return res