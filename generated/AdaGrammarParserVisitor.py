# Generated from AdaGrammarParser.g4 by ANTLR 4.12.0
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


    # Visit a parse tree produced by AdaGrammarParser#package_declaration.
    def visitPackage_declaration(self, ctx:AdaGrammarParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#package_import.
    def visitPackage_import(self, ctx:AdaGrammarParser.Package_importContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#package_use.
    def visitPackage_use(self, ctx:AdaGrammarParser.Package_useContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#subprogram_declaration.
    def visitSubprogram_declaration(self, ctx:AdaGrammarParser.Subprogram_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#subprogram_specification.
    def visitSubprogram_specification(self, ctx:AdaGrammarParser.Subprogram_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#subprogram_head.
    def visitSubprogram_head(self, ctx:AdaGrammarParser.Subprogram_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#formal_part.
    def visitFormal_part(self, ctx:AdaGrammarParser.Formal_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#subprogram_body.
    def visitSubprogram_body(self, ctx:AdaGrammarParser.Subprogram_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#subunit.
    def visitSubunit(self, ctx:AdaGrammarParser.SubunitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#type_declaration.
    def visitType_declaration(self, ctx:AdaGrammarParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#type_definition.
    def visitType_definition(self, ctx:AdaGrammarParser.Type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#enumeration_type_definition.
    def visitEnumeration_type_definition(self, ctx:AdaGrammarParser.Enumeration_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#array_type_definition.
    def visitArray_type_definition(self, ctx:AdaGrammarParser.Array_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#index_subtype_definition.
    def visitIndex_subtype_definition(self, ctx:AdaGrammarParser.Index_subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#subtype_mark.
    def visitSubtype_mark(self, ctx:AdaGrammarParser.Subtype_markContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#component_subtype_definition.
    def visitComponent_subtype_definition(self, ctx:AdaGrammarParser.Component_subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#record_type_definition.
    def visitRecord_type_definition(self, ctx:AdaGrammarParser.Record_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#component_list.
    def visitComponent_list(self, ctx:AdaGrammarParser.Component_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#component_declaration.
    def visitComponent_declaration(self, ctx:AdaGrammarParser.Component_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#subtype_definition.
    def visitSubtype_definition(self, ctx:AdaGrammarParser.Subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#subtype_indication.
    def visitSubtype_indication(self, ctx:AdaGrammarParser.Subtype_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#constant_declaration.
    def visitConstant_declaration(self, ctx:AdaGrammarParser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#variable_declaration.
    def visitVariable_declaration(self, ctx:AdaGrammarParser.Variable_declarationContext):
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


    # Visit a parse tree produced by AdaGrammarParser#element_association.
    def visitElement_association(self, ctx:AdaGrammarParser.Element_associationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#qualified_expression.
    def visitQualified_expression(self, ctx:AdaGrammarParser.Qualified_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#function_call.
    def visitFunction_call(self, ctx:AdaGrammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#actual_parameter.
    def visitActual_parameter(self, ctx:AdaGrammarParser.Actual_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#assignment_statement.
    def visitAssignment_statement(self, ctx:AdaGrammarParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#target.
    def visitTarget(self, ctx:AdaGrammarParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#procedure_call_statement.
    def visitProcedure_call_statement(self, ctx:AdaGrammarParser.Procedure_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#sequence_of_statements.
    def visitSequence_of_statements(self, ctx:AdaGrammarParser.Sequence_of_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#statement.
    def visitStatement(self, ctx:AdaGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#simple_statement.
    def visitSimple_statement(self, ctx:AdaGrammarParser.Simple_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#if_statement.
    def visitIf_statement(self, ctx:AdaGrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#condition.
    def visitCondition(self, ctx:AdaGrammarParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#case_statement.
    def visitCase_statement(self, ctx:AdaGrammarParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#case_statement_alternative.
    def visitCase_statement_alternative(self, ctx:AdaGrammarParser.Case_statement_alternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#choice_list.
    def visitChoice_list(self, ctx:AdaGrammarParser.Choice_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#loop_statement.
    def visitLoop_statement(self, ctx:AdaGrammarParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#iteration_scheme.
    def visitIteration_scheme(self, ctx:AdaGrammarParser.Iteration_schemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#basic_loop.
    def visitBasic_loop(self, ctx:AdaGrammarParser.Basic_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#for_loop.
    def visitFor_loop(self, ctx:AdaGrammarParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#discrete_range.
    def visitDiscrete_range(self, ctx:AdaGrammarParser.Discrete_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#range.
    def visitRange(self, ctx:AdaGrammarParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#while_loop.
    def visitWhile_loop(self, ctx:AdaGrammarParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#begin_end_block.
    def visitBegin_end_block(self, ctx:AdaGrammarParser.Begin_end_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#exit_statement.
    def visitExit_statement(self, ctx:AdaGrammarParser.Exit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#return_statement.
    def visitReturn_statement(self, ctx:AdaGrammarParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaGrammarParser#null_statement.
    def visitNull_statement(self, ctx:AdaGrammarParser.Null_statementContext):
        return self.visitChildren(ctx)



del AdaGrammarParser