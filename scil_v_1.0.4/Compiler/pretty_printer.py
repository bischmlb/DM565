
# This module is for development and debugging purposes, printing a
# reasonable layout version of the input program.
# It is based on the visitors_base and AST modules that together implement
# the recursive traversal and visit functionality.


from visitors_base import VisitorsBase


class ASTPrettyPrinterVisitor(VisitorsBase):
    """The visitor implementing the pretty printing of the AST."""
    def __init__(self):
        self._indentation = 0
        self._tab = 3
        self._text = []
        self._make_newline = False

    def getPrettyProgram(self):
        return "".join(self._text)

    def _indent(self):
        self._indentation += self._tab

    def _outdent(self):
        self._indentation -= self._tab

    def _newline(self):
        self._make_newline = True

    def _write(self, s):
        if self._make_newline:
            self._text.append("\n" + self._indentation * " ")
            self._make_newline = False
        self._text.append(s)

    def preVisit_variables_declaration_sequence(self, t):
        self._write("var ")

    def midVisit_variables_declaration_sequence(self, t):
        self._newline()

    def preVisit_function(self, t):
        self._newline()
        self._write("function " + t.name + "(")

    def midVisit_function(self, t):
        self._write(")")
        self._newline()
        self._indent()

    def postVisit_function(self, t):
        self._newline()
        self._outdent()

    def preVisit_parameter_list(self, t):
        self._write(t.parameter)
        if t.next:
            self._write(", ")

    def preVisit_variables_list(self, t):
        self._write(t.variable)
        if t.next:
            self._write(", ")

    def preVisit_statement_return(self, t):
        self._write("return ")

    def postVisit_statement_return(self, t):
        self._write(";")
        self._newline()

    def preVisit_statement_print(self, t):
        self._write("print ")

    def postVisit_statement_print(self, t):
        self._write(";")
        self._newline()

    def preVisit_statement_assignment(self, t):
        self._write(t.lhs + " = ")

    def postVisit_statement_assignment(self, t):
        self._write(";")
        self._newline()

    def preVisit_statement_ifthenelse(self, t):
        self._write("if ")

    def preMidVisit_statement_ifthenelse(self, t):
        self._write(" then")
        self._newline()
        self._indent()

    def postMidVisit_statement_ifthenelse(self, t):
        self._outdent()
        self._write("else")
        self._newline()
        self._indent()

    def postVisit_statement_ifthenelse(self, t):
        self._newline()
        self._outdent()

    def preVisit_statement_while(self, t):
        self._write("while ")

    def midVisit_statement_while(self, t):
        self._write(" do")
        self._newline()
        self._indent()

    def postVisit_statement_while(self, t):
        self._newline()
        self._outdent()

    def postVisit_expression_integer(self, t):
        self._write(str(t.integer))

    def postVisit_expression_identifier(self, t):
        self._write(t.identifier)

    def preVisit_expression_call(self, t):
        self._write(t.name + "(")

    def postVisit_expression_call(self, t):
        self._write(")")

    def preVisit_expression_binop(self, t):
        self._write("(")

    def midVisit_expression_binop(self, t):
        self._write(t.op)

    def postVisit_expression_binop(self, t):
        self._write(")")

    def midVisit_expression_list(self, t):
        if t.next:
            self._write(", ")
