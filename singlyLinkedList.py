class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class listElement():
    usn = 0
    name = ""
    branch = ""
    semester = 0
    phoneNum = 0


class SLinkedList:
    def __init__(self):
        self.headval = None

    # Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(
                printval.dataval.usn + " " + printval.dataval.name + " " + printval.dataval.branch + " " + printval.dataval.semester
                + " " + printval.dataval.phoneNum)
            printval = printval.nextval

    def insertAtBegining(self, newData):
        NewNode = Node(newData)
        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    def insertAtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    def deleteAtEnd(self):

        if self.headval is None:
            return None
        if self.headval.nextval is None:
            self.headval = None
            return None
        second_last = self.headval
        while second_last.nextval.nextval is not None:
            second_last = second_last.nextval
        second_last.nextval = None
        return self.headval

    def createObject(self):
        usn, name, branch, sem, phone = input("Enter USN, Name, Branch, Semester, and Phone Number: ").split()
        element = listElement()
        element.usn = usn
        element.name = name
        element.branch = branch
        element.semester = sem
        element.phoneNum = phone
        return element

    def stackImplement(self):
        isTrue1 = True
        while isTrue1:
            print("1:Push operation \n2:Pop operation \n3:Display \n4:Exit")
            inp1 = int(input("Enter choice: "))
            if inp1 == 1:
                element = list.createObject()
                list.insertAtEnd(element)
            elif inp1 == 2:
                list.deleteAtEnd()
            elif inp1 == 3:
                list.listprint()
            elif inp1 == 4:
                isTrue1 = False
            else:
                print("Invalid input...")

isTrue = True
list = SLinkedList()
while isTrue:
    print("1:Create SLL of Student Nodes \n2:DisplayStatus \n3:InsertAtEnd \n4:DeleteAtEnd \n5:Stack Demo using SLL("
          "Insertion and Deletion at Front) \n6:Exit")
    inp = int(input("Enter choice: "))
    if inp == 1:
        studentNum = int(input("Enter number of student: "))
        while studentNum > 0:
            element = list.createObject()
            list.insertAtBegining(element)
            studentNum -= 1
    elif inp == 2:
        list.listprint()
    elif inp == 3:
        studentNum = int(input("Enter number of student: "))
        while studentNum > 0:
            element = list.createObject()
            list.insertAtEnd(element)
            studentNum -= 1
    elif inp == 4:
        list.deleteAtEnd()
    elif inp == 5:
        list.stackImplement()
    elif inp == 6:
        isTrue = False
    else:
        print("Wrong Input...")

# 2 t kh 3 234
# 1 r kh 3 123
# 4 u kh 3 456
# 5 i kh 3 567