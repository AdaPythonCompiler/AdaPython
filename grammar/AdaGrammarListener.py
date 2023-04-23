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



del AdaGrammarParser