class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for letters in zip(*strs):
            if len(set(letters)) == 1:
                prefix += letters[0]
            else:
                break
        return prefix