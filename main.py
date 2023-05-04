import sys
from antlr4 import *
from generated.AdaGrammarLexer import AdaGrammarLexer
from generated.AdaGrammarParser import AdaGrammarParser
from generated.AdaGrammarParserVisitor import AdaGrammarParserVisitor
class AdaVisitor(AdaGrammarParserVisitor):

    operators_map = {
        "and": "and",
        "or": "or",
        "not": "not",
        ":=": "=",
        "=": "==",
        "/=": "!=",
        "<": "<",
        "<=": "<=",
        ">": ">",
        ">=": ">=",
        "+": "+",
        "-": "-",
        "*": "*",
        "/": "/",
        "**": "**",
        "mod": "%",
    }

    type_map = {
        "Integer": "int",
        "Float": "float",
        "String": "str",
        "Boolean": "bool",
    }
    type_map_declaration = {
        "Integer": 0,
        "Float": 0.0,
        "String": "",
        "Boolean": False,
    }

    def write(self, text):
        self.out_file.write(self.tab_count * "\t" + text + "\n")

    def __init__(self):
        self.out_file = open("python.py", "w")
        self.out_file.write("import sys\n")
        self.tab_count = 0

    def visitProgram(self, ctx):
        print("Program")
        return self.visitChildren(ctx)
    
    def visitProgram_declaration(self, ctx):
        print("Program_declaration")
        return super().visitProgram_declaration(ctx)
        
    def visitVariable_declaration(self, ctx):
        print("Variable_declaration")
        print(ctx.getChild(0).getText())
        return self.visitChildren(ctx)
    
    def visitExpression(self, ctx):
        print("Expression")
        if ctx.getChildCount() == 1:
            return self.visitChildren(ctx)
            


    def visitIf_statement(self, ctx):
        print("If_statement")
        self.write("if " + ctx.getChild(1).getText() + ":")
        self.tab_count += 1
        self.visitChildren(ctx)
        self.tab_count -= 1
    
    def visitElsif_statement(self, ctx):
        print("Elsif_statement")
        self.tab_count -= 1
        self.write("elif " + ctx.getChild(1).getText() + ":")
        self.tab_count += 1
        self.visitChildren(ctx)
        self.tab_count -= 1
    
    def visitElse_statement(self, ctx):
        print("Else_statement")
        self.write("else:")
        self.tab_count += 1
        self.visitChildren(ctx)
        self.tab_count -= 1
    
    def visitAssignment_statement(self, ctx):
        print("Assignment_statement")
        return super().visitAssignment_statement(ctx)

    def visitLoop_statement(self, ctx):
        print("Loop_statement")
        return super().visitLoop_statement(ctx)
    
    def visitType_declaration(self, ctx):
        print("Type_declaration")
        return self.visitChildren(ctx)
    def visitBegin_end_block(self, ctx):
        return super().visitBegin_end_block(ctx)
    def visitPackage_import(self, ctx):
        print("Package_import")
        return super().visitPackage_import(ctx)
    
    def visitFull_variable_declaration(self, ctx ):
        print("Full_variable_declaration")
        id = ctx.getToken(AdaGrammarParser.ID, 0)
        for child in ctx.getChildren():
            print(child.getText())
        self.write(id.getText() + " : " + self.type_map[ctx.getChild(2).getText()] + " = " + ctx.getChild(4).getText())
    
    def visitVariable_declaration(self, ctx):
        print("Variable_declaration")
        for i in ctx.getTokens(AdaGrammarParser.ID):
            self.write(i.getText() + " : "  +  self.type_map[ctx.getChild(2).getText()] + " = " + str(self.type_map_declaration[ctx.getChild(2).getText()]))

    def visitProcedure_call_statement(self, ctx):
        print("Procedure_call_statement")
        if ctx.getChild(0).getText() == "Put_Line":
            self.write("print(" + ctx.getChild(2).getText() + ")")
        
        return super().visitProcedure_call_statement(ctx)

    def visitLoop_statement(self, ctx):
        print("Loop_statement")
        self.tab_count += 1
        self.visitChildren(ctx)
        self.tab_count -= 1


    def visitWhile_loop(self, ctx):
        print("While_loop")
        self.write("while " + ctx.getChild(1).getText() + ":")
        self.visitChildren(ctx)

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
    #print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main() 