class Myhash:
    def __init__(self,b):
        self.Bucket=b
        self.table=[[]for x in range(b)]
    def insert(self,x):
        i=x%self.Bucket
        self.table[i].append(x)
    def remove(self,x):
        i=x%self.Bucket
        self.table[i].remove(x)
    def search(self,x):
        i=x%self.Bucket
        return x in self.table[i]
    
hash=Myhash(7)
hash.insert(10)
print(hash.search(20))