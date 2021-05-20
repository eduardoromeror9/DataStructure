"""from node import Node

head = None
for count in range(1,6):
    head = Node(count, head)
    
while head != None:  
    print(head.data) # Imprime loop infinito porque head no va a ningun lado
    head = head.next
    
probe = head
while probe != None:
    print(probe.data)
    probe = probe.next
    
probe = head
target_item = head
target_item = 2
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    print(f'Target item {target_item} has been found!!')
else:
    print(f'Target item {target_item} is not in the list!!')"""
    
    
# from node import Node
# index = 1
# new_item = 'ham'
# head = Node(None, None) 
# head.next = head       
# probe = head
# while index > 0 and probe.next != head:
#     probe = probe.next
#     index -= 1
 
# probe.next = Node(new_item, probe.next) 
# print(probe.next.data)

"""from double_linked_list import Node, TwoWayNode
head = TwoWayNode(1)
tail = head
for data in range(2,6):
    tail.next = TwoWayNode(data, tail)
    tail = tail.next

probe = tail

while probe != None:
    print(probe.data)
    probe = probe.previous"""
    

from stack import Stack

food = Stack()

food.push('egg')
food.push('ham')
food.push('spam')

food.pop()
food.peek()