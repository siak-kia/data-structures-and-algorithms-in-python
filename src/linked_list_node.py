class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    def traverse(self, head):
        #node = head
        while head:
            print ("node_value: ", head.val)
            head = head.next
        return None

    def copy(self, head):
        result = []
        while head:
            node = Node(head.val)
            result.append(node)
            head = head.next
        for i in range(len(result) -1, 0, -1):
            result[i-1].next = result[i]
        return result[0]

if __name__ == '__main__':
     linkedList = LinkedList()
     node1 = Node(5)
     node2 = Node(2)
     node3 = Node(3)
     ## 5 - > 2 -- > 3
     node1.next = node2
     node2.next = node3

     linkedList.traverse(node1)
     new_node = linkedList.copy(node1)
     linkedList.traverse(new_node)
