class ObjectAssignment:
    def __init__(self, num):
        self.val = num

if __name__ == '__main__':
    a = ObjectAssignment(2)
    b = ObjectAssignment(None)
    c = ObjectAssignment(None)

    b = a
    print b.val
    a = c
    print (b.val)