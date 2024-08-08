n_t = int(input())
inp = []

for i in range(n_t):
    inp.append(list(input()))


for num in inp:
    print(int(num[0]) + int(num[1]))