import math
import decimal

X = input()
ans = math.ceil(decimal.Decimal(X) / decimal.Decimal("10.0"))
print(ans)
