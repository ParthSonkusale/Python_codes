def solve(s):
    s_1 = ""

    for i in range(len(s)):
        s_1 += s[(len(s) - 1) - i]
        
    if s == s_1:
        return "OK"

    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]
        rev = ""

        for j in range(len(new_s)):
            rev += new_s[(len(new_s) - 1) - j]
            
        if new_s == rev:
            return "remove one"

    return "not possible"