class VisitorsBase:

    def _visit(self, t, s):
        method = getattr(self, s + "_" + t.__class__.__name__, None)
        if method:
            method(t)

    def visit(self, t):
        self._visit(t, "visit")

    def preVisit(self, t):
        self._visit(t, "preVisit")

    def midVisit(self, t):
        self._visit(t, "midVisit")

    def postVisit(self, t):
        self._visit(t, "postVisit")
