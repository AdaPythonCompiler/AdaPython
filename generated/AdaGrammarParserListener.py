# Generated from AdaGrammarParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AdaGrammarParser import AdaGrammarParser
else:
    from AdaGrammarParser import AdaGrammarParser

# This class defines a complete listener for a parse tree produced by AdaGrammarParser.
class AdaGrammarParserListener(ParseTreeListener):

    # Enter a parse tree produced by AdaGrammarParser#program.
    def enterProgram(self, ctx:AdaGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#program.
    def exitProgram(self, ctx:AdaGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#package_import.
    def enterPackage_import(self, ctx:AdaGrammarParser.Package_importContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#package_import.
    def exitPackage_import(self, ctx:AdaGrammarParser.Package_importContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#package_use.
    def enterPackage_use(self, ctx:AdaGrammarParser.Package_useContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#package_use.
    def exitPackage_use(self, ctx:AdaGrammarParser.Package_useContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#program_declaration.
    def enterProgram_declaration(self, ctx:AdaGrammarParser.Program_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#program_declaration.
    def exitProgram_declaration(self, ctx:AdaGrammarParser.Program_declarationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#program_head.
    def enterProgram_head(self, ctx:AdaGrammarParser.Program_headContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#program_head.
    def exitProgram_head(self, ctx:AdaGrammarParser.Program_headContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#input_vars.
    def enterInput_vars(self, ctx:AdaGrammarParser.Input_varsContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#input_vars.
    def exitInput_vars(self, ctx:AdaGrammarParser.Input_varsContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#variable_declaration.
    def enterVariable_declaration(self, ctx:AdaGrammarParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#variable_declaration.
    def exitVariable_declaration(self, ctx:AdaGrammarParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#full_variable_declaration.
    def enterFull_variable_declaration(self, ctx:AdaGrammarParser.Full_variable_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#full_variable_declaration.
    def exitFull_variable_declaration(self, ctx:AdaGrammarParser.Full_variable_declarationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#type.
    def enterType(self, ctx:AdaGrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#type.
    def exitType(self, ctx:AdaGrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#begin_end_block.
    def enterBegin_end_block(self, ctx:AdaGrammarParser.Begin_end_blockContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#begin_end_block.
    def exitBegin_end_block(self, ctx:AdaGrammarParser.Begin_end_blockContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#statement.
    def enterStatement(self, ctx:AdaGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#statement.
    def exitStatement(self, ctx:AdaGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#if_statement.
    def enterIf_statement(self, ctx:AdaGrammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#if_statement.
    def exitIf_statement(self, ctx:AdaGrammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#elsif_statement.
    def enterElsif_statement(self, ctx:AdaGrammarParser.Elsif_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#elsif_statement.
    def exitElsif_statement(self, ctx:AdaGrammarParser.Elsif_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#else_statement.
    def enterElse_statement(self, ctx:AdaGrammarParser.Else_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#else_statement.
    def exitElse_statement(self, ctx:AdaGrammarParser.Else_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#loop_statement.
    def enterLoop_statement(self, ctx:AdaGrammarParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#loop_statement.
    def exitLoop_statement(self, ctx:AdaGrammarParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#basic_loop.
    def enterBasic_loop(self, ctx:AdaGrammarParser.Basic_loopContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#basic_loop.
    def exitBasic_loop(self, ctx:AdaGrammarParser.Basic_loopContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#for_loop.
    def enterFor_loop(self, ctx:AdaGrammarParser.For_loopContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#for_loop.
    def exitFor_loop(self, ctx:AdaGrammarParser.For_loopContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#range.
    def enterRange(self, ctx:AdaGrammarParser.RangeContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#range.
    def exitRange(self, ctx:AdaGrammarParser.RangeContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#while_loop.
    def enterWhile_loop(self, ctx:AdaGrammarParser.While_loopContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#while_loop.
    def exitWhile_loop(self, ctx:AdaGrammarParser.While_loopContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#case_statement.
    def enterCase_statement(self, ctx:AdaGrammarParser.Case_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#case_statement.
    def exitCase_statement(self, ctx:AdaGrammarParser.Case_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#case_statement_alternative.
    def enterCase_statement_alternative(self, ctx:AdaGrammarParser.Case_statement_alternativeContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#case_statement_alternative.
    def exitCase_statement_alternative(self, ctx:AdaGrammarParser.Case_statement_alternativeContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#simple_statement.
    def enterSimple_statement(self, ctx:AdaGrammarParser.Simple_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#simple_statement.
    def exitSimple_statement(self, ctx:AdaGrammarParser.Simple_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#procedure_call_statement.
    def enterProcedure_call_statement(self, ctx:AdaGrammarParser.Procedure_call_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#procedure_call_statement.
    def exitProcedure_call_statement(self, ctx:AdaGrammarParser.Procedure_call_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#assignment_statement.
    def enterAssignment_statement(self, ctx:AdaGrammarParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#assignment_statement.
    def exitAssignment_statement(self, ctx:AdaGrammarParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#expression.
    def enterExpression(self, ctx:AdaGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#expression.
    def exitExpression(self, ctx:AdaGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#relation.
    def enterRelation(self, ctx:AdaGrammarParser.RelationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#relation.
    def exitRelation(self, ctx:AdaGrammarParser.RelationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#relational_operator.
    def enterRelational_operator(self, ctx:AdaGrammarParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#relational_operator.
    def exitRelational_operator(self, ctx:AdaGrammarParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#simple_expression.
    def enterSimple_expression(self, ctx:AdaGrammarParser.Simple_expressionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#simple_expression.
    def exitSimple_expression(self, ctx:AdaGrammarParser.Simple_expressionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#unary_adding_operator.
    def enterUnary_adding_operator(self, ctx:AdaGrammarParser.Unary_adding_operatorContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#unary_adding_operator.
    def exitUnary_adding_operator(self, ctx:AdaGrammarParser.Unary_adding_operatorContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#binary_adding_operator.
    def enterBinary_adding_operator(self, ctx:AdaGrammarParser.Binary_adding_operatorContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#binary_adding_operator.
    def exitBinary_adding_operator(self, ctx:AdaGrammarParser.Binary_adding_operatorContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#term.
    def enterTerm(self, ctx:AdaGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#term.
    def exitTerm(self, ctx:AdaGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#factor.
    def enterFactor(self, ctx:AdaGrammarParser.FactorContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#factor.
    def exitFactor(self, ctx:AdaGrammarParser.FactorContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#primary.
    def enterPrimary(self, ctx:AdaGrammarParser.PrimaryContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#primary.
    def exitPrimary(self, ctx:AdaGrammarParser.PrimaryContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#aggregate.
    def enterAggregate(self, ctx:AdaGrammarParser.AggregateContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#aggregate.
    def exitAggregate(self, ctx:AdaGrammarParser.AggregateContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#qualified_expression.
    def enterQualified_expression(self, ctx:AdaGrammarParser.Qualified_expressionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#qualified_expression.
    def exitQualified_expression(self, ctx:AdaGrammarParser.Qualified_expressionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#function_call.
    def enterFunction_call(self, ctx:AdaGrammarParser.Function_callContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#function_call.
    def exitFunction_call(self, ctx:AdaGrammarParser.Function_callContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#element_association.
    def enterElement_association(self, ctx:AdaGrammarParser.Element_associationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#element_association.
    def exitElement_association(self, ctx:AdaGrammarParser.Element_associationContext):
        pass



del AdaGrammarParser