# https://www.youtube.com/watch?v=sUicrnHwA0s
# ----------specification-----------
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc" with the lenght of 3

# Input: "bbbbbb"
# Output: 1
# Explanation: The answer is "b" with the lenght of 1

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke" with the lenght of 3
# the answer must be a SUBSTRING, "pwke" is a SUBSEQUENCE
# and not a SUBSTRING

# ---------------notes--------------
# abcdecfab
# the key of substring is continuous sequence of a string, NO SKIP letter
# the requirement is no duplicated letter in a substring
# for an invalid substring, the last char is duplicated with any char of the front
# SO, any char before the duplicated char should be deprecated
# they are shorter than the current invalid substring
# they will face the same invalid situation
# it's better to think before code, but don't hesitate too long
# in this case, the current pointer keeps on going and the seen chars will change
#
def lengthOfLongestSubstring(string1):
    sub = {}
    cur_sub_start = 0
    cur_len = 0
    longest = 0

    for i, letter in enumerate(string1):
        if letter in sub and sub[letter] >= cur_sub_start:
            cur_sub_start = sub[letter] + 1
            cur_len = i - sub[letter]
            sub[letter] = i
        else:
            sub[letter] = i
            cur_len += 1
            if cur_len > longest:
                longest = cur_len
    print(longest)
    return longest


lengthOfLongestSubstring("abcdecfab")
