class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create linked list
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
                new.prev = temp

    # 2. Insert at beginning
    def insert_begin(self, data):
        new = Node(data)

        new.next = self.head

        if self.head is not None:
            self.head.prev = new

        self.head = new

    # 3. Insert at end
    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new
            new.prev = temp

    # 4. Insert at specific index
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
        new.prev = temp

        if temp.next is not None:
            temp.next.prev = new

        temp.next = new

    # 5. Delete by value
    def delete_value(self, data):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head

        while temp:
            if temp.data == data:

                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next is not None:
                    temp.next.prev = temp.prev

                return

            temp = temp.next

        print("Value not found")

    # 6. Delete first node
    def delete_first(self):
        if self.head is None:
            print("Linked list is empty")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    # 7. Delete last node
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        if temp.prev is None:
            self.head = None
        else:
            temp.prev.next = None

    # 8. Count number of nodes
    def count(self):
        count = 0
        temp = self.head

        while temp:
            count = count + 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


l = DoublyLinkedList()

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
