import sys
import PySimpleGUI as sg
import time
from pyrecord import Record
from antlr4 import *
from generated.AdaGrammarLexer import AdaGrammarLexer
from generated.AdaGrammarParser import AdaGrammarParser
from generated.AdaGrammarParserVisitor import AdaGrammarParserVisitor

class AdaVisitor(AdaGrammarParserVisitor):


    procedureList = []

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

    def write(self, text, new_line=True):
        if new_line:
            self.out_file.write(self.tab_count * "\t" + text + "\n")
        else:
            self.out_file.write(self.tab_count * "\t" + text)

    def __init__(self):
        self.out_file = open("python.py", "w")
        self.out_file.write("import sys\n")
        self.tab_count = 0

    def get_file(self):
        return self.out_file
    
    def visitProgram(self, ctx):
        print("Program")
        return self.visitChildren(ctx)
    
    def visitProgram_declaration(self, ctx):
        print("Program_declaration")
        self.write("def " + ctx.program_head().getText() + "():")
        if self.tab_count == 0:
            self.procedureList.append(ctx.program_head().getText() + "()")
        self.tab_count += 1
        self.visitChildren(ctx)
        self.tab_count -= 1
        # return self.visitChildren(ctx)
    def visitExpression(self, ctx):
        print("Expression")
        return super().visitExpression(ctx)

    def visitIf_statement(self, ctx):
        print("If_statement")
        buf = ctx.getChild(1).getText()
        for key in self.operators_map:
            if key in buf:
                buf = buf.replace(key, self.operators_map[key])
        self.write("if " +  buf + ":")
        self.tab_count += 1
        for i in ctx.statement():
            self.visit(i)
        self.tab_count -= 1
        # if ctx.getChildCount() > 7:
        #     self.visit(ctx.getChild(4))
        #     self.visit(ctx.getChild(5))
        for i in ctx.elsif_statement():
            self.visit(i)
        self.visit(ctx.else_statement())

    def visitElsif_statement(self, ctx):
        print("Elsif_statement")
        buf = ctx.getChild(1).getText()
        for key in self.operators_map:
            if key in buf:
                buf = buf.replace(key, self.operators_map[key])
        self.write("elif " + buf + ":")
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
        self.visitChildren(ctx)

    def visitWhile_loop(self, ctx):
        print("While_loop")
        self.write("while " + ctx.getChild(1).getText() + ":")
        self.tab_count += 1
        self.visitChildren(ctx)
        self.tab_count -= 1

    def visitAssignment_statement(self, ctx):
        print("Assignment_statement")
        self.write(ctx.getChild(0).getText() + " " + self.operators_map[ctx.getChild(1).getText()] + " " + ctx.getChild(2).getText())
        self.visitChildren(ctx)

    def visitFor_loop(self, ctx):
        print("For_loop")
        self.write("for " + ctx.getChild(1).getText() + " in ", False)
        self.visit(ctx.range_())
        self.tab_count += 1
        for i in ctx.statement():
            self.visit(i)
        self.tab_count -= 1
        
    def visitRange(self, ctx):
        print("Range")
        self.out_file.write('range(' + ctx.simple_expression(0).getText() + ", " + str(int(ctx.simple_expression(1).getText()) + 1) + "):" + "\n")

    def visitBasic_loop(self, ctx):
        print("Basic_loop")
        self.write("while True:")
        self.tab_count += 1
        self.visitChildren(ctx)
        self.tab_count -= 1
    
    def visitCase_statement(self, ctx):
        print("Case_statement")
        x = 0
        for i in ctx.case_statement_alternative():
            if x == 0:
                self.write('if ' + ctx.getChild(1).getText() + ' == ' + i.expression().getText() + ':')
                x = 1
            elif i.getChild(1).getText() == 'others':
                self.write('else:')
            else:
                self.write('elif ' + ctx.getChild(1).getText() + ' == ' + i.expression().getText() + ':')
            self.tab_count += 1
            self.visitChildren(i)
            self.tab_count -= 1

    def visitType_declaration(self, ctx):
        print("Type_declaration")
        return self.visitChildren(ctx)
    
    def visitType_array_declaration(self, ctx):
        print("Type_array_declaration")
        id = ctx.ID().getText()
        self.write(id +": list" + " = [x for x in range(" + ctx.simple_expression(0).getText() + ", " +  str(int(ctx.simple_expression(1).getText()) + 1) + ")]")
        
    def visitEndOfFile(self):
        print("EndOfFile")
        n = len(self.procedureList)
        if n > 0:
            self.write("if __name__ == '__main__':")
            self.tab_count += 1
            for i in self.procedureList:
                self.write(i)
            for i in range(n):
             self.procedureList.pop()
            self.tab_count -= 1

        
def main():
    input_code_column = [
        [sg.Text('Wprowadź kod w języku Ada:', font=('Arial', 14))],
        [sg.Multiline(key='-INPUT-', size=(80, 20),font=('Arial', 14))],
        [sg.Button('Wykonaj', key='-EXECUTE-', size=(54, 3)),
            sg.Button('Wyczyść', key='-CLEAR-', size=(54, 3))]
    ]

    output_code_column = [
        [sg.Text('Kod w języku Python:', font=('Arial', 14))],
        [sg.Multiline(key='-OUTPUT-', size=(80, 20),font=('Arial', 14))]
    ]


    terminal_bottom = [
        [sg.Text('Terminal:', font=('Arial', 14))],
        [sg.Multiline(key='-TERMINAL-', size=(160, 20),font=('Arial', 14))]
    ]

    layout = [
        [sg.Column(input_code_column),
        sg.VSeperator(),
        sg.Column(output_code_column)],
        [sg.Column(terminal_bottom)]
    ]

    window = sg.Window('AdaToPython', layout)

    while True:  # Event Loop
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == '-EXECUTE-':
            input_stream = InputStream(values['-INPUT-'])

            lexer = AdaGrammarLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = AdaGrammarParser(stream)
            SyntaxErrorListener = parser.SyntaxErrorListener()
            parser.addErrorListener(SyntaxErrorListener)
            
            tree = parser.program()
            visitor = AdaVisitor()
            visitor.visit(tree)
            visitor.visitEndOfFile()
            visitor.out_file.close()
            

            
            with open('python.py', 'r') as f:
                output_text = f.read()

            output_text = output_text.replace('\t', '    ')
            window['-OUTPUT-'].update(output_text)

            number_of_errors = parser.getNumberOfSyntaxErrors()
            if number_of_errors > 0:
               
                window['-TERMINAL-'].update(SyntaxErrorListener.getSyntaxErrors())
            #write antlr errors to terminal

                
        elif event == '-CLEAR-':
            window['-INPUT-'].update('')
            window['-OUTPUT-'].update('')
            with open('python.py', 'w') as f:
                f.write('')

        

    window.close()
    


if __name__ == '__main__':
    main() 