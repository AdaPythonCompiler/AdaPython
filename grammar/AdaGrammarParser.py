# Generated from AdaGrammar.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,53,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,4,1,28,
        8,1,11,1,12,1,29,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,53,8,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,67,8,3,10,3,12,3,70,9,3,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,86,8,6,
        10,6,12,6,89,9,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,97,8,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,0,1,6,12,0,2,4,6,8,10,12,14,16,18,20,22,0,4,1,0,34,
        35,1,0,30,33,1,0,24,25,1,0,26,27,125,0,24,1,0,0,0,2,27,1,0,0,0,4,
        38,1,0,0,0,6,52,1,0,0,0,8,71,1,0,0,0,10,76,1,0,0,0,12,82,1,0,0,0,
        14,90,1,0,0,0,16,102,1,0,0,0,18,110,1,0,0,0,20,112,1,0,0,0,22,116,
        1,0,0,0,24,25,3,2,1,0,25,1,1,0,0,0,26,28,3,4,2,0,27,26,1,0,0,0,28,
        29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,3,1,0,0,0,31,39,3,8,4,
        0,32,39,3,10,5,0,33,39,3,14,7,0,34,39,3,16,8,0,35,39,3,18,9,0,36,
        39,3,20,10,0,37,39,3,22,11,0,38,31,1,0,0,0,38,32,1,0,0,0,38,33,1,
        0,0,0,38,34,1,0,0,0,38,35,1,0,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,
        5,1,0,0,0,40,41,6,3,-1,0,41,42,5,36,0,0,42,53,3,6,3,7,43,44,5,40,
        0,0,44,45,3,6,3,0,45,46,5,41,0,0,46,53,1,0,0,0,47,53,5,23,0,0,48,
        53,5,47,0,0,49,53,5,48,0,0,50,53,5,49,0,0,51,53,5,50,0,0,52,40,1,
        0,0,0,52,43,1,0,0,0,52,47,1,0,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,
        50,1,0,0,0,52,51,1,0,0,0,53,68,1,0,0,0,54,55,10,11,0,0,55,56,7,0,
        0,0,56,67,3,6,3,12,57,58,10,10,0,0,58,59,7,1,0,0,59,67,3,6,3,11,
        60,61,10,9,0,0,61,62,7,2,0,0,62,67,3,6,3,10,63,64,10,8,0,0,64,65,
        7,3,0,0,65,67,3,6,3,9,66,54,1,0,0,0,66,57,1,0,0,0,66,60,1,0,0,0,
        66,63,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,7,1,0,
        0,0,70,68,1,0,0,0,71,72,5,23,0,0,72,73,5,28,0,0,73,74,3,6,3,0,74,
        75,5,38,0,0,75,9,1,0,0,0,76,77,5,23,0,0,77,78,5,40,0,0,78,79,3,12,
        6,0,79,80,5,41,0,0,80,81,5,38,0,0,81,11,1,0,0,0,82,87,3,6,3,0,83,
        84,5,37,0,0,84,86,3,6,3,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,
        0,0,87,88,1,0,0,0,88,13,1,0,0,0,89,87,1,0,0,0,90,91,5,4,0,0,91,92,
        3,6,3,0,92,93,5,21,0,0,93,96,3,2,1,0,94,95,5,5,0,0,95,97,3,2,1,0,
        96,94,1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,5,3,0,0,99,100,5,
        4,0,0,100,101,5,38,0,0,101,15,1,0,0,0,102,103,5,22,0,0,103,104,3,
        6,3,0,104,105,5,17,0,0,105,106,3,2,1,0,106,107,5,3,0,0,107,108,5,
        17,0,0,108,109,5,38,0,0,109,17,1,0,0,0,110,111,5,18,0,0,111,19,1,
        0,0,0,112,113,5,20,0,0,113,114,3,6,3,0,114,115,5,38,0,0,115,21,1,
        0,0,0,116,117,5,38,0,0,117,23,1,0,0,0,7,29,38,52,66,68,87,96
    ]

class AdaGrammarParser ( Parser ):

    grammarFileName = "AdaGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'begin'", "'end'", "'if'", 
                     "'else'", "'procedure'", "'function'", "'is'", "'type'", 
                     "'array'", "'of'", "'record'", "'with'", "'select'", 
                     "'when'", "'others'", "'loop'", "'exit'", "'continue'", 
                     "'return'", "'then'", "'while'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'='", "'/='", "'<'", "'>'", "'<='", 
                     "'>='", "'and'", "'or'", "'not'", "','", "';'", "':'", 
                     "'('", "')'", "'['", "']'", "'.'", "'..'", "'=>'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "BEGIN", "END", "IF", "ELSE", 
                      "PROCEDURE", "FUNCTION", "IS", "TYPE", "ARRAY", "OF", 
                      "RECORD", "WITH", "SELECT", "WHEN", "OTHERS", "LOOP", 
                      "EXIT", "CONTINUE", "RETURN", "THEN", "WHILE", "ID", 
                      "ADD", "SUB", "MUL", "DIV", "EQUALS", "NOTEQUALS", 
                      "LT", "GT", "LTE", "GTE", "AND", "OR", "NOT", "COMMA", 
                      "SEMICOLON", "COLON", "LPAREN", "RPAREN", "LEFT_BRACKET", 
                      "RIGHT_BRACKET", "PERIOD", "DOT_DOT", "ARROW", "INT", 
                      "FLOAT", "CHAR", "STRING", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_statementList = 1
    RULE_statement = 2
    RULE_expression = 3
    RULE_assignment = 4
    RULE_procedureCall = 5
    RULE_argumentList = 6
    RULE_conditionalStatement = 7
    RULE_loopStatement = 8
    RULE_exitStatement = 9
    RULE_returnStatement = 10
    RULE_nullStatement = 11

    ruleNames =  [ "program", "statementList", "statement", "expression", 
                   "assignment", "procedureCall", "argumentList", "conditionalStatement", 
                   "loopStatement", "exitStatement", "returnStatement", 
                   "nullStatement" ]

    EOF = Token.EOF
    PROGRAM=1
    BEGIN=2
    END=3
    IF=4
    ELSE=5
    PROCEDURE=6
    FUNCTION=7
    IS=8
    TYPE=9
    ARRAY=10
    OF=11
    RECORD=12
    WITH=13
    SELECT=14
    WHEN=15
    OTHERS=16
    LOOP=17
    EXIT=18
    CONTINUE=19
    RETURN=20
    THEN=21
    WHILE=22
    ID=23
    ADD=24
    SUB=25
    MUL=26
    DIV=27
    EQUALS=28
    NOTEQUALS=29
    LT=30
    GT=31
    LTE=32
    GTE=33
    AND=34
    OR=35
    NOT=36
    COMMA=37
    SEMICOLON=38
    COLON=39
    LPAREN=40
    RPAREN=41
    LEFT_BRACKET=42
    RIGHT_BRACKET=43
    PERIOD=44
    DOT_DOT=45
    ARROW=46
    INT=47
    FLOAT=48
    CHAR=49
    STRING=50
    LINE_COMMENT=51
    BLOCK_COMMENT=52
    WS=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(AdaGrammarParser.StatementListContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = AdaGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.statementList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = AdaGrammarParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.statement()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274891800592) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(AdaGrammarParser.AssignmentContext,0)


        def procedureCall(self):
            return self.getTypedRuleContext(AdaGrammarParser.ProcedureCallContext,0)


        def conditionalStatement(self):
            return self.getTypedRuleContext(AdaGrammarParser.ConditionalStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(AdaGrammarParser.LoopStatementContext,0)


        def exitStatement(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExitStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(AdaGrammarParser.ReturnStatementContext,0)


        def nullStatement(self):
            return self.getTypedRuleContext(AdaGrammarParser.NullStatementContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = AdaGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.procedureCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.conditionalStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.loopStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.exitStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 36
                self.returnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 37
                self.nullStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(AdaGrammarParser.NOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,i)


        def LPAREN(self):
            return self.getToken(AdaGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AdaGrammarParser.RPAREN, 0)

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def INT(self):
            return self.getToken(AdaGrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(AdaGrammarParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(AdaGrammarParser.CHAR, 0)

        def STRING(self):
            return self.getToken(AdaGrammarParser.STRING, 0)

        def AND(self):
            return self.getToken(AdaGrammarParser.AND, 0)

        def OR(self):
            return self.getToken(AdaGrammarParser.OR, 0)

        def LT(self):
            return self.getToken(AdaGrammarParser.LT, 0)

        def GT(self):
            return self.getToken(AdaGrammarParser.GT, 0)

        def LTE(self):
            return self.getToken(AdaGrammarParser.LTE, 0)

        def GTE(self):
            return self.getToken(AdaGrammarParser.GTE, 0)

        def ADD(self):
            return self.getToken(AdaGrammarParser.ADD, 0)

        def SUB(self):
            return self.getToken(AdaGrammarParser.SUB, 0)

        def MUL(self):
            return self.getToken(AdaGrammarParser.MUL, 0)

        def DIV(self):
            return self.getToken(AdaGrammarParser.DIV, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AdaGrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.state = 41
                self.match(AdaGrammarParser.NOT)
                self.state = 42
                self.expression(7)
                pass
            elif token in [40]:
                self.state = 43
                self.match(AdaGrammarParser.LPAREN)
                self.state = 44
                self.expression(0)
                self.state = 45
                self.match(AdaGrammarParser.RPAREN)
                pass
            elif token in [23]:
                self.state = 47
                self.match(AdaGrammarParser.ID)
                pass
            elif token in [47]:
                self.state = 48
                self.match(AdaGrammarParser.INT)
                pass
            elif token in [48]:
                self.state = 49
                self.match(AdaGrammarParser.FLOAT)
                pass
            elif token in [49]:
                self.state = 50
                self.match(AdaGrammarParser.CHAR)
                pass
            elif token in [50]:
                self.state = 51
                self.match(AdaGrammarParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = AdaGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 55
                        _la = self._input.LA(1)
                        if not(_la==34 or _la==35):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = AdaGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 58
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.expression(11)
                        pass

                    elif la_ == 3:
                        localctx = AdaGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 60
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 61
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        self.expression(10)
                        pass

                    elif la_ == 4:
                        localctx = AdaGrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 63
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 64
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        self.expression(9)
                        pass

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def EQUALS(self):
            return self.getToken(AdaGrammarParser.EQUALS, 0)

        def expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = AdaGrammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(AdaGrammarParser.ID)
            self.state = 72
            self.match(AdaGrammarParser.EQUALS)
            self.state = 73
            self.expression(0)
            self.state = 74
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def LPAREN(self):
            return self.getToken(AdaGrammarParser.LPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(AdaGrammarParser.ArgumentListContext,0)


        def RPAREN(self):
            return self.getToken(AdaGrammarParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_procedureCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedureCall" ):
                listener.enterProcedureCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedureCall" ):
                listener.exitProcedureCall(self)




    def procedureCall(self):

        localctx = AdaGrammarParser.ProcedureCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_procedureCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(AdaGrammarParser.ID)
            self.state = 77
            self.match(AdaGrammarParser.LPAREN)
            self.state = 78
            self.argumentList()
            self.state = 79
            self.match(AdaGrammarParser.RPAREN)
            self.state = 80
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.COMMA)
            else:
                return self.getToken(AdaGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = AdaGrammarParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.expression(0)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 83
                self.match(AdaGrammarParser.COMMA)
                self.state = 84
                self.expression(0)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.IF)
            else:
                return self.getToken(AdaGrammarParser.IF, i)

        def expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(AdaGrammarParser.THEN, 0)

        def statementList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.StatementListContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.StatementListContext,i)


        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def ELSE(self):
            return self.getToken(AdaGrammarParser.ELSE, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_conditionalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalStatement" ):
                listener.enterConditionalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalStatement" ):
                listener.exitConditionalStatement(self)




    def conditionalStatement(self):

        localctx = AdaGrammarParser.ConditionalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditionalStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(AdaGrammarParser.IF)
            self.state = 91
            self.expression(0)
            self.state = 92
            self.match(AdaGrammarParser.THEN)
            self.state = 93
            self.statementList()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 94
                self.match(AdaGrammarParser.ELSE)
                self.state = 95
                self.statementList()


            self.state = 98
            self.match(AdaGrammarParser.END)
            self.state = 99
            self.match(AdaGrammarParser.IF)
            self.state = 100
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(AdaGrammarParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,0)


        def LOOP(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.LOOP)
            else:
                return self.getToken(AdaGrammarParser.LOOP, i)

        def statementList(self):
            return self.getTypedRuleContext(AdaGrammarParser.StatementListContext,0)


        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)




    def loopStatement(self):

        localctx = AdaGrammarParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(AdaGrammarParser.WHILE)
            self.state = 103
            self.expression(0)
            self.state = 104
            self.match(AdaGrammarParser.LOOP)
            self.state = 105
            self.statementList()
            self.state = 106
            self.match(AdaGrammarParser.END)
            self.state = 107
            self.match(AdaGrammarParser.LOOP)
            self.state = 108
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExitStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXIT(self):
            return self.getToken(AdaGrammarParser.EXIT, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_exitStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExitStatement" ):
                listener.enterExitStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExitStatement" ):
                listener.exitExitStatement(self)




    def exitStatement(self):

        localctx = AdaGrammarParser.ExitStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exitStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(AdaGrammarParser.EXIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(AdaGrammarParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = AdaGrammarParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(AdaGrammarParser.RETURN)
            self.state = 113
            self.expression(0)
            self.state = 114
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_nullStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullStatement" ):
                listener.enterNullStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullStatement" ):
                listener.exitNullStatement(self)




    def nullStatement(self):

        localctx = AdaGrammarParser.NullStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_nullStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




