class Node(object):
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
class Linked_list(object):
    def __init__(self, head=None, tail=None):
        self.head=head
        self.tail=tail

    def show_elements(self):
        print 'showing list elements'
        current = self.head
        while current is not None:
            print current.data, "-->",
            current = current.next
        print None

    def append(self, data):
        next = Node(data, None)
        if self.head == None:
            self.head=self.tail=next
        else:
            self.tail.next = next
        self.tail=next

    def remove(self, next_value):
        current=self.head
        previous = None
        while current is not None:
            if current.data== next_value:
                if previous is not None:
                    previous.next = current.next
                else :
                    self.head=current.next
            previous = current
            current = current.next
s=Linked_list()
#s.remove(1)
s.append(31)
s.append(2)
s.append(23)
s.append(25)
s.show_elements()
s.remove(23)
s.append(55)
s.show_elements()
