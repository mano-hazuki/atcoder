S = input()
removing = False
for s in S:
    if s == "|":
        removing = not removing
        continue
    if not removing:
        print(s, end="")
