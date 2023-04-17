# Generated from AdaGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AdaGrammarParser import AdaGrammarParser
else:
    from AdaGrammarParser import AdaGrammarParser

# This class defines a complete listener for a parse tree produced by AdaGrammarParser.
class AdaGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by AdaGrammarParser#program.
    def enterProgram(self, ctx:AdaGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#program.
    def exitProgram(self, ctx:AdaGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#statementList.
    def enterStatementList(self, ctx:AdaGrammarParser.StatementListContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#statementList.
    def exitStatementList(self, ctx:AdaGrammarParser.StatementListContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#statement.
    def enterStatement(self, ctx:AdaGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#statement.
    def exitStatement(self, ctx:AdaGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#expression.
    def enterExpression(self, ctx:AdaGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#expression.
    def exitExpression(self, ctx:AdaGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#assignment.
    def enterAssignment(self, ctx:AdaGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#assignment.
    def exitAssignment(self, ctx:AdaGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#procedureCall.
    def enterProcedureCall(self, ctx:AdaGrammarParser.ProcedureCallContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#procedureCall.
    def exitProcedureCall(self, ctx:AdaGrammarParser.ProcedureCallContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#argumentList.
    def enterArgumentList(self, ctx:AdaGrammarParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#argumentList.
    def exitArgumentList(self, ctx:AdaGrammarParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:AdaGrammarParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:AdaGrammarParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#loopStatement.
    def enterLoopStatement(self, ctx:AdaGrammarParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#loopStatement.
    def exitLoopStatement(self, ctx:AdaGrammarParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#exitStatement.
    def enterExitStatement(self, ctx:AdaGrammarParser.ExitStatementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#exitStatement.
    def exitExitStatement(self, ctx:AdaGrammarParser.ExitStatementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#returnStatement.
    def enterReturnStatement(self, ctx:AdaGrammarParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#returnStatement.
    def exitReturnStatement(self, ctx:AdaGrammarParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#nullStatement.
    def enterNullStatement(self, ctx:AdaGrammarParser.NullStatementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#nullStatement.
    def exitNullStatement(self, ctx:AdaGrammarParser.NullStatementContext):
        pass



del AdaGrammarParser