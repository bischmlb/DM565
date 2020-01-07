class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def accept(self, visitor):
        visitor.preVisit(self)
        if self.left:
            self.left.accept(visitor)
        visitor.midVisit(self)
        if self.right:
            self.right.accept(visitor)
        visitor.postVisit(self)


class Leaf:
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        visitor.visit(self)
