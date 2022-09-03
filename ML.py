class Node:
    def __init__(self,data, link=None):
        self.data = data
        self.link = link

class MyList:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.length = 0
        for arg in args:
            self.append(arg)

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.link = node
            self.tail = node
        self.length += 1
    def __iter__(self):
        def genIter():
            curr = self.head
            while curr is not None:
                yield curr.data
                curr = curr.link
        return genIter()

    def __len__(self):
        return self.length

    def __str__(self):
        s = "<"
        for idx, data in enumerate(self):
            s+=str(data)
            if idx  < len(self)-1:
                s += ", "
            else:
                s += ">"
        return s
    def __getitem__(self, item):
        if type(item) is not int:
            raise TypeError("정수를 입력해줘요")
        if item < 0:
            item = len(self) + item
        if item>= len(self) or item < 0:
            for idx, data in enumerate(self):
                if idx == item:
                    return data

    def __setitem__(self, key, value):
        if type(key) is not int:
            raise TypeError("인덱스는 정수여야해여")
        if key < 0:
            item = len(self) + key
        if key >= len(self) or key < 0:
            raise IndexError("Index out of range")
        curr = self.head
        for i in range(key):
            curr=curr.link
        curr.data = value
mylist = MyList(1, 2, 3, 4)

mylist[3] = 5
print(mylist)
