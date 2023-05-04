import sys
from antlr4 import *
from generated.AdaGrammarLexer import AdaGrammarLexer
from generated.AdaGrammarParser import AdaGrammarParser
from generated.AdaGrammarParserVisitor import AdaGrammarParserVisitor

class AdaVisitor(AdaGrammarParserVisitor):
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

def main():
    
    input_stream = FileStream("examples/simple.ada")
    lexer = AdaGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AdaGrammarParser(stream)
    tree = parser.program()
    visitor = AdaVisitor()
    visitor.visit(tree)

    for i in tree.getChildren():
        print(i.getText())
        print("----")
    
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
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main() 