class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter number of elements: "))

        for i in range(n):
            data = int(input("Enter data: "))
            new = Node(data)

            if self.head is None:
                self.head = new
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def insert_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_begin(data)
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        new = Node(data)
        new.next = temp.next
        temp.next = new

    def delete_value(self, data):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found")

    def delete_first(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    def count(self):
        count = 0
        temp = self.head

        while temp:
            count = count + 1
            temp = temp.next

        print("Number of nodes:", count)

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


l = LinkedList()

l.create()
print("Linked list:", end=" ")
l.display()

data = int(input("Enter data to insert at beginning: "))
l.insert_begin(data)
print("After insertion:", end=" ")
l.display()

data = int(input("Enter data to insert at end: "))
l.insert_end(data)
print("After insertion:", end=" ")
l.display()

index = int(input("Enter index: "))
data = int(input("Enter data: "))
l.insert_index(index, data)
print("After insertion:", end=" ")
l.display()

data = int(input("Enter value to delete: "))
l.delete_value(data)
print("After deletion:", end=" ")
l.display()

l.delete_first()
print("After deleting first node:", end=" ")
l.display()

l.delete_last()
print("After deleting last node:", end=" ")
l.display()

l.count()
