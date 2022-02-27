N = int(input())
members = []
for _ in range(N):
	a, b = int(input()), int(input())
	score = 5 * a - 3 * b
	members.append(score)
c = 0
for m in members:
	if m > 40:
		c += 1
print(f"{c}{'+' if len(members) == c else ''}")
