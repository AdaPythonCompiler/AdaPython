# Generated from Ada.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AdaParser import AdaParser
else:
    from AdaParser import AdaParser

# This class defines a complete listener for a parse tree produced by AdaParser.
class AdaListener(ParseTreeListener):

    # Enter a parse tree produced by AdaParser#prog.
    def enterProg(self, ctx:AdaParser.ProgContext):
        pass

    # Exit a parse tree produced by AdaParser#prog.
    def exitProg(self, ctx:AdaParser.ProgContext):
        pass


    # Enter a parse tree produced by AdaParser#stmt.
    def enterStmt(self, ctx:AdaParser.StmtContext):
        pass

    # Exit a parse tree produced by AdaParser#stmt.
    def exitStmt(self, ctx:AdaParser.StmtContext):
        pass


    # Enter a parse tree produced by AdaParser#assignment.
    def enterAssignment(self, ctx:AdaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by AdaParser#assignment.
    def exitAssignment(self, ctx:AdaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by AdaParser#if_stmt.
    def enterIf_stmt(self, ctx:AdaParser.If_stmtContext):
        pass

    # Exit a parse tree produced by AdaParser#if_stmt.
    def exitIf_stmt(self, ctx:AdaParser.If_stmtContext):
        pass


    # Enter a parse tree produced by AdaParser#loop_stmt.
    def enterLoop_stmt(self, ctx:AdaParser.Loop_stmtContext):
        pass

    # Exit a parse tree produced by AdaParser#loop_stmt.
    def exitLoop_stmt(self, ctx:AdaParser.Loop_stmtContext):
        pass


    # Enter a parse tree produced by AdaParser#exit_stmt.
    def enterExit_stmt(self, ctx:AdaParser.Exit_stmtContext):
        pass

    # Exit a parse tree produced by AdaParser#exit_stmt.
    def exitExit_stmt(self, ctx:AdaParser.Exit_stmtContext):
        pass


    # Enter a parse tree produced by AdaParser#return_stmt.
    def enterReturn_stmt(self, ctx:AdaParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by AdaParser#return_stmt.
    def exitReturn_stmt(self, ctx:AdaParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by AdaParser#proc_call.
    def enterProc_call(self, ctx:AdaParser.Proc_callContext):
        pass

    # Exit a parse tree produced by AdaParser#proc_call.
    def exitProc_call(self, ctx:AdaParser.Proc_callContext):
        pass


    # Enter a parse tree produced by AdaParser#proc_def.
    def enterProc_def(self, ctx:AdaParser.Proc_defContext):
        pass

    # Exit a parse tree produced by AdaParser#proc_def.
    def exitProc_def(self, ctx:AdaParser.Proc_defContext):
        pass


    # Enter a parse tree produced by AdaParser#param.
    def enterParam(self, ctx:AdaParser.ParamContext):
        pass

    # Exit a parse tree produced by AdaParser#param.
    def exitParam(self, ctx:AdaParser.ParamContext):
        pass


    # Enter a parse tree produced by AdaParser#param_type.
    def enterParam_type(self, ctx:AdaParser.Param_typeContext):
        pass

    # Exit a parse tree produced by AdaParser#param_type.
    def exitParam_type(self, ctx:AdaParser.Param_typeContext):
        pass


    # Enter a parse tree produced by AdaParser#type_def.
    def enterType_def(self, ctx:AdaParser.Type_defContext):
        pass

    # Exit a parse tree produced by AdaParser#type_def.
    def exitType_def(self, ctx:AdaParser.Type_defContext):
        pass


    # Enter a parse tree produced by AdaParser#type_decl.
    def enterType_decl(self, ctx:AdaParser.Type_declContext):
        pass

    # Exit a parse tree produced by AdaParser#type_decl.
    def exitType_decl(self, ctx:AdaParser.Type_declContext):
        pass


    # Enter a parse tree produced by AdaParser#scalar_type.
    def enterScalar_type(self, ctx:AdaParser.Scalar_typeContext):
        pass

    # Exit a parse tree produced by AdaParser#scalar_type.
    def exitScalar_type(self, ctx:AdaParser.Scalar_typeContext):
        pass


    # Enter a parse tree produced by AdaParser#array_type.
    def enterArray_type(self, ctx:AdaParser.Array_typeContext):
        pass

    # Exit a parse tree produced by AdaParser#array_type.
    def exitArray_type(self, ctx:AdaParser.Array_typeContext):
        pass


    # Enter a parse tree produced by AdaParser#index_spec.
    def enterIndex_spec(self, ctx:AdaParser.Index_specContext):
        pass

    # Exit a parse tree produced by AdaParser#index_spec.
    def exitIndex_spec(self, ctx:AdaParser.Index_specContext):
        pass


    # Enter a parse tree produced by AdaParser#discrete_range.
    def enterDiscrete_range(self, ctx:AdaParser.Discrete_rangeContext):
        pass

    # Exit a parse tree produced by AdaParser#discrete_range.
    def exitDiscrete_range(self, ctx:AdaParser.Discrete_rangeContext):
        pass


    # Enter a parse tree produced by AdaParser#expr.
    def enterExpr(self, ctx:AdaParser.ExprContext):
        pass

    # Exit a parse tree produced by AdaParser#expr.
    def exitExpr(self, ctx:AdaParser.ExprContext):
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


    # Enter a parse tree produced by AdaParser#bool_expr.
    def enterBool_expr(self, ctx:AdaParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by AdaParser#bool_expr.
    def exitBool_expr(self, ctx:AdaParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by AdaParser#bool_term.
    def enterBool_term(self, ctx:AdaParser.Bool_termContext):
        pass

    # Exit a parse tree produced by AdaParser#bool_term.
    def exitBool_term(self, ctx:AdaParser.Bool_termContext):
        pass


    # Enter a parse tree produced by AdaParser#bool_factor.
    def enterBool_factor(self, ctx:AdaParser.Bool_factorContext):
        pass

    # Exit a parse tree produced by AdaParser#bool_factor.
    def exitBool_factor(self, ctx:AdaParser.Bool_factorContext):
        pass



del AdaParser