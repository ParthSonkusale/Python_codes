s = "abcabcbb"
s_copy = []

max_len = 0

for ch in s:
    if ch in s_copy:
        index = s_copy.index(ch)
        s_copy = s_copy[index + 1:]
    s_copy.append(ch)
    
    if len(s_copy) > max_len:
        max_len = len(s_copy)
    
print(max_len)    