class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NewList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
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
        print("1: Append")
        print("2: Delete")
        print("3: Show data")
        print("4: Search")
        print("5: Replace")
        print("0: Exit")

        user_choice = input("(1-0): ")

        if user_choice == '1':
            value = int(input("Write num to append: "))
            list1.append(value)
        elif user_choice == "2":
            value = int(input("Write num to delete: "))
            list1.delete(value)
        elif user_choice == "3":
            print("List: ")
            list1.display()
        elif user_choice == "4":
            value = int(input("Write num for search: "))
            if list1.search(value):
                print("Found")
            else:
                print("Not found")
        elif user_choice == "5":
            value1 = int(input("Write num to replace: "))
            value2 = int(input("Write new num: "))
            list1.replace(value1, value2)
        elif user_choice == "0":
            break;

if __name__ == '__main__':
    main()





