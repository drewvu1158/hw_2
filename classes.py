class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Contact_list:
    def __init__(self, head):
        self.head = head

    def add(self, name, number):
        new_node = node(contact(name, number))
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        string = self.head
        while string:
            print(string.data.name, string.data.phone)
            string = string.next
        return ""

    def remove_name(self, name):
        current = self.head
        while current is not None:
            if current.data.name == name:
                current.data.name = None
            else:
                if current.data == None:
                    print("Name not found")
                else:
                    self.head = current.next
            current = current.next

    def remove_number(self, name, number):
        current = self.head
        while current is not None:
            if current.data.name == name:
                if current.data.phone == number:
                    current.data.phone == None
                else:
                    if current.data == None:
                        print("Number not found")
                    self.head = current.next
            current = current.next
