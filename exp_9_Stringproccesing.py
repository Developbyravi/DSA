def naive_string_matching(text, pattern):
    """
    Function to find all occurrences of 'pattern' in 'text'
    using the Naïve String Matching Algorithm.
    
    :param text: The main text string (length n)
    :param pattern: The pattern to be searched (length m)
    :return: List of starting indices where pattern is found
    """
    n = len(text)
    m = len(pattern)
    indices = []

    print(f"🔍 Searching for pattern '{pattern}' in text '{text}'")

    # Loop over all possible shifts of pattern within text
    for i in range(n - m + 1):  # up to n-m inclusive
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            indices.append(i)
            print(f"✅ Pattern found at index {i}")
    if not indices:
        print("❌ No match found.")
    return indices

# ---------------------------------------------------------------
# Example Execution
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Input text and pattern
    text = "ABAAABCDBBABCDDEABCABCD"
    pattern = "ABC"

    result = naive_string_matching(text, pattern)

    print("------------------------------------------------")
    print(f"📄 Text: {text}")
    print(f"🔎 Pattern: {pattern}")
    print(f"📍 Pattern found at indices: {result}")



#  Experiment No.: 9
# Title:
# String Processing: Naïve String Matching – CO1, CO2, CO4
# Problem Statement:
# Given:
# ● A text string text of length n.
# ● A pattern string pattern of length m.
# Objective:
# Find all starting indices i in the text such that the substring text[i : i + m] is exactly equal to
# the pattern using the Naïve String Matching Algorithm approach.
# Constraints:
# ● l 0 ≤ m ≤ n
# ● Characters in text and pattern can be any valid characters (e.g., a–z, A–Z, digits, etc.)
# Theory:
# The Naïve String Matching Algorithm is the most basic method for pattern searching within
# a text.
# It works by checking for the occurrence of the pattern starting from each position of the text
# one by one.
# Working Principle:
# 1. Compare the pattern with a substring of the text starting at position i.
# 2. If all characters match, record index i as a match position.
# 3. Otherwise, shift the pattern by one position and repeat.
# 4. Continue until the end of the text is reached.
# Example:
# Text: AABAACAADAABAABA
# Pattern: AABA
# Matches found at indices: 0, 9, 12

# Algorithm:
# NAIVE_STRING_MATCH(text, pattern):
#  n = length(text)
#  m = length(pattern)
#  for i from 0 to n - m:
#  j = 0
#  while j < m and text[i + j] == pattern[j]:
#  j = j + 1
#  if j == m:
#  print("Pattern found at index", i)


# Experiment 09:String Processing: Naïve String Matching
# Python Program:
# def naiveStringMatch(text, pattern):
#  n = len(text)
#  m = len(pattern)
#  print(f"Text: {text}")
#  print(f"Pattern: {pattern}")
#  print("Pattern found at indices:", end=" ")
#  for i in range(n - m + 1):
#  match = True
#  for j in range(m):
#  if text[i + j] != pattern[j]:
#  match = False
#  break
#  if match:
#  print(i, end=" ")
# # Driver Code
# if __name__ == "__main__":
#  text = "AABAACAADAABAABA"
#  pattern = "AABA"
#  naiveStringMatch(text, pattern)
# Output:
# Text: AABAACAADAABAABA
# Pattern: AABA
# Pattern found at indices: 0 9 12