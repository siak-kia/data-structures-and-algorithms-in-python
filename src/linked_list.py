class LinkedList:
    def __init__(self):
        self.value = None
        self.next = None

    def __init__(self, value):
        self.value = value
        self.next = None

    def print_linked_list(self):
        x = self
        while x is not None:
            print (x.value)
            x = x.next

    def reverse_linked_list(self, head):
        if head.next is None:
            return head
        else:
            head = self.reverse_linked_list(head.next)
            self.next.next = self
            self.next = None
            return head
    def reverseList(self, head):
        prev = LinkedList(head.value, head)
        current = LinkedList(head.value, head.next)

        if head.next is not None:
            nextNode = head.next.next
        while current is not None:
            current.next = prev
            prev = current
            current = nextNode
            if nextNode is not None:
                nextNode = nextNode.next
        return prev

if __name__ == '__main__':
       node1 =  LinkedList(1)
       node2 =  LinkedList(2)
       node3 = LinkedList(3)
       node1.next = node2
       node2.next = node3
       node1.reverseList(node1)
       node1.print_linked_list()
# class MyClass():
#     def __init__(self, value):
#         self.x =  value
# if __name__ == '__main__':
#     X = MyClass(2)
#     Y = X
#     print ("X.x = ", X.x)
#     Y.x = 3
#     print ("Y.x = ", Y.x)
#     print ("X.x = ", X.x)

def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    nums.sort()
    frequency_dict = {}
    frequency = 0
    result = []
    for j in range(0, len(nums) -1):
        if nums[j] == nums[j+1]:
            frequency += 1
        else:
            frequency_dict[nums[j]] = frequency
            frequency = 0
    for h, v in frequency_dict.items():
        if v == k:
            result.append(h)
    return result
                