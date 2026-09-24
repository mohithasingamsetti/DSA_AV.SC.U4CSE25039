class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        print(f"Front element (peek): {self.queue[self.front]}")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty:")
            return
        print("Queue elements:", end =" ")
        for i in range(self.size):
            idx = (self.front + i) % self.capacity
            print(self.queue[idx], end = " ")
        print()


def menu_array_queue():
    q = ArrayQueue()
    while True:
        print("\n--- Array-Based Queue Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            val = input("Enter value to enqueue:")
            q.enqueue(val)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.peek()
        elif choice == '4':
            q.display()
        elif choice == '5':
            print("Exiting array-based queue.")
            break
        else:
            print("Invalid choice! Try again.")

def main():
    while True:
        print("\n=== Queue Implementation Menu ===")
        print("1. Use Array-Based Queue")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            menu_array_queue()
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
      



