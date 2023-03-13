l = [10, -15, -2, 1]
ls = sorted(l, key=abs, reverse=True)
print(ls)


t = (10, 12, 15, 5)
print(sorted(t))

s = {10, 12, 15, 5}
print(sorted(s))

dict = {20: "a", 15: "b", 10: "c", 5: "d"}
print(sorted(dict))

n = [(10, 15), (1, 8), (2, 7)]
print(sorted(n))
