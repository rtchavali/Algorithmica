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

    def search(self, node_data):
        current = self.head
        node_point = 1
        while current is not None:
            if current.data == node_data:
                print  'Element found at %s' % (node_point)
                break
            else :
                current = current.next
                node_point+=1
# below function need to be modified .. it is replacing , it should insert
    def insert_arbitratry(self, position, new):
        previous = current = self.head
        new = Node(new, next)
        while position is not 0:
            current=current.next
            previous=previous.next
            position-=1
            print position, previous, current
            previous.next=new.next
        new.next= current.next


s=Linked_list()
s.append(31)
s.append(2)
s.append(23)
s.insert_arbitratry(2, 12)
s.append(25)
s.show_elements()
s.remove(23)
s.append(55)
s.show_elements()
s.search(55)
