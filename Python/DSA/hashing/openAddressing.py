class OpenAddressing:
    def __init__(self,b):
        self.Bucket=b
        self.Table=[[] for x in range(b)]