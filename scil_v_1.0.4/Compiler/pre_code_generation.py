
# This module implements a pre-phase to the code generation. For this
# simple language not much is needed. The only task here is to
# assign unique labels to functions such that code generation work
# for functions not defined in a bottom-up order, including mutual
# recursion, where no order would work without this early assignment
# of labels. The module is based on the visitors_base and AST modules
# that together implement the recursive traversal and visit functionality.


from visitors_base import VisitorsBase


class Labels:
    """Generate unique labels with a descriptive string at the end."""
    def __init__(self):
        self.counter = -1

    def next(self, s):
        self.counter += 1
        return "F" + str(self.counter).zfill(3) + "_" + s


# Pre Code Generation

class ASTPreCodeGenerationVisitor(VisitorsBase):
    """Implements the pre code generation phase based on the AST."""
    def __init__(self):
        # The unique labels generator:
        self._labels = Labels()

    def getLabelsGenerator(self):
        return self._labels

    def preVisit_function(self, t):
        if t.name == "main":
            t.start_label = "main"
            t.end_label = "end_main"
        else:
            t.start_label = self._labels.next(t.name)
            t.end_label = self._labels.next(f"end_{t.name}")
