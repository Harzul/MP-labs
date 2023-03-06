class Node:
    def __init__(self, key=None, value=None, color='r'):
        self.color = color
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class Functor:
    def __call__(self, first_val, sec_val):
        try:
            return True if first_val < sec_val else False
        except TypeError:
            return False


class RBTree:
    def __init__(self, key=None, value=None):
        if key is not None and value is not None:
            self.new = Node(None, None, 'b')
            self.root = Node(key, value, 'b')
            self.root.left = self.new
            self.root.right = self.new
        else:
            self.new = Node(None, None, 'b')
            self.root = self.new
        self.F = Functor()

    def RBprint(self):
        try:
            if self.root.key is not None:
                print("|||||||||||||||ROOT-NODE|||||||||||||||||||")
                print("Key: " + str(self.root.key))
                print("Value: " + str(self.root.value))
                print("Color: " + str(self.root.color))
                if self.root.left.key is not None:
                    print("Left: exist  = " + str(self.root.left.key))
                else:
                    print("Left: Doesn't exist ")
                if self.root.right.key is not None:
                    print("Right: exist = " + str(self.root.right.key))
                else:
                    print("Right: Doesn't exist ")
                print("|||||||||||||||||||||||||||||||||||||||||||\n")
                self.__print__(self.root)
        except AttributeError:
            print("Tree is empty")
            return

    def __print__(self, node):
        try:
            if node.left.key is not None:
                print("|||||||||||||||||NODE|||||||||||||||||||||")
                print("Key: " + str(node.left.key))
                print("Value: " + str(node.left.value))
                print("Color: " + str(node.left.color))
                if node.left.left.key is not None:
                    print("Left: exist  = " + str(node.left.left.key))
                else:
                    print("Left: Doesn't exist ")
                if node.left.right.key is not None:
                    print("Right: exist  = " + str(node.left.right.key))
                else:
                    print("Right: Doesn't exist ")
                print("|||||||||||||||||||||||||||||||||||||||||||\n")
                self.__print__(node.left)
            if node.right.key is not None:
                print("|||||||||||||||||NODE|||||||||||||||||||||")
                print("Key: " + str(node.right.key))
                print("Value: " + str(node.right.value))
                print("Color: " + str(node.right.color))
                if node.right.left.key is not None:
                    print("Left: exist  = " + str(node.right.left.key))
                else:
                    print("Left: Doesn't exist ")
                if node.right.right.key is not None:
                    print("Right: exist  = " + str(node.right.right.key))
                else:
                    print("Right: Doesn't exist ")
                print("|||||||||||||||||||||||||||||||||||||||||||\n")
                self.__print__(node.right)
        except AttributeError:
            print("Tree is empty")
            return

    def insert(self, key, value):
        try:
            ins_node = Node(key, value)
            ins_node.left = self.new
            ins_node.right = self.new

            curr_node = self.root
            prev_node = None
            while curr_node != self.new:
                prev_node = curr_node
                if self.F(key, curr_node.key):
                    curr_node = curr_node.left
                elif self.F(curr_node.key, key):
                    curr_node = curr_node.right
                else:
                    return
            ins_node.parent = prev_node
            if prev_node is None:
                self.root = ins_node
            elif self.F(key, prev_node.key):
                prev_node.left = ins_node
            elif self.F(prev_node.key, key):
                prev_node.right = ins_node

            self.fix_insert(ins_node)
        except AttributeError:
            return ""

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'r':
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 'r':
                    uncle.color = 'b'
                    node.parent.color = 'b'
                    node.parent.parent.color = 'r'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotation(node)
                    node.parent.color = 'b'
                    node.parent.parent.color = 'r'
                    self.left_rotation(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.color == 'r':
                    uncle.color = 'b'
                    node.parent.color = 'b'
                    node.parent.parent.color = 'r'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotation(node)
                    else:
                        if node == node.parent.right:
                            node = node.parent
                            self.left_rotation(node)
                        node.parent.color = 'b'
                        node.parent.parent.color = 'r'
                        self.right_rotation(node.parent.parent)
        self.root.color = 'b'

    def left_rotation(self, node):
        changed_node = node.right
        node.right = changed_node.left
        if changed_node.left != self.new:
            changed_node.left.parent = node

        changed_node.parent = node.parent
        if node.parent is None:
            self.root = changed_node
        elif node == node.parent.left:
            node.parent.left = changed_node
        else:
            node.parent.right = changed_node
        changed_node.left = node
        node.parent = changed_node

    def right_rotation(self, node):
        changed_node = node.left
        node.left = changed_node.right
        if changed_node.right != self.new:
            changed_node.right.parent = node

        changed_node.parent = node.parent
        if node.parent is None:
            self.root = changed_node
        elif node == node.parent.right:
            node.parent.right = changed_node
        else:
            node.parent.left = changed_node
        changed_node.right = node
        node.parent = changed_node

    def search(self, key):
        curr_node = self.root
        while curr_node != self.new and key != curr_node.key:
            if self.F(key, curr_node.key):
                curr_node = curr_node.left
            elif self.F(curr_node.key, key):
                curr_node = curr_node.right
        if curr_node.key != key:
            return "No such element"
        else:
            print("|||||||||||||||Searched-NODE|||||||||||||||||||")
            print("Key: " + str(curr_node.key))
            print("Value: " + str(curr_node.value))
            print("Color: " + str(curr_node.color))
            if curr_node.left.key is not None:
                print("Left: exist  = " + str(curr_node.left.key))
            else:
                print("Left: Doesn't exist ")
            if curr_node.right.key is not None:
                print("Right: exist = " + str(curr_node.right.key))
            else:
                print("Right: Doesn't exist ")

            print("|||||||||||||||||||||||||||||||||||||||||||\n")

    def is_empty(self):
        return True if self.root.key is None else False

    def __dell(self, node):
        if node:
            # node.value.cleanup()

            self.__dell(node.left)
            self.__dell(node.right)

            node.left = None
            node.right = None

    def RBdelete(self):
        if self.root is None:
            return
        elif self.root.left is None and self.root.right is None:
            self.root = None
            return
        else:
            self.__dell(self.root)
            self.root.color = None
            self.root.value = None
            self.root.key = None
            self.root = None


RB = RBTree(1, 2)
for i in range(2, 10):
    RB.insert(i, i * 2)
RB.RBprint()
RB.RBdelete()
RB.RBprint()