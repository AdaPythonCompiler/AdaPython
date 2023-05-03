# Generated from Ada.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AdaParser import AdaParser
else:
    from AdaParser import AdaParser

# This class defines a complete listener for a parse tree produced by AdaParser.
class AdaListener(ParseTreeListener):

    # Enter a parse tree produced by AdaParser#program.
    def enterProgram(self, ctx:AdaParser.ProgramContext):
        pass

    # Exit a parse tree produced by AdaParser#program.
    def exitProgram(self, ctx:AdaParser.ProgramContext):
        pass


    # Enter a parse tree produced by AdaParser#package_declaration.
    def enterPackage_declaration(self, ctx:AdaParser.Package_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#package_declaration.
    def exitPackage_declaration(self, ctx:AdaParser.Package_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#package_import.
    def enterPackage_import(self, ctx:AdaParser.Package_importContext):
        pass

    # Exit a parse tree produced by AdaParser#package_import.
    def exitPackage_import(self, ctx:AdaParser.Package_importContext):
        pass


    # Enter a parse tree produced by AdaParser#package_use.
    def enterPackage_use(self, ctx:AdaParser.Package_useContext):
        pass

    # Exit a parse tree produced by AdaParser#package_use.
    def exitPackage_use(self, ctx:AdaParser.Package_useContext):
        pass


    # Enter a parse tree produced by AdaParser#subprogram_declaration.
    def enterSubprogram_declaration(self, ctx:AdaParser.Subprogram_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#subprogram_declaration.
    def exitSubprogram_declaration(self, ctx:AdaParser.Subprogram_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#subprogram_specification.
    def enterSubprogram_specification(self, ctx:AdaParser.Subprogram_specificationContext):
        pass

    # Exit a parse tree produced by AdaParser#subprogram_specification.
    def exitSubprogram_specification(self, ctx:AdaParser.Subprogram_specificationContext):
        pass


    # Enter a parse tree produced by AdaParser#subprogram_head.
    def enterSubprogram_head(self, ctx:AdaParser.Subprogram_headContext):
        pass

    # Exit a parse tree produced by AdaParser#subprogram_head.
    def exitSubprogram_head(self, ctx:AdaParser.Subprogram_headContext):
        pass


    # Enter a parse tree produced by AdaParser#subprogram_body.
    def enterSubprogram_body(self, ctx:AdaParser.Subprogram_bodyContext):
        pass

    # Exit a parse tree produced by AdaParser#subprogram_body.
    def exitSubprogram_body(self, ctx:AdaParser.Subprogram_bodyContext):
        pass


    # Enter a parse tree produced by AdaParser#subunit.
    def enterSubunit(self, ctx:AdaParser.SubunitContext):
        pass

    # Exit a parse tree produced by AdaParser#subunit.
    def exitSubunit(self, ctx:AdaParser.SubunitContext):
        pass


    # Enter a parse tree produced by AdaParser#type_declaration.
    def enterType_declaration(self, ctx:AdaParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#type_declaration.
    def exitType_declaration(self, ctx:AdaParser.Type_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#type_definition.
    def enterType_definition(self, ctx:AdaParser.Type_definitionContext):
        pass

    # Exit a parse tree produced by AdaParser#type_definition.
    def exitType_definition(self, ctx:AdaParser.Type_definitionContext):
        pass


    # Enter a parse tree produced by AdaParser#enumeration_type_definition.
    def enterEnumeration_type_definition(self, ctx:AdaParser.Enumeration_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaParser#enumeration_type_definition.
    def exitEnumeration_type_definition(self, ctx:AdaParser.Enumeration_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaParser#array_type_definition.
    def enterArray_type_definition(self, ctx:AdaParser.Array_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaParser#array_type_definition.
    def exitArray_type_definition(self, ctx:AdaParser.Array_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaParser#index_subtype_definition.
    def enterIndex_subtype_definition(self, ctx:AdaParser.Index_subtype_definitionContext):
        pass

    # Exit a parse tree produced by AdaParser#index_subtype_definition.
    def exitIndex_subtype_definition(self, ctx:AdaParser.Index_subtype_definitionContext):
        pass


    # Enter a parse tree produced by AdaParser#subtype_mark.
    def enterSubtype_mark(self, ctx:AdaParser.Subtype_markContext):
        pass

    # Exit a parse tree produced by AdaParser#subtype_mark.
    def exitSubtype_mark(self, ctx:AdaParser.Subtype_markContext):
        pass


    # Enter a parse tree produced by AdaParser#component_subtype_definition.
    def enterComponent_subtype_definition(self, ctx:AdaParser.Component_subtype_definitionContext):
        pass

    # Exit a parse tree produced by AdaParser#component_subtype_definition.
    def exitComponent_subtype_definition(self, ctx:AdaParser.Component_subtype_definitionContext):
        pass


    # Enter a parse tree produced by AdaParser#record_type_definition.
    def enterRecord_type_definition(self, ctx:AdaParser.Record_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaParser#record_type_definition.
    def exitRecord_type_definition(self, ctx:AdaParser.Record_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaParser#component_list.
    def enterComponent_list(self, ctx:AdaParser.Component_listContext):
        pass

    # Exit a parse tree produced by AdaParser#component_list.
    def exitComponent_list(self, ctx:AdaParser.Component_listContext):
        pass


    # Enter a parse tree produced by AdaParser#component_declaration.
    def enterComponent_declaration(self, ctx:AdaParser.Component_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#component_declaration.
    def exitComponent_declaration(self, ctx:AdaParser.Component_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#subtype_definition.
    def enterSubtype_definition(self, ctx:AdaParser.Subtype_definitionContext):
        pass

    # Exit a parse tree produced by AdaParser#subtype_definition.
    def exitSubtype_definition(self, ctx:AdaParser.Subtype_definitionContext):
        pass


    # Enter a parse tree produced by AdaParser#subtype_indication.
    def enterSubtype_indication(self, ctx:AdaParser.Subtype_indicationContext):
        pass

    # Exit a parse tree produced by AdaParser#subtype_indication.
    def exitSubtype_indication(self, ctx:AdaParser.Subtype_indicationContext):
        pass


    # Enter a parse tree produced by AdaParser#constant_declaration.
    def enterConstant_declaration(self, ctx:AdaParser.Constant_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#constant_declaration.
    def exitConstant_declaration(self, ctx:AdaParser.Constant_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#variable_declaration.
    def enterVariable_declaration(self, ctx:AdaParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by AdaParser#variable_declaration.
    def exitVariable_declaration(self, ctx:AdaParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by AdaParser#expression.
    def enterExpression(self, ctx:AdaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AdaParser#expression.
    def exitExpression(self, ctx:AdaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AdaParser#relation.
    def enterRelation(self, ctx:AdaParser.RelationContext):
        pass

    # Exit a parse tree produced by AdaParser#relation.
    def exitRelation(self, ctx:AdaParser.RelationContext):
        pass


    # Enter a parse tree produced by AdaParser#relational_operator.
    def enterRelational_operator(self, ctx:AdaParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by AdaParser#relational_operator.
    def exitRelational_operator(self, ctx:AdaParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by AdaParser#simple_expression.
    def enterSimple_expression(self, ctx:AdaParser.Simple_expressionContext):
        pass

    # Exit a parse tree produced by AdaParser#simple_expression.
    def exitSimple_expression(self, ctx:AdaParser.Simple_expressionContext):
        pass


    # Enter a parse tree produced by AdaParser#unary_adding_operator.
    def enterUnary_adding_operator(self, ctx:AdaParser.Unary_adding_operatorContext):
        pass

    # Exit a parse tree produced by AdaParser#unary_adding_operator.
    def exitUnary_adding_operator(self, ctx:AdaParser.Unary_adding_operatorContext):
        pass


    # Enter a parse tree produced by AdaParser#binary_adding_operator.
    def enterBinary_adding_operator(self, ctx:AdaParser.Binary_adding_operatorContext):
        pass

    # Exit a parse tree produced by AdaParser#binary_adding_operator.
    def exitBinary_adding_operator(self, ctx:AdaParser.Binary_adding_operatorContext):
        pass


    # Enter a parse tree produced by AdaParser#term.
    def enterTerm(self, ctx:AdaParser.TermContext):
        pass

    # Exit a parse tree produced by AdaParser#term.
    def exitTerm(self, ctx:AdaParser.TermContext):
        pass


    # Enter a parse tree produced by AdaParser#factor.
    def enterFactor(self, ctx:AdaParser.FactorContext):
        pass

    # Exit a parse tree produced by AdaParser#factor.
    def exitFactor(self, ctx:AdaParser.FactorContext):
        pass


    # Enter a parse tree produced by AdaParser#primary.
    def enterPrimary(self, ctx:AdaParser.PrimaryContext):
        pass

    # Exit a parse tree produced by AdaParser#primary.
    def exitPrimary(self, ctx:AdaParser.PrimaryContext):
        pass


    # Enter a parse tree produced by AdaParser#aggregate.
    def enterAggregate(self, ctx:AdaParser.AggregateContext):
        pass

    # Exit a parse tree produced by AdaParser#aggregate.
    def exitAggregate(self, ctx:AdaParser.AggregateContext):
        pass


    # Enter a parse tree produced by AdaParser#element_association.
    def enterElement_association(self, ctx:AdaParser.Element_associationContext):
        pass

    # Exit a parse tree produced by AdaParser#element_association.
    def exitElement_association(self, ctx:AdaParser.Element_associationContext):
        pass


    # Enter a parse tree produced by AdaParser#qualified_expression.
    def enterQualified_expression(self, ctx:AdaParser.Qualified_expressionContext):
        pass

    # Exit a parse tree produced by AdaParser#qualified_expression.
    def exitQualified_expression(self, ctx:AdaParser.Qualified_expressionContext):
        pass


    # Enter a parse tree produced by AdaParser#function_call.
    def enterFunction_call(self, ctx:AdaParser.Function_callContext):
        pass

    # Exit a parse tree produced by AdaParser#function_call.
    def exitFunction_call(self, ctx:AdaParser.Function_callContext):
        pass


    # Enter a parse tree produced by AdaParser#actual_parameter.
    def enterActual_parameter(self, ctx:AdaParser.Actual_parameterContext):
        pass

    # Exit a parse tree produced by AdaParser#actual_parameter.
    def exitActual_parameter(self, ctx:AdaParser.Actual_parameterContext):
        pass


    # Enter a parse tree produced by AdaParser#assignment_statement.
    def enterAssignment_statement(self, ctx:AdaParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#assignment_statement.
    def exitAssignment_statement(self, ctx:AdaParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#target.
    def enterTarget(self, ctx:AdaParser.TargetContext):
        pass

    # Exit a parse tree produced by AdaParser#target.
    def exitTarget(self, ctx:AdaParser.TargetContext):
        pass


    # Enter a parse tree produced by AdaParser#procedure_call_statement.
    def enterProcedure_call_statement(self, ctx:AdaParser.Procedure_call_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#procedure_call_statement.
    def exitProcedure_call_statement(self, ctx:AdaParser.Procedure_call_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#sequence_of_statements.
    def enterSequence_of_statements(self, ctx:AdaParser.Sequence_of_statementsContext):
        pass

    # Exit a parse tree produced by AdaParser#sequence_of_statements.
    def exitSequence_of_statements(self, ctx:AdaParser.Sequence_of_statementsContext):
        pass


    # Enter a parse tree produced by AdaParser#statement.
    def enterStatement(self, ctx:AdaParser.StatementContext):
        pass

    # Exit a parse tree produced by AdaParser#statement.
    def exitStatement(self, ctx:AdaParser.StatementContext):
        pass


    # Enter a parse tree produced by AdaParser#simple_statement.
    def enterSimple_statement(self, ctx:AdaParser.Simple_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#simple_statement.
    def exitSimple_statement(self, ctx:AdaParser.Simple_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#if_statement.
    def enterIf_statement(self, ctx:AdaParser.If_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#if_statement.
    def exitIf_statement(self, ctx:AdaParser.If_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#condition.
    def enterCondition(self, ctx:AdaParser.ConditionContext):
        pass

    # Exit a parse tree produced by AdaParser#condition.
    def exitCondition(self, ctx:AdaParser.ConditionContext):
        pass


    # Enter a parse tree produced by AdaParser#case_statement.
    def enterCase_statement(self, ctx:AdaParser.Case_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#case_statement.
    def exitCase_statement(self, ctx:AdaParser.Case_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#case_statement_alternative.
    def enterCase_statement_alternative(self, ctx:AdaParser.Case_statement_alternativeContext):
        pass

    # Exit a parse tree produced by AdaParser#case_statement_alternative.
    def exitCase_statement_alternative(self, ctx:AdaParser.Case_statement_alternativeContext):
        pass


    # Enter a parse tree produced by AdaParser#choice_list.
    def enterChoice_list(self, ctx:AdaParser.Choice_listContext):
        pass

    # Exit a parse tree produced by AdaParser#choice_list.
    def exitChoice_list(self, ctx:AdaParser.Choice_listContext):
        pass


    # Enter a parse tree produced by AdaParser#loop_statement.
    def enterLoop_statement(self, ctx:AdaParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#loop_statement.
    def exitLoop_statement(self, ctx:AdaParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#iteration_scheme.
    def enterIteration_scheme(self, ctx:AdaParser.Iteration_schemeContext):
        pass

    # Exit a parse tree produced by AdaParser#iteration_scheme.
    def exitIteration_scheme(self, ctx:AdaParser.Iteration_schemeContext):
        pass


    # Enter a parse tree produced by AdaParser#basic_loop.
    def enterBasic_loop(self, ctx:AdaParser.Basic_loopContext):
        pass

    # Exit a parse tree produced by AdaParser#basic_loop.
    def exitBasic_loop(self, ctx:AdaParser.Basic_loopContext):
        pass


    # Enter a parse tree produced by AdaParser#for_loop.
    def enterFor_loop(self, ctx:AdaParser.For_loopContext):
        pass

    # Exit a parse tree produced by AdaParser#for_loop.
    def exitFor_loop(self, ctx:AdaParser.For_loopContext):
        pass


    # Enter a parse tree produced by AdaParser#discrete_range.
    def enterDiscrete_range(self, ctx:AdaParser.Discrete_rangeContext):
        pass

    # Exit a parse tree produced by AdaParser#discrete_range.
    def exitDiscrete_range(self, ctx:AdaParser.Discrete_rangeContext):
        pass


    # Enter a parse tree produced by AdaParser#range.
    def enterRange(self, ctx:AdaParser.RangeContext):
        pass

    # Exit a parse tree produced by AdaParser#range.
    def exitRange(self, ctx:AdaParser.RangeContext):
        pass


    # Enter a parse tree produced by AdaParser#while_loop.
    def enterWhile_loop(self, ctx:AdaParser.While_loopContext):
        pass

    # Exit a parse tree produced by AdaParser#while_loop.
    def exitWhile_loop(self, ctx:AdaParser.While_loopContext):
        pass


    # Enter a parse tree produced by AdaParser#begin_end_block.
    def enterBegin_end_block(self, ctx:AdaParser.Begin_end_blockContext):
        pass

    # Exit a parse tree produced by AdaParser#begin_end_block.
    def exitBegin_end_block(self, ctx:AdaParser.Begin_end_blockContext):
        pass


    # Enter a parse tree produced by AdaParser#exit_statement.
    def enterExit_statement(self, ctx:AdaParser.Exit_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#exit_statement.
    def exitExit_statement(self, ctx:AdaParser.Exit_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#return_statement.
    def enterReturn_statement(self, ctx:AdaParser.Return_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#return_statement.
    def exitReturn_statement(self, ctx:AdaParser.Return_statementContext):
        pass


    # Enter a parse tree produced by AdaParser#null_statement.
    def enterNull_statement(self, ctx:AdaParser.Null_statementContext):
        pass

    # Exit a parse tree produced by AdaParser#null_statement.
    def exitNull_statement(self, ctx:AdaParser.Null_statementContext):
        pass



del AdaParser