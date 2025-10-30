# Problem: B - Mihret and Chess - https://codeforces.com/gym/604781/problem/B

r1, c1, r2, c2 = map(int, input().split())

# Rook
rook = 1 if (r1 == r2 or c1 == c2) else 2

# Bishop
if (r1 + c1) % 2 != (r2 + c2) % 2:
    bishop = 0
elif abs(r1 - r2) == abs(c1 - c2):
    bishop = 1
else:
    bishop = 2

# King
king = max(abs(r1 - r2), abs(c1 - c2))

print(rook, bishop, king)
