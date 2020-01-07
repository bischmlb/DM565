#!/usr/bin/python3

from pretty_printer import PreOrderVisitor, InOrderVisitor, LeavesVisitor
from tree import Node, Leaf


myTree = Node(Leaf(1), Node(Node(Leaf(3), Leaf(5), 4), Leaf(7), 6), 2)


def main():
    pp = PreOrderVisitor()
    myTree.accept(pp)
    print("----------")
    pp = InOrderVisitor()
    myTree.accept(pp)
    print("----------")
    pp = LeavesVisitor()
    myTree.accept(pp)


if __name__ == "__main__":
    main()
