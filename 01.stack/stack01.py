print("Let's start the stack01.py program!")
capacity = 5
my_list = [None] * capacity

top = -1

def isEmpty() :
  if top == -1 :
    return True
  else :
    return False
  
def isFull() :
  if top == capacity - 1 :
    return True
  else :
    return False

def pop() :
  global top
  if isEmpty() :
    print("Stack is empty")
    return
  data = my_list[top]
  my_list[top] = None
  top -= 1
  return data

def push(data) :
  global top
  if isFull() :
    print("Stack is full")
    return
  
  top += 1
  my_list[top] = data
  
  return data

def peek() :
  if isEmpty() :
    print("Stack is empty")
    return
  return my_list[top]
   
def size() :
  return top + 1

print(push(34))
print(push(35))
print(push(37))
print(push(38))
print(push(38))
print(push(38))
print(push(38))
print(push(38))
print(pop())
print(pop())
print(pop())
print(my_list)