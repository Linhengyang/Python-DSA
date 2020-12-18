# input_str = str(input())

# class Stack():
#     def __init__(self):
#         self.__items = []
#     def push(self, item):
#         self.__items.append(item)
#     def pop(self):
#         return self.__items.pop()
#     def peek(self):
#         return self.__items[-1]
#     def size(self):
#         return len(self.__items)
#     def isEmpty(self):
#         return self.__items == []
# def bracketsMatch(brackestStr):
#     brackets = list(brackestStr)
#     s = Stack()
#     for char in brackets:
#         if char in "([{":
#             s.push(char)
#         else:
#             if (not s.isEmpty()) and "([{".index(s.pop()) == ")]}".index(char):
#                 continue
#             else:
#                 return False
#     if s.isEmpty():
#         return True
#     else:
#         return False
# print(bracketsMatch(input_str))

# input_str = input()
# class Stack():
#     def __init__(self):
#         self.items = []
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def peek(self):
#         return self.items[-1]
#     def size(self):
#         return len(self.items)
#     def isEmpty(self):
#         return self.items == []

# def xiaoxiaole(input_str):
#     chars =  list(input_str)
#     s = Stack()
#     s.push(chars[0])
#     for char in chars[1:]:
#         if (not s.isEmpty()) and s.peek() == char:
#             s.pop()
#         else:
#             s.push(char)
#     if s.isEmpty():
#         return None
#     else:
#         return "".join(s.items) 

# print(xiaoxiaole(input_str))

# 第三题应该改成：设小明没有作弊的前提下，顾客的盘子的顺序是可以出现的，那么就输出Yes；不然就输出No
input_str = input()
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

def jiancha(input_str):
    numbs = [int(i) for i in list(input_str)]
    heap = Stack()
    bosshave = []
    # Add the first value to bosshave
    # bosshave.append(numbs[0])
    Good = True
    for i in range(numbs[0]):
        heap.push(i)
    for j in range(1,len(numbs)): # 第二个顾客拿到的盘子是numb
        if not heap.isEmpty() and numbs[j] == heap.peek(): #heap是前一个盘子拿到时，盘堆的状态
            heap.pop()
            # bosshave.append(numbs[j])
        elif not heap.isEmpty() and numbs[j] < heap.peek():
            Good = False
            break
        elif not heap.isEmpty() and numbs[j] > heap.peek():
            for i in range(numbs[j]):
                if i not in heap.items and i not in numbs[:j]:
                    heap.push(i)
        else: # now heap is empty
            # numbs[:j] 是0到j-1的一个排列
            for i in range(j, numbs[j]):
                heap.push(i)
    if Good:
        return "Yes"
    else:
        return "No"
print(jiancha(input_str))