# Generated from Ada.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AdaParser import AdaParser
else:
    from AdaParser import AdaParser

# This class defines a complete generic visitor for a parse tree produced by AdaParser.

class AdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AdaParser#program.
    def visitProgram(self, ctx:AdaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#package_declaration.
    def visitPackage_declaration(self, ctx:AdaParser.Package_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#package_import.
    def visitPackage_import(self, ctx:AdaParser.Package_importContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#package_use.
    def visitPackage_use(self, ctx:AdaParser.Package_useContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subprogram_declaration.
    def visitSubprogram_declaration(self, ctx:AdaParser.Subprogram_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subprogram_specification.
    def visitSubprogram_specification(self, ctx:AdaParser.Subprogram_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subprogram_head.
    def visitSubprogram_head(self, ctx:AdaParser.Subprogram_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subprogram_body.
    def visitSubprogram_body(self, ctx:AdaParser.Subprogram_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subunit.
    def visitSubunit(self, ctx:AdaParser.SubunitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#type_declaration.
    def visitType_declaration(self, ctx:AdaParser.Type_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#type_definition.
    def visitType_definition(self, ctx:AdaParser.Type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#enumeration_type_definition.
    def visitEnumeration_type_definition(self, ctx:AdaParser.Enumeration_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#array_type_definition.
    def visitArray_type_definition(self, ctx:AdaParser.Array_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#index_subtype_definition.
    def visitIndex_subtype_definition(self, ctx:AdaParser.Index_subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subtype_mark.
    def visitSubtype_mark(self, ctx:AdaParser.Subtype_markContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#component_subtype_definition.
    def visitComponent_subtype_definition(self, ctx:AdaParser.Component_subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#record_type_definition.
    def visitRecord_type_definition(self, ctx:AdaParser.Record_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#component_list.
    def visitComponent_list(self, ctx:AdaParser.Component_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#component_declaration.
    def visitComponent_declaration(self, ctx:AdaParser.Component_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subtype_definition.
    def visitSubtype_definition(self, ctx:AdaParser.Subtype_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#subtype_indication.
    def visitSubtype_indication(self, ctx:AdaParser.Subtype_indicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#constant_declaration.
    def visitConstant_declaration(self, ctx:AdaParser.Constant_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#variable_declaration.
    def visitVariable_declaration(self, ctx:AdaParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#expression.
    def visitExpression(self, ctx:AdaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#relation.
    def visitRelation(self, ctx:AdaParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#relational_operator.
    def visitRelational_operator(self, ctx:AdaParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#simple_expression.
    def visitSimple_expression(self, ctx:AdaParser.Simple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#unary_adding_operator.
    def visitUnary_adding_operator(self, ctx:AdaParser.Unary_adding_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#binary_adding_operator.
    def visitBinary_adding_operator(self, ctx:AdaParser.Binary_adding_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#term.
    def visitTerm(self, ctx:AdaParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#factor.
    def visitFactor(self, ctx:AdaParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#primary.
    def visitPrimary(self, ctx:AdaParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#aggregate.
    def visitAggregate(self, ctx:AdaParser.AggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#element_association.
    def visitElement_association(self, ctx:AdaParser.Element_associationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#qualified_expression.
    def visitQualified_expression(self, ctx:AdaParser.Qualified_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#function_call.
    def visitFunction_call(self, ctx:AdaParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#actual_parameter.
    def visitActual_parameter(self, ctx:AdaParser.Actual_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#assignment_statement.
    def visitAssignment_statement(self, ctx:AdaParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#target.
    def visitTarget(self, ctx:AdaParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#procedure_call_statement.
    def visitProcedure_call_statement(self, ctx:AdaParser.Procedure_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#sequence_of_statements.
    def visitSequence_of_statements(self, ctx:AdaParser.Sequence_of_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#statement.
    def visitStatement(self, ctx:AdaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#simple_statement.
    def visitSimple_statement(self, ctx:AdaParser.Simple_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#if_statement.
    def visitIf_statement(self, ctx:AdaParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#condition.
    def visitCondition(self, ctx:AdaParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#case_statement.
    def visitCase_statement(self, ctx:AdaParser.Case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#case_statement_alternative.
    def visitCase_statement_alternative(self, ctx:AdaParser.Case_statement_alternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#choice_list.
    def visitChoice_list(self, ctx:AdaParser.Choice_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#loop_statement.
    def visitLoop_statement(self, ctx:AdaParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#iteration_scheme.
    def visitIteration_scheme(self, ctx:AdaParser.Iteration_schemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#basic_loop.
    def visitBasic_loop(self, ctx:AdaParser.Basic_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#for_loop.
    def visitFor_loop(self, ctx:AdaParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#discrete_range.
    def visitDiscrete_range(self, ctx:AdaParser.Discrete_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#range.
    def visitRange(self, ctx:AdaParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#while_loop.
    def visitWhile_loop(self, ctx:AdaParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#begin_end_block.
    def visitBegin_end_block(self, ctx:AdaParser.Begin_end_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#exit_statement.
    def visitExit_statement(self, ctx:AdaParser.Exit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#return_statement.
    def visitReturn_statement(self, ctx:AdaParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AdaParser#null_statement.
    def visitNull_statement(self, ctx:AdaParser.Null_statementContext):
        return self.visitChildren(ctx)



del AdaParser