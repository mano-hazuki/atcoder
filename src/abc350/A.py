S = input()
number = int(S.replace("ABC", ""))
print("No" if number == 316 or number < 1 or number > 349 else "Yes")
