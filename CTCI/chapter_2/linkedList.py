#!/usr/bin/env python3

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def prependNode(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new
        self.size += 1

    def appendNode(self,val):
        new = Node(val)
        node = self.head
        if node:
            while (node.next != None):
                node = node.next
            node.next = new
            self.size += 1
        else:
            self.head = new
            self.size += 1

    def printList(self):
        list = ''
        node = self.head
        while node:
            list += str(node.val)
            if (node.next != None):
                list += ' - '
            node = node.next
        print(list)

    def getValueAtPosition(self, position):
        node = self.head
        count = 0

        if (position < 0):
            raise ValueError("Position must be between 0 and size of list.")

        try:
            while(count < position):
                node = node.next
                count += 1
            return node.val
        except:
            raise ValueError("Position must be between 0 and size of list.")


print("\nCreating a linked list...\n")
LL = LinkedList()
LL.prependNode(1)
LL.prependNode(2)
LL.prependNode(5)

## 5 - 2 - 1

LL.appendNode(3)

## 5 - 2 - 1 - 3

LL.printList()

print("\nSize of linked list is: ", LL.getSize())

position = 2
print("\nValue at position %s: %i \n(head is position 0)\n" % (position, LL.getValueAtPosition(position)))
