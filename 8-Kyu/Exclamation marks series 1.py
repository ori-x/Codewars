"""
Description:
Remove all exclamation marks from the end of sentence.

Examples
remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi! Hi"
remove("Hi") === "Hi"
"""

 def remove(s):
    return s[:-1] if len(s) > 0 and s[-1] == "!" else s

# When compared to other 8 Kyu, this one is in no way on the same level.
# Easy for beginners like me to fail the code on an index error if not careful. 