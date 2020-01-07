
from visitors_base import VisitorsBase


class PreOrderVisitor(VisitorsBase):
    """The visitor implementing the printing of the tree."""
    def __init__(self):
        pass

    def preVisit_Node(self, t):
        print(t.value)

    def visit_Leaf(self, t):
        print(t.value)


class InOrderVisitor(VisitorsBase):
    """The visitor implementing the printing of the tree."""
    def __init__(self):
        pass

    def midVisit_Node(self, t):
        print(t.value)

    def visit_Leaf(self, t):
        print(t.value)


class LeavesVisitor(VisitorsBase):
    """The visitor implementing the printing of the tree."""
    def __init__(self):
        pass

    def visit_Leaf(self, t):
        print(t.value)
