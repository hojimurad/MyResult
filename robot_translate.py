#
#
#
#
#
# word = input()
#
#
# natija=""
#
#
#
# for i in range(len(word)):
#
#     nums =""
#     if  word[i].isdigit()
#
#


class Stack:
    def __init__(self):
        self.list = []
    def push(self, a):
        return self.list.append(a)
    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[0]


s2 = Stack()

s2.push("Sa")

print(s2.peek())