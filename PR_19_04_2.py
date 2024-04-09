class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class NewList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def delete(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                if current_node == self.head:
                    self.head = current_node.next
                current_node = None
                return
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def replace(self, old_data, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == old_data:
                current_node.data = new_data
                return
            current_node = current_node.next

def main():
    list1 = NewList()

    while True:
        print("1: Append str: ")
        print("2: Delete str: ")
        print("3: :ist: ")
        print("4: Search str: ")
        print("5: REplace str: ")
        print("0: Exit")

        user_choice = input("(1-0): ")

        if user_choice == '1':
            value = input("Write str to append: ")
            list1.append(value)
        elif user_choice == '2':
            value = input("Write str to delete: ")
            list1.delete(value)
        elif user_choice == '3':
            print("List: ")
            list1.display()
        elif user_choice == '4':
            value = input("Write str for search: ")
            if list1.search(value):
                print("Found")
            else:
                print("Not found")
        elif user_choice == '5':
            old_value = input("Write str to replace: ")
            new_value = input("Write new str: ")
            list1.replace(old_value, new_value)
        elif user_choice == '0':
            break;

if __name__ == "__main__":
    main()