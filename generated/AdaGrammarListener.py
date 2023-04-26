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


    # Enter a parse tree produced by AdaGrammarParser#package_declaration.
    def enterPackage_declaration(self, ctx:AdaGrammarParser.Package_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#package_declaration.
    def exitPackage_declaration(self, ctx:AdaGrammarParser.Package_declarationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#subprogram_declaration.
    def enterSubprogram_declaration(self, ctx:AdaGrammarParser.Subprogram_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#subprogram_declaration.
    def exitSubprogram_declaration(self, ctx:AdaGrammarParser.Subprogram_declarationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#subprogram_specification.
    def enterSubprogram_specification(self, ctx:AdaGrammarParser.Subprogram_specificationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#subprogram_specification.
    def exitSubprogram_specification(self, ctx:AdaGrammarParser.Subprogram_specificationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#subprogram_head.
    def enterSubprogram_head(self, ctx:AdaGrammarParser.Subprogram_headContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#subprogram_head.
    def exitSubprogram_head(self, ctx:AdaGrammarParser.Subprogram_headContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#formal_part.
    def enterFormal_part(self, ctx:AdaGrammarParser.Formal_partContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#formal_part.
    def exitFormal_part(self, ctx:AdaGrammarParser.Formal_partContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#subprogram_body.
    def enterSubprogram_body(self, ctx:AdaGrammarParser.Subprogram_bodyContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#subprogram_body.
    def exitSubprogram_body(self, ctx:AdaGrammarParser.Subprogram_bodyContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#task_declaration.
    def enterTask_declaration(self, ctx:AdaGrammarParser.Task_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#task_declaration.
    def exitTask_declaration(self, ctx:AdaGrammarParser.Task_declarationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#task_body.
    def enterTask_body(self, ctx:AdaGrammarParser.Task_bodyContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#task_body.
    def exitTask_body(self, ctx:AdaGrammarParser.Task_bodyContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#protected_type_declaration.
    def enterProtected_type_declaration(self, ctx:AdaGrammarParser.Protected_type_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#protected_type_declaration.
    def exitProtected_type_declaration(self, ctx:AdaGrammarParser.Protected_type_declarationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#protected_type_body.
    def enterProtected_type_body(self, ctx:AdaGrammarParser.Protected_type_bodyContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#protected_type_body.
    def exitProtected_type_body(self, ctx:AdaGrammarParser.Protected_type_bodyContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#subunit.
    def enterSubunit(self, ctx:AdaGrammarParser.SubunitContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#subunit.
    def exitSubunit(self, ctx:AdaGrammarParser.SubunitContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#type_declaration.
    def enterType_declaration(self, ctx:AdaGrammarParser.Type_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#type_declaration.
    def exitType_declaration(self, ctx:AdaGrammarParser.Type_declarationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#type_definition.
    def enterType_definition(self, ctx:AdaGrammarParser.Type_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#type_definition.
    def exitType_definition(self, ctx:AdaGrammarParser.Type_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#enumeration_type_definition.
    def enterEnumeration_type_definition(self, ctx:AdaGrammarParser.Enumeration_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#enumeration_type_definition.
    def exitEnumeration_type_definition(self, ctx:AdaGrammarParser.Enumeration_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#array_type_definition.
    def enterArray_type_definition(self, ctx:AdaGrammarParser.Array_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#array_type_definition.
    def exitArray_type_definition(self, ctx:AdaGrammarParser.Array_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#index_subtype_definition.
    def enterIndex_subtype_definition(self, ctx:AdaGrammarParser.Index_subtype_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#index_subtype_definition.
    def exitIndex_subtype_definition(self, ctx:AdaGrammarParser.Index_subtype_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#subtype_mark.
    def enterSubtype_mark(self, ctx:AdaGrammarParser.Subtype_markContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#subtype_mark.
    def exitSubtype_mark(self, ctx:AdaGrammarParser.Subtype_markContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#component_subtype_definition.
    def enterComponent_subtype_definition(self, ctx:AdaGrammarParser.Component_subtype_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#component_subtype_definition.
    def exitComponent_subtype_definition(self, ctx:AdaGrammarParser.Component_subtype_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#record_type_definition.
    def enterRecord_type_definition(self, ctx:AdaGrammarParser.Record_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#record_type_definition.
    def exitRecord_type_definition(self, ctx:AdaGrammarParser.Record_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#component_list.
    def enterComponent_list(self, ctx:AdaGrammarParser.Component_listContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#component_list.
    def exitComponent_list(self, ctx:AdaGrammarParser.Component_listContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#component_declaration.
    def enterComponent_declaration(self, ctx:AdaGrammarParser.Component_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#component_declaration.
    def exitComponent_declaration(self, ctx:AdaGrammarParser.Component_declarationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#access_type_definition.
    def enterAccess_type_definition(self, ctx:AdaGrammarParser.Access_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#access_type_definition.
    def exitAccess_type_definition(self, ctx:AdaGrammarParser.Access_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#protected_type_definition.
    def enterProtected_type_definition(self, ctx:AdaGrammarParser.Protected_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#protected_type_definition.
    def exitProtected_type_definition(self, ctx:AdaGrammarParser.Protected_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#tagged_type_definition.
    def enterTagged_type_definition(self, ctx:AdaGrammarParser.Tagged_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#tagged_type_definition.
    def exitTagged_type_definition(self, ctx:AdaGrammarParser.Tagged_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#limited_type_definition.
    def enterLimited_type_definition(self, ctx:AdaGrammarParser.Limited_type_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#limited_type_definition.
    def exitLimited_type_definition(self, ctx:AdaGrammarParser.Limited_type_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#subtype_definition.
    def enterSubtype_definition(self, ctx:AdaGrammarParser.Subtype_definitionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#subtype_definition.
    def exitSubtype_definition(self, ctx:AdaGrammarParser.Subtype_definitionContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#subtype_indication.
    def enterSubtype_indication(self, ctx:AdaGrammarParser.Subtype_indicationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#subtype_indication.
    def exitSubtype_indication(self, ctx:AdaGrammarParser.Subtype_indicationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#constant_declaration.
    def enterConstant_declaration(self, ctx:AdaGrammarParser.Constant_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#constant_declaration.
    def exitConstant_declaration(self, ctx:AdaGrammarParser.Constant_declarationContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#variable_declaration.
    def enterVariable_declaration(self, ctx:AdaGrammarParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#variable_declaration.
    def exitVariable_declaration(self, ctx:AdaGrammarParser.Variable_declarationContext):
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


    # Enter a parse tree produced by AdaGrammarParser#element_association.
    def enterElement_association(self, ctx:AdaGrammarParser.Element_associationContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#element_association.
    def exitElement_association(self, ctx:AdaGrammarParser.Element_associationContext):
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


    # Enter a parse tree produced by AdaGrammarParser#actual_parameter.
    def enterActual_parameter(self, ctx:AdaGrammarParser.Actual_parameterContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#actual_parameter.
    def exitActual_parameter(self, ctx:AdaGrammarParser.Actual_parameterContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#assignment_statement.
    def enterAssignment_statement(self, ctx:AdaGrammarParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#assignment_statement.
    def exitAssignment_statement(self, ctx:AdaGrammarParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#target.
    def enterTarget(self, ctx:AdaGrammarParser.TargetContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#target.
    def exitTarget(self, ctx:AdaGrammarParser.TargetContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#procedure_call_statement.
    def enterProcedure_call_statement(self, ctx:AdaGrammarParser.Procedure_call_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#procedure_call_statement.
    def exitProcedure_call_statement(self, ctx:AdaGrammarParser.Procedure_call_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#sequence_of_statements.
    def enterSequence_of_statements(self, ctx:AdaGrammarParser.Sequence_of_statementsContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#sequence_of_statements.
    def exitSequence_of_statements(self, ctx:AdaGrammarParser.Sequence_of_statementsContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#statement.
    def enterStatement(self, ctx:AdaGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#statement.
    def exitStatement(self, ctx:AdaGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#simple_statement.
    def enterSimple_statement(self, ctx:AdaGrammarParser.Simple_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#simple_statement.
    def exitSimple_statement(self, ctx:AdaGrammarParser.Simple_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#if_statement.
    def enterIf_statement(self, ctx:AdaGrammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#if_statement.
    def exitIf_statement(self, ctx:AdaGrammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#condition.
    def enterCondition(self, ctx:AdaGrammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#condition.
    def exitCondition(self, ctx:AdaGrammarParser.ConditionContext):
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


    # Enter a parse tree produced by AdaGrammarParser#choice_list.
    def enterChoice_list(self, ctx:AdaGrammarParser.Choice_listContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#choice_list.
    def exitChoice_list(self, ctx:AdaGrammarParser.Choice_listContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#loop_statement.
    def enterLoop_statement(self, ctx:AdaGrammarParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#loop_statement.
    def exitLoop_statement(self, ctx:AdaGrammarParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#iteration_scheme.
    def enterIteration_scheme(self, ctx:AdaGrammarParser.Iteration_schemeContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#iteration_scheme.
    def exitIteration_scheme(self, ctx:AdaGrammarParser.Iteration_schemeContext):
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


    # Enter a parse tree produced by AdaGrammarParser#discrete_range.
    def enterDiscrete_range(self, ctx:AdaGrammarParser.Discrete_rangeContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#discrete_range.
    def exitDiscrete_range(self, ctx:AdaGrammarParser.Discrete_rangeContext):
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


    # Enter a parse tree produced by AdaGrammarParser#begin_end_block.
    def enterBegin_end_block(self, ctx:AdaGrammarParser.Begin_end_blockContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#begin_end_block.
    def exitBegin_end_block(self, ctx:AdaGrammarParser.Begin_end_blockContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#exit_statement.
    def enterExit_statement(self, ctx:AdaGrammarParser.Exit_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#exit_statement.
    def exitExit_statement(self, ctx:AdaGrammarParser.Exit_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#return_statement.
    def enterReturn_statement(self, ctx:AdaGrammarParser.Return_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#return_statement.
    def exitReturn_statement(self, ctx:AdaGrammarParser.Return_statementContext):
        pass


    # Enter a parse tree produced by AdaGrammarParser#null_statement.
    def enterNull_statement(self, ctx:AdaGrammarParser.Null_statementContext):
        pass

    # Exit a parse tree produced by AdaGrammarParser#null_statement.
    def exitNull_statement(self, ctx:AdaGrammarParser.Null_statementContext):
        pass



del AdaGrammarParser