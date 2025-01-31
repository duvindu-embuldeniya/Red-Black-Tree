# class InvalidNameException(Exception):
#     def __init__(self,msg):
#         super(InvalidNameException, self).__init__()
#         self.msg = msg

# class InvalidAgeException(Exception):
#     def __init__(self,msg):
#         super(InvalidAgeException, self).__init__()
#         self.msg = msg

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     @staticmethod
#     def func(name,age):
#         if name == None:
#             raise InvalidNameException("name 404")

#         if age < 0:
#             raise InvalidAgeException("age 405")
        
#         return Person(name, age)

# try:
#     obj = Person.func("duvindu", -22)
#     print(obj)

# except Exception as ex:
#     print(ex.msg)



# subject_dic = {}
# student_dic = {}

# def func1(subject, values):
#     h_name = None
#     h_marks = 0
#     for name, marks in values.items():
#         if marks > h_marks:
#             h_name = name
#             h_marks = marks
#     return subject, h_name, h_marks

# def keyFunc(tple):
#     return tple[1]

# with open('./marks.txt', 'r') as fr:
#     text = fr.readlines()
#     length = len(text)
#     for i in range(1,length):
#         line = text[i]
#         data = line.split(',')
#         name = str(data[0].strip())
#         subject = str(data[1].strip())
#         marks = int(data[2].strip())

#         if subject not in subject_dic:
#             subject_dic[subject] = {}
#         subject_dic[subject][name] = marks

#         previous_marks = student_dic.get(name, 0)
#         marks += previous_marks
#         student_dic[name] = marks


# for subject, values in subject_dic.items():
#     subject, h_name, h_marks = func1(subject, values) 
    
# lst = [item for item in student_dic.items()]
# lst.sort(key = keyFunc, reverse=True)
# print(lst)






# class Fib:
#     a = None
#     b = None
#     def __init__(self, val1, val2):
#         self.a = val1
#         self.b = val2
#         self.count = 0
    
#     def cycle(self):
#         while self.count < 10:
#             c = self.a + self.b
#             yield self.a
#             self.a, self.b  = self.b, c
#             self.count += 1

# fib = Fib(0,1)
# result = fib.cycle()

# while True:
#     try:
#         print(next(result))
#         continue

#     except Exception as ex:
#         print(ex, type(ex))
#         break

# print(f"Outside")





# # emp_dic = {}
# salary_dic = {}

# # def empFunc(employee, values):
# #     name = employee
# #     just_month = None
# #     highest_salary = 0
# #     for month, salary in values.items():
# #         if salary > highest_salary:
# #             highest_salary = salary
# #             just_month = month
# #     return name, just_month, salary

# def descOrder(values):
#     return values[1]

# with open('./employees.txt', 'r') as fr:
#     data = fr.readlines()
#     for i in range(1, len(data)):
#         line = data[i].split(',')
#         name = str(line[0].strip())
#         month = str(line[1].strip())
#         salary = int(line[2].strip())

#         # if name not in emp_dic:
#         #     emp_dic[name] = {}
#         # emp_dic[name][month] = salary

#         previous = salary_dic.get(name, 0)
#         salary_dic[name] = previous + salary


# # for employee, values in emp_dic.items():
#     # employee, month, salary = empFunc(employee, values)
# # print(f"In {month} highest salary which was {salary}/= was earned by {employee}")

# # sorted_lst = [(name,salary) for name, 
# #               salary in salary_dic.items()]
# # sorted_lst.sort(key=descOrder)
# # print(sorted_lst)


# print(salary_dic)




# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Sll:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.bucket = []

#     def creation(self):
#         current_node = self.head
#         while current_node:
#             self.bucket.append(current_node.value)
#             current_node = current_node.next
    
#     def travel(self):
#         if self.head == None:
#             print("Empty")
#         else:
#             node = self.head
#             while node:
#                 print(node.value)
#                 node = node.next
#                 continue

# node1 = Node(4)
# node2 = Node(5)
# node3 = Node(6)

# linkedList = Sll()

# linkedList.head = node1
# node1.next = node2
# node2.next = node3
# linkedList.tail = node3

# linkedList.creation()
# # print(linkedList.bucket)

# linkedList.travel()



salary_dic = {}

with open('./employes.txt', 'r') as fr:
    data = fr.readlines()
    for i in range(1, len(data)):
        line = data[i].split(',')
        name = str(line[0].strip())
        month = str(line[1].strip())
        salary = int(line[2].strip())

        previous = salary_dic.get(name, 0)
        salary_dic[name] = previous + salary


class Node:
    def __init__(self, key, color="red"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        if not self.root:
            self.root = node
            self.root.color = "black"
            return

        curr = self.root
        parent = None
        while curr:
            parent = curr
            curr = curr.left if key < curr.key else curr.right

        if key < parent.key:
            parent.left = node
        else:
            parent.right = node
        node.parent = parent

        self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_left(node.parent.parent)
        self.root.color = "black"

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def delete(self, key):
        node = self._find_node(key)
        if not node:
            return

        y = node
        y_original_color = y.color

        if not node.left:
            x = node.right
            self._transplant(node, node.right)
        elif not node.right:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == "black":
            self._fix_delete(x)

    def _find_node(self, key):
        curr = self.root
        while curr and curr.key != key:
            curr = curr.left if key < curr.key else curr.right
        return curr

    def _minimum(self, node):
        while node.left:
            node = node.left
        return node

    def _transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def _fix_delete(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self._rotate_left(x.parent)
                    w = x.parent.right
                if (w.left and w.left.color == "black" and w.right and w.right.color == "black") or (not w.left and not w.right):
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right is None or w.right.color == "black":
                        if w.left:
                            w.left.color = "black"
                        w.color = "red"
                        self._rotate_right(w)
                        w = x.parent.right
                    if w.right:
                        w.color = x.parent.color
                        x.parent.color = "black"
                        w.right.color = "black"
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self._rotate_right(x.parent)
                    w = x.parent.left
                if (w.left is not None and w.left.color == "black" and w.right is not None and w.right.color == "black") or (not w.left and not w.right):
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left is None or w.left.color == "black":
                        if w.right:
                            w.right.color = "black"
                        w.color = "red"
                        self._rotate_left(w)
                        w = x.parent.left
                    if w.left:
                        w.color = x.parent.color
                        x.parent.color = "black"
                        w.left.color = "black"
                    self._rotate_right(x.parent)
                    x = self.root
        if x:
            x.color = "black"


    def seeTree(self):
        self._print_tree(self.root)
        print()

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print(f"{node.key} ({node.color})", end=' ')
            self._print_tree(node.right)



rbt = RedBlackTree()

# Operation 1 >>> INSERT the salary values from the dictionary <<<
for name, salary in salary_dic.items():  
    rbt.insert(salary)

print("\nRed-Black Tree after insertions:")
rbt.seeTree()


# Operation 2 >>> DELETING a salary <<<
salary_to_delete = 115500
rbt.delete(salary_to_delete)
print(f"\nRed-Black Tree after deleting {salary_to_delete}:")
rbt.seeTree()


#Operation 3 >>> SEARCHING a salary <<<
salary_to_search = 22500

found = False
def search_tree(node, key):
    global found
    if node:
        search_tree(node.left, key)
        if node.key == key:
            found = True
        search_tree(node.right, key)

search_tree(rbt.root, salary_to_search)
if found:
    print(f"\nSalary {salary_to_search} found in the tree.")
else:
    print(f"\nSalary {salary_to_search} not found in the tree.")






