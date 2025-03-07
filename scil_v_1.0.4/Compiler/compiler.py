#!/usr/bin/env python3

# Copyright (C) 2019
# Kim Skak Larsen
# All rights reserved.
# License: GNU GPLv3

# Description: A compiler is implemented. The implementation is meant for
# teaching purposes. The goal is to illustrate important compiler
# techniques in a simple setting and to enable the students to make
# minor adjustments and extensions. The source language is a simple
# imperative languages with integers being the only type, but including
# expressions, assignment, control structures, and function definitions
# and calls, including recursion and static nested scope. The target
# language is 64 bit x86 assembler using the GNU syntax.

import sys
import getopt

import interfacing_parser
from errors import error_message
from lexer_parser import parser
from symbols import ASTSymbolVisitor
from type_checking import ASTTypeCheckingVisitor
from pretty_printer import ASTPrettyPrinterVisitor
from code_generation import ASTCodeGenerationVisitor
from pre_code_generation import ASTPreCodeGenerationVisitor
from emit import Emit


__version__ = "1.0.4"


# MAIN

def compiler(showSource, input_file, output_file):
    """This function goes through the classic phases of a modern compiler,
    each phase organized in its own module. The phases are:

    parsing:
        handled using the ply package - the parser module includes a lexer,
        and it builds an abstract syntax tree (AST).

    symbol collection:
        collects function, parameter, and variables names, and stores these
        in a symbol table.

    code generation:
        from the AST and symbol table, code is produced in an intermediate
        representation, quite close to the final assembler code.

    emit:
        the slightly abstract intermediate code is transformed to assembler
        code.
    """

    # Read and verify ASCII input:
    encodingError = False
    try:
        if input_file:
            with open(input_file) as f:
                text = f.read()
        else:
            text = sys.stdin.read()
        try:
            text.encode("ascii")
        except UnicodeEncodeError:  # Check for non-ascii
            encodingError = True
    except UnicodeDecodeError:  # Check for unicode
        encodingError = True
    if encodingError:
        error_message("Set-Up", "The input is not in ASCII.", 1)

    # Parse input text:
    parser.parse(text)

    # the_program is the resulting AST:
    if interfacing_parser.parsing_error:
        exit()
    the_program = interfacing_parser.the_program

    if showSource:

        # Pretty print program:
        pp = ASTPrettyPrinterVisitor()
        the_program.accept(pp)
        return pp.getPrettyProgram()

    else:

        # Collect names of functions, parameters, and local variables:
        symbols_collector = ASTSymbolVisitor()
        the_program.accept(symbols_collector)
        symbol_table = symbols_collector.getSymbolTable()

        # Type check use of functions, parameters, and local variables:
        type_checker = ASTTypeCheckingVisitor(symbol_table)
        the_program.accept(type_checker)

        # Assign unique labels to functions:
        pre_intermediate_code_generator = ASTPreCodeGenerationVisitor()
        the_program.accept(pre_intermediate_code_generator)

        # Generate intermediate code:
        intermediate_code_generator = ASTCodeGenerationVisitor(
            symbol_table, pre_intermediate_code_generator.getLabelsGenerator())
        the_program.accept(intermediate_code_generator)
        intermediate_code = intermediate_code_generator.get_code()

        # Emit the target code:
        emitter = Emit(intermediate_code,
                       pre_intermediate_code_generator.getLabelsGenerator())
        emitter.emit()
        code = emitter.get_code()

        return code


def main(argv):
    usage = f"Usage: {sys.argv[0]} [-hvs] [-i source_file] [-o target_file]"
    help_text = """
    -h  Print this help text.

    -v  Print the version number.

    -s  Print back the parsed source code instead of target code.

    -i source_file  Set source file; default is stdin.

    -o target_file  Set target file; default is stdout.
    """
    input_file = ""
    output_file = ""
    show_source = False
    try:
        opts, args = getopt.getopt(argv, "hsvi:o:")
    except getopt.GetoptError:
        print(usage)
        sys.exit(1)
    for opt, arg in opts:
        if opt == "-h":
            print(usage)
            print(help_text)
            sys.exit(0)
        elif opt == "-v":
            print(__version__)
            sys.exit(0)
        elif opt == "-s":
            show_source = True
        elif opt == "-i":
            input_file = arg
        elif opt == "-o":
            output_file = arg
    result = compiler(show_source, input_file, output_file)
    if output_file:
        f = open(output_file, "w")
        f.write(result)
        f.close()
    else:
        print(result)


if __name__ == "__main__":
    main(sys.argv[1:])
