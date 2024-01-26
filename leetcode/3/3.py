# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curStart = 0
        longestSubstring = '' if len(s) == 0 else s[0:1]

        # breakpoint()
        for i in range(1, len(s)+1):
            candidate = s[curStart:i]
            #test to see if there's any repetition
            if len(set(candidate)) == len(candidate):
                if len(candidate) > len(longestSubstring):
                    longestSubstring = candidate
            else:
                #find first index where there are no repetitions
                curStart += 1
                candidate = s[curStart:i]
                while len(set(candidate)) < len(candidate):
                    curStart += 1
                    candidate = s[curStart:i]
        return len(longestSubstring)


if __name__ == "__main__":
    s = Solution()
    a1 = s.lengthOfLongestSubstring("abcabcbb")
    assert a1 == 3

    a2 = s.lengthOfLongestSubstring("bbbbb")
    assert a2 == 1

    a3 = s.lengthOfLongestSubstring("pwwkew")
    assert a3 == 3

    a4 = s.lengthOfLongestSubstring(" ")
    assert a4 == 1
    a5 = s.lengthOfLongestSubstring("au")
    assert a5 == 2
