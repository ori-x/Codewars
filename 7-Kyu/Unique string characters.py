def solve(a,b):
    c = ""
    for char in a:
         if char not in b:
             c += char
    for charb in b:
         if charb not in a:
             c += charb

    return c
