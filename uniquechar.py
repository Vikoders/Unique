def firstUniqChar(s):
    char_freq = {}

    # Count the frequency of each character
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1

    # Find the first non-repeating character
    for i, char in enumerate(s):
        if char_freq[char] == 1:
            return i

    return -1
# Example 1
s1 = "leetcode"
print(firstUniqChar(s1))
# Output: 0

# Example 2
s2 = "loveleetcode"
print(firstUniqChar(s2))
# Output: 2

# Example 3
s3 = "aabb"
print(firstUniqChar(s3))
# Output: -1