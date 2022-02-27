X = int(input())
must = [input().split() for _ in range(X)]
Y = int(input())
mustnot = [input().split() for _ in range(Y)]
G = int(input())
groups = [input().split() for _ in range(G)]
count = 0
violatedmust, violatedmustnot = [], []
for group in groups:
	for m in must:
		if (m[0] not in group and m[1] in group or m[0] in group and m[1] not in group) and m not in violatedmust:
			count += 1
			violatedmust.append(m)
	for m in mustnot:
		if (m[0] in group and m[1] in group) and m not in violatedmustnot:
			count += 1
			violatedmustnot.append(m)
print(count)
