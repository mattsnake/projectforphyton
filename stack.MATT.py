#MATT ANDREW F. SOLATAN
#CPE PETITION

class Stack:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5, 6]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    x = 0
    while x <= 100:
        s.push(x)
        print s.peek()
        x += 1

    print "last element =", s.peek()
    print "size is = ", s.size()


# s = [1, 2, 3, 4, 5, 6]
# t = [1, 2, 3, 4, 5]
