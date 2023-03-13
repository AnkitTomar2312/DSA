# List
l1 = [10, 5, 15, 1, 80, 72]
l1.sort()
print(l1)

l2 = [10, 5, 15, 1, 80, 72]
l2.sort(reverse=True)
print(l2)

l3 = ['gfg', 'courses', 'development']
l3.sort()
print(l3)


# Sorting user defined using key-fun
def Mykey(l4):
    return len(l4)


l4 = ['gfg', 'courses', 'development']
l4.sort(key=Mykey)
print(l4)

l5 = ['gfg', 'courses', 'development']
l5.sort(key=Mykey, reverse=True)
print(l5)

# Sorting user defined object {used in natural order}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def myFun(p):
    return p.x


l = [Point(1, 3), Point(4, 10), Point(8, 9)]
l.sort(key=myFun)
for i in l:
    print(i.x, i.y)


# Sorting user defined using __lt__ 2  => less then method
# another method is aslo existed called equal to order

print("Sorting user defined using __lt__ 2 \n")


class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x


l = [Point1(1, 3), Point1(4, 10), Point1(8, 9)]
l.sort()
for i in l:
    print(i.x, i.y)
print('\n\n')

# one more program usig the __lt__ method:


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x


l = [Point2(1, 8), Point2(1, 2), Point2(0, 9), Point2(0, 5)]
l.sort()
for i in l:
    print(i.x, i.y)
