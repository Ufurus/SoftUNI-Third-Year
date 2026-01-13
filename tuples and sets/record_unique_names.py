n = int(input())
names = set({})
for _ in range(n):
    given_names = input()
    names.add(given_names)

for name in names:
    print(name)