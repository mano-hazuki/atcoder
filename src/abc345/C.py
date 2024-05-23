S = input()
chars = set()
counts = dict()
ans = 0
counted_first = False
for s in S:
    chars.add(s)
    counts.setdefault(s, 0)
    counts[s] += 1
for i in range(0, len(chars)):
    combs = 0
    if counts[list(chars)[i]] > 1 and not counted_first:
        combs += 1
        counted_first = True
    if i != len(chars) - 1:
        for j in range(i + 1, len(chars)):
            combs += counts[list(chars)[i]] * counts[list(chars)[j]]
    ans += combs
print(ans)
