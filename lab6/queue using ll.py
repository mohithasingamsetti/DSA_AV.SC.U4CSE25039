class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:  # queue became empty
            self.rear = None
        self.size -= 1
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        print(f"Front element (peek): {self.front.data}")
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Queue elements:", end=" ")
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()



def menu_linked_queue():
    q = LinkedQueue()
    while True:
        print("\n--- Linked List-Based Queue Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            val = input("Enter value to enqueue: ")
            q.enqueue(val)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.peek()
        elif choice == '4':
            q.display()
        elif choice == '5':
            print("Exiting linked list-based queue.")
            break
        else:
            print("Invalid choice! Try again.")


def main():
    while True:
        print("\n=== Queue Implementation Menu ===")
        print("1. Use Linked List-Based Queue")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            menu_linked_queue()
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

