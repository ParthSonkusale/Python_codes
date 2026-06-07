#st = "aaB"
#st_f = ""

#for i in range(len(st)):
#    st_f += st[i]

#    if len(st_f) == len(st):
#        for i in range(len(st)):
#            st_f += st[(len(st) - 1) - i]

#        for i in range(len(st)):
#            if st[i] != st_f[(len(st) - 1) + i]:
#                st_f = st_f[:((len(st) - 1) + i)] + st_f[((len(st) - 1) + i + 1):]
#            elif st[i] == st_f[(len(st) - 1) + i]:
#                if st[len(st) - 1] == st_f[(len(st) - 1) + i]:
#                    st_f = st_f[:((len(st) - 1) + i)] + st_f[((len(st) - 1) + i + 1):]                             
#            else:
#                print(st_f)
#                
           # if st_f[len(st_f) - 1] == st[0]:
def complete(st):
    for i in range(1, len(st)):
        suffix = st[i:]

        if suffix == suffix[::-1]: # short trick to reverse the string
            return st + st[:i][::-1]

    return st + st[:-1][::-1]

   