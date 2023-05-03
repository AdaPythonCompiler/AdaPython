import sys
from antlr4 import *

from disc.AdaLexer import AdaLexer
from disc.AdaParser import AdaParser
from disc.AdaVisitor import AdaVisitor


input_stream = FileStream("/Users/mati/Desktop/Kompilatory_projekt/AdaPython/hello.adb")
Lexer = AdaLexer(input_stream)
print(Lexer)
token_stream = CommonTokenStream(Lexer)
print("test")
parser = AdaParser(token_stream)
tree = parser.program()


s = tree.toStringTree(recog=parser)

tab_count = 0
for c in s:
    if c == '(':
        print(c)
        tab_count += 1
        print('\t' * tab_count, end='')
    elif c == ')':
        tab_count -= 1
        print('\n', '\t' * tab_count, c, end='')
        tab_count = max(tab_count, 0)  # nie pozwalamy na ujemną ilość tabulacji
    else:
        print(c, end='')

class AdaVisitor(AdaVisitor):
    def visitProgram(self, ctx):
        print("Program")
        return self.visitChildren(ctx)
    
    def visitDeclaration(self, ctx):
        print("Declaration")
        return self.visitChildren(ctx)
    
    def visitVariable_declaration(self, ctx):
        print("Variable_declaration")
        return self.visitChildren(ctx)
    
    def visitType_declaration(self, ctx):
        print("Type_declaration")
        return self.visitChildren(ctx)
    def visitBegin_end_block(self, ctx):
        return super().visitBegin_end_block(ctx)
    def visitPackage_import(self, ctx):
        print("Package_import")
        return super().visitPackage_import(ctx)
    def visitProcedure_call_statement(self, ctx):
        print("Procedure_call_statement")
        return super().visitProcedure_call_statement(ctx)

    pass
print("test")
AdaVisitor().visit(tree)

