def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    else:
        longest = 0
        for i in range(len(s)):
            temp = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in temp:
                    temp += s[j]
                else:
                    break
            if len(temp) > longest:
                longest = len(temp)
        return longest

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring(""))
    print(lengthOfLongestSubstring(" "))
    print(lengthOfLongestSubstring("au"))
    print(lengthOfLongestSubstring("dvdf"))
    print(lengthOfLongestSubstring("abba"))
    print(lengthOfLongestSubstring("tmmzuxt"))
    print(lengthOfLongestSubstring("aab"))