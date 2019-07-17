"""
2019-03-25
by z
循环双链表
"""

class Node:
    # 初始化结点函数
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoubleLinedList:

    #初始化头节点..
    def __init__(self):
        self.head = Node(None)

    #创建双链表函数
    def Create(self):
        cNode = self.head
        Element = input()
        while Element != "#":
            nNode = Node(int(Element))
            cNode.next = nNode
            nNode.prev = cNode
            nNode.next = self.head
            self.head.prev = nNode
            cNode = cNode.next
            Element = input()

    #单链表长度
    def Length(self):
        cNode = self.head
        length = 0
        while cNode.next != self._head:
            length = length +1
            cNode = cNode.next
        return length

    #判断是否为空
    def IsEmpty(self):
        if self.Length() == 0:
            return True
        else:
            return False

    #尾端插入元素
    def InsertE(self):
        Element = input()
        if Element == "#":
            return
        cNode = self.head
        nNode = Node(int(Element))
        while cNode.next != self._head:
            cNode = cNode.next
        cNode.next = nNode
        nNode.prev = cNode
        nNode.next = self.head
        self.head.prev = nNode

    #首端插入元素
    def InsertEh(self):
        Element = input()
        if Element == "#":
            return
        cNode = self.head.next
        pNode = self.head
        nNode = Node(int(Element))
        nNode.prev = pNode
        pNode.next = nNode
        nNode.next = cNode
        cNode.next = nNode

    #查找
    def Find(self):
        Pos = 0
        cNode = self.head
        key = int(input())
        if self.IsEmpty():
            print("empty")
            return
        while cNode.next != self._head and cNode.data != key:
            cNode = cNode.next
            Pos = Pos + 1
        if cNode.data == key:
            print(Pos)
        else:
            print(False)

    #删除
    def Delete(self):
        Element = int(input())
        cNode = self.head
        pNode = self.head
        if self.IsEmpty():
            return
        while cNode.next != self._head and cNode.data != Element:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == Element:
            qNode = cNode.next
            pNode.next = qNode
            qNode.prev = pNode
            del cNode

    #输出
    def Visit(self,tNode):
        if tNode != None:
            print(tNode.data,"->")
        else:
            print(None)

    #遍历
    def Travel(self):
        cNode = self.head
        if self.IsEmpty():
            return
        while cNode.next != self._head:
            cNode = cNode.next
            self.Visit(cNode)

CircularDoubleLinedList = CircularDoubleLinedList()
CircularDoubleLinedList.Create()
