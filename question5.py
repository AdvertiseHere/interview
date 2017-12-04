'''
Question 5
Find the element in a singly linked list that's m elements from the end. For example, if
a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function
 definition should look like question5(ll, m), where ll is the first node of a linked list
 and m is the "mth number from the end". You should copy/paste the Node class below to use
 as a representation of a node in the linked list. Return the value of the node at that
 position.
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def question5(self, m):
        p1 = self.head
        p2 = self.head

        # Starts at the first element of the linked list, continues
        for i in range(m):
            if (p1 == None):
                return None
            p1 = p1.next
        while (p1 != None):
            p1 = p1.next
            p2 = p2.next

        return p2.data



ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)

def main():

    print LinkedList.question5(ll, 1)

if __name__ == "__main__":
    main()