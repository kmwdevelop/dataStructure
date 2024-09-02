print("Let's start the stack01.py program!")
capacity = 5
my_list = [None] * capacity

top = -1

def pop() :
  global top
  if top == -1 :
    print("Stack is empty")
    return
  data = my_list[top]
  my_list[top] = None
  top -= 1
  return data

def push(data) :
  global top
  if top == len(my_list) -1 :
    print("Stack is full")
    return
  
  top += 1
  my_list[top] = data
  
  return data
   
print(push(34))
print(push(35))
print(push(37))
print(push(38))
print(pop())
print(pop())
print(pop())
print(my_list)