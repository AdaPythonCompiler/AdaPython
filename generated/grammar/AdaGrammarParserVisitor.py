# Generated from grammar/AdaGrammarParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AdaGrammarParser import AdaGrammarParser
else:
    from AdaGrammarParser import AdaGrammarParser

# This class defines a complete generic visitor for a parse tree produced by AdaGrammarParser.

class AdaGrammarParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AdaGrammarParser#program.
    def visitProgram(self, ctx:AdaGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#package_import.
    def visitPackage_import(self, ctx:AdaGrammarParser.Package_importContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#package_use.
    def visitPackage_use(self, ctx:AdaGrammarParser.Package_useContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#program_declaration.
    def visitProgram_declaration(self, ctx:AdaGrammarParser.Program_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#program_head.
    def visitProgram_head(self, ctx:AdaGrammarParser.Program_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#input_vars.
    def visitInput_vars(self, ctx:AdaGrammarParser.Input_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#variable_declaration.
    def visitVariable_declaration(self, ctx:AdaGrammarParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#full_variable_declaration.
    def visitFull_variable_declaration(self, ctx:AdaGrammarParser.Full_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#type.
    def visitType(self, ctx:AdaGrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#begin_end_block.
    def visitBegin_end_block(self, ctx:AdaGrammarParser.Begin_end_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#statement.
    def visitStatement(self, ctx:AdaGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#if_statement.
    def visitIf_statement(self, ctx:AdaGrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#loop_statement.
    def visitLoop_statement(self, ctx:AdaGrammarParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#basic_loop.
    def visitBasic_loop(self, ctx:AdaGrammarParser.Basic_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#for_loop.
    def visitFor_loop(self, ctx:AdaGrammarParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#range.
    def visitRange(self, ctx:AdaGrammarParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#while_loop.
    def visitWhile_loop(self, ctx:AdaGrammarParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#simple_statement.
    def visitSimple_statement(self, ctx:AdaGrammarParser.Simple_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#procedure_call_statement.
    def visitProcedure_call_statement(self, ctx:AdaGrammarParser.Procedure_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#assignment_statement.
    def visitAssignment_statement(self, ctx:AdaGrammarParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#expression.
    def visitExpression(self, ctx:AdaGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#relation.
    def visitRelation(self, ctx:AdaGrammarParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#relational_operator.
    def visitRelational_operator(self, ctx:AdaGrammarParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#simple_expression.
    def visitSimple_expression(self, ctx:AdaGrammarParser.Simple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#unary_adding_operator.
    def visitUnary_adding_operator(self, ctx:AdaGrammarParser.Unary_adding_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#binary_adding_operator.
    def visitBinary_adding_operator(self, ctx:AdaGrammarParser.Binary_adding_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#term.
    def visitTerm(self, ctx:AdaGrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#factor.
    def visitFactor(self, ctx:AdaGrammarParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#primary.
    def visitPrimary(self, ctx:AdaGrammarParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#aggregate.
    def visitAggregate(self, ctx:AdaGrammarParser.AggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#qualified_expression.
    def visitQualified_expression(self, ctx:AdaGrammarParser.Qualified_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#function_call.
    def visitFunction_call(self, ctx:AdaGrammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#element_association.
    def visitElement_association(self, ctx:AdaGrammarParser.Element_associationContext):
        return self.visitChildren(ctx)



del AdaGrammarParser