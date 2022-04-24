#!/usr/bin/env python3

''' Class Template for a singly linked list Head -> Tail convention
Exercise Part starts at line 40 '''

# class for holding the data, defaults to empty node if no data is given
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # pointer to the next node

# Class for managing the list and nodes
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1  # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size


    '''
    Exercise Part 1,2 and 3:
    Implement the given methods below according to the requirements in the exercise sheet.
    return the correct data types and values
    '''

    def clear(self):
        while self.head:
            temp = self.head
            self.head = self.head.next
            temp = None

    def get_data(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def delete(self, data):
        temp = self.head  # store head node

        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next

        temp = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

llist = SinglyLinkedList()

llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.delete(2)
print(llist.get_data(1))
# llist.clear()

llist.print_list()


'''Exercise Part 4: Copy the code from the singly linked list implementation and rewrite it
to implement a doubly linked list according to the exercise sheet. Don't forget to change the names of the classes
in the code to reflect the new class name (NodeDLL instead of Node).
'''

class NodeDLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if self.head is None:  # if head is empty ...
            new_node = NodeDLL(data)
            new_node.prev = None
            self.head = new_node
        else:  # if head is not empty, how to append at the end of the list?
            new_node = NodeDLL(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None
        self.size += 1

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data and current == self.head:
                if not current.next:
                    current = None
                    self.head = None
                    return

                # if we want to remove the head node and there is a node following it
                else:  # if current.next is pointing to a valid node.
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return

            # if we want to remove a node from the middle
            elif current.data == data:
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return

                # if we want to remove the last node of the list
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next

    def clear(self):
        while self.head:
            temp = self.head
            self.head = self.head.next
            temp = None

    def get_data(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

dllist = DoublyLinkedList()

dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.delete(4)

dllist.print_list()



'''Exercise Part 5 and 6:
Complete the classes below to implement a stack and queue data structure. You are free to use built-in
methods but you have to complete all methods below. Always return the correct data type according
to the exercise sheet'''


class MyStack():
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def top(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def get_stack(self):
        return self.elements

s = MyStack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
print(s.pop())
print(s.get_stack())
print(s.top())
print(s.size())


class MyQueue:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop(0)

    def show_left(self):
        return self.elements[0]

    def show_right(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def get_queue(self):
        return self.elements

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(9)
print(q.show_right())
print(q.show_left())
print(q.pop())
print(q.get_queue())
