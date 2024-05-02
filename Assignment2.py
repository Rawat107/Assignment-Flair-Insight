class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepand(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node 
            self.tail = self.head
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        
    def insert(self, position, data):
        if position >= self.length:
            if position > self.length:
                print("Position not available, Inserting at the end of the list.")

            self.append(data)
        elif position == 0:
            self.prepand(data)
        
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position -1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
    
    def delete_by_position(self, position):
        if self.head == None:
            print("Linked list is empty. Nothing to delete.")
            return
        
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        
        if position >= self.length:
            position = self.length - 1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node

        return
    
    def delete_by_value(self, data):
        if self.head == None:
            print("Linked list is empty. Nothing to delete.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
    
        while current_node.next != None and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next != None:
            current_node.next = current_node.next.next
            if current_node.next == None:
                self.tail = current_node
            self.length -= 1
            return

        else:
            print("Given value not found.")
        
    def print(self):
        if self.head == None:
            print("Empty")
        else:
            current = self.head
            while current:
                print(current.data, end= "->")
                current = current.next
        print()

    def reverse(self):
        prev = None
        current_node = self.head
        while current_node:
            new_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = new_node
        self.head = prev

    def middle_ele(self):
        mid = self.length // 2

        current_head = self.head
        for i in range(mid):
            current_head = current_head.next

        
        return current_head.data
        

    def merge_sorted_list(self, l1, l2):
        merge_list = LinkedList()

        p1 = l1.head
        p2 = l2.head

        while p1 is not None and p2 is not None:
            if p1.data < p2.data:
                merge_list.append(p1.data)
                p1 = p1.next
            else:
                merge_list.append(p2.data)
                p2 = p2.next

        while p1 is not None:
            merge_list.append(p1.data)
            p1 = p1.next    
           
        while p2 is not None:
            merge_list.append(p2.data)
            p2 = p2.next

        merge_list.head = merge_list.head
        merge_list.tail = merge_list.tail
        return merge_list
    
if __name__ == '__main__':
    # my_linked_list = LinkedList()
    # my_linked_list.print()

    # my_linked_list.append(10)
    # my_linked_list.append(5)
    # my_linked_list.print()

    # my_linked_list.prepand(11)
    # my_linked_list.print()

    # my_linked_list.insert(2, 12)
    # my_linked_list.insert(6, 222)

    # my_linked_list.print()
    # my_linked_list.reverse()
    # my_linked_list.print()
    # my_linked_list.delete_by_value(11)
    # my_linked_list.delete_by_position(0)
    # my_linked_list.print()
    # middle_element = my_linked_list.middle_ele()
    # print("Middle element:", middle_element)
    
    l1 = LinkedList()
    l1.append(10)
    l1.append(11)
    l2 = LinkedList()
    l2.append(2)
    l2.append(34)

    l3 = LinkedList()
    merger_list = l3.merge_sorted_list(l1, l2)
    merger_list.print()

    