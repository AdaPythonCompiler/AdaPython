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
        4,1,103,330,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,65,8,0,10,0,12,
        0,68,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,81,8,1,
        10,1,12,1,84,9,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,5,3,103,8,3,10,3,12,3,106,9,3,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,3,4,115,8,4,1,4,1,4,1,4,3,4,120,8,4,1,4,1,4,3,4,124,
        8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,134,8,5,10,5,12,5,137,9,
        5,3,5,139,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,
        6,153,8,6,10,6,12,6,156,9,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,5,7,172,8,7,10,7,12,7,175,9,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,190,8,8,10,8,12,8,193,
        9,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        5,9,210,8,9,10,9,12,9,213,9,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,5,10,228,8,10,10,10,12,10,231,9,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,243,8,11,1,12,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        3,13,259,8,13,1,14,1,14,1,14,1,14,5,14,265,8,14,10,14,12,14,268,
        9,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,5,15,277,8,15,10,15,12,15,
        280,9,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,18,
        1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,5,20,302,8,20,10,20,
        12,20,305,9,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,
        1,24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,27,1,27,1,27,3,27,328,
        8,27,1,27,0,0,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,0,0,382,0,66,1,0,0,0,2,69,1,0,0,0,
        4,89,1,0,0,0,6,92,1,0,0,0,8,123,1,0,0,0,10,125,1,0,0,0,12,142,1,
        0,0,0,14,161,1,0,0,0,16,180,1,0,0,0,18,198,1,0,0,0,20,218,1,0,0,
        0,22,242,1,0,0,0,24,244,1,0,0,0,26,258,1,0,0,0,28,260,1,0,0,0,30,
        271,1,0,0,0,32,285,1,0,0,0,34,289,1,0,0,0,36,291,1,0,0,0,38,293,
        1,0,0,0,40,298,1,0,0,0,42,306,1,0,0,0,44,310,1,0,0,0,46,313,1,0,
        0,0,48,316,1,0,0,0,50,319,1,0,0,0,52,322,1,0,0,0,54,324,1,0,0,0,
        56,65,3,2,1,0,57,65,3,4,2,0,58,65,3,12,6,0,59,65,3,14,7,0,60,65,
        3,16,8,0,61,65,3,18,9,0,62,65,3,20,10,0,63,65,3,22,11,0,64,56,1,
        0,0,0,64,57,1,0,0,0,64,58,1,0,0,0,64,59,1,0,0,0,64,60,1,0,0,0,64,
        61,1,0,0,0,64,62,1,0,0,0,64,63,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,
        0,66,67,1,0,0,0,67,1,1,0,0,0,68,66,1,0,0,0,69,70,5,45,0,0,70,71,
        5,74,0,0,71,82,5,33,0,0,72,81,3,2,1,0,73,81,3,4,2,0,74,81,3,12,6,
        0,75,81,3,14,7,0,76,81,3,16,8,0,77,81,3,18,9,0,78,81,3,20,10,0,79,
        81,3,22,11,0,80,72,1,0,0,0,80,73,1,0,0,0,80,74,1,0,0,0,80,75,1,0,
        0,0,80,76,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,81,84,
        1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,
        85,86,5,22,0,0,86,87,5,74,0,0,87,88,5,88,0,0,88,3,1,0,0,0,89,90,
        3,6,3,0,90,91,5,88,0,0,91,5,1,0,0,0,92,93,3,8,4,0,93,104,5,33,0,
        0,94,103,3,6,3,0,95,103,3,4,2,0,96,103,3,12,6,0,97,103,3,14,7,0,
        98,103,3,16,8,0,99,103,3,18,9,0,100,103,3,20,10,0,101,103,3,22,11,
        0,102,94,1,0,0,0,102,95,1,0,0,0,102,96,1,0,0,0,102,97,1,0,0,0,102,
        98,1,0,0,0,102,99,1,0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,106,
        1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,104,
        1,0,0,0,107,108,5,22,0,0,108,109,5,74,0,0,109,110,5,88,0,0,110,7,
        1,0,0,0,111,112,5,48,0,0,112,114,5,74,0,0,113,115,3,10,5,0,114,113,
        1,0,0,0,114,115,1,0,0,0,115,124,1,0,0,0,116,117,5,27,0,0,117,119,
        5,74,0,0,118,120,3,10,5,0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,
        1,0,0,0,121,122,5,56,0,0,122,124,5,74,0,0,123,111,1,0,0,0,123,116,
        1,0,0,0,124,9,1,0,0,0,125,138,5,90,0,0,126,127,5,74,0,0,127,128,
        5,89,0,0,128,135,5,74,0,0,129,130,5,87,0,0,130,131,5,74,0,0,131,
        132,5,89,0,0,132,134,5,74,0,0,133,129,1,0,0,0,134,137,1,0,0,0,135,
        133,1,0,0,0,135,136,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,138,
        126,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,141,5,91,0,0,141,
        11,1,0,0,0,142,143,3,6,3,0,143,154,5,33,0,0,144,153,3,6,3,0,145,
        153,3,4,2,0,146,153,3,12,6,0,147,153,3,14,7,0,148,153,3,16,8,0,149,
        153,3,18,9,0,150,153,3,20,10,0,151,153,3,22,11,0,152,144,1,0,0,0,
        152,145,1,0,0,0,152,146,1,0,0,0,152,147,1,0,0,0,152,148,1,0,0,0,
        152,149,1,0,0,0,152,150,1,0,0,0,152,151,1,0,0,0,153,156,1,0,0,0,
        154,152,1,0,0,0,154,155,1,0,0,0,155,157,1,0,0,0,156,154,1,0,0,0,
        157,158,5,22,0,0,158,159,5,74,0,0,159,160,5,88,0,0,160,13,1,0,0,
        0,161,162,5,64,0,0,162,163,5,74,0,0,163,173,5,33,0,0,164,172,3,14,
        7,0,165,172,3,16,8,0,166,172,3,4,2,0,167,172,3,12,6,0,168,172,3,
        18,9,0,169,172,3,20,10,0,170,172,3,22,11,0,171,164,1,0,0,0,171,165,
        1,0,0,0,171,166,1,0,0,0,171,167,1,0,0,0,171,168,1,0,0,0,171,169,
        1,0,0,0,171,170,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,
        1,0,0,0,174,176,1,0,0,0,175,173,1,0,0,0,176,177,5,22,0,0,177,178,
        5,74,0,0,178,179,5,88,0,0,179,15,1,0,0,0,180,181,3,14,7,0,181,191,
        5,33,0,0,182,190,3,14,7,0,183,190,3,16,8,0,184,190,3,4,2,0,185,190,
        3,12,6,0,186,190,3,18,9,0,187,190,3,20,10,0,188,190,3,22,11,0,189,
        182,1,0,0,0,189,183,1,0,0,0,189,184,1,0,0,0,189,185,1,0,0,0,189,
        186,1,0,0,0,189,187,1,0,0,0,189,188,1,0,0,0,190,193,1,0,0,0,191,
        189,1,0,0,0,191,192,1,0,0,0,192,194,1,0,0,0,193,191,1,0,0,0,194,
        195,5,22,0,0,195,196,5,74,0,0,196,197,5,88,0,0,197,17,1,0,0,0,198,
        199,5,49,0,0,199,200,5,67,0,0,200,201,5,74,0,0,201,211,5,33,0,0,
        202,210,3,18,9,0,203,210,3,20,10,0,204,210,3,4,2,0,205,210,3,12,
        6,0,206,210,3,14,7,0,207,210,3,16,8,0,208,210,3,22,11,0,209,202,
        1,0,0,0,209,203,1,0,0,0,209,204,1,0,0,0,209,205,1,0,0,0,209,206,
        1,0,0,0,209,207,1,0,0,0,209,208,1,0,0,0,210,213,1,0,0,0,211,209,
        1,0,0,0,211,212,1,0,0,0,212,214,1,0,0,0,213,211,1,0,0,0,214,215,
        5,22,0,0,215,216,5,74,0,0,216,217,5,88,0,0,217,19,1,0,0,0,218,219,
        3,18,9,0,219,229,5,33,0,0,220,228,3,18,9,0,221,228,3,20,10,0,222,
        228,3,4,2,0,223,228,3,12,6,0,224,228,3,14,7,0,225,228,3,16,8,0,226,
        228,3,22,11,0,227,220,1,0,0,0,227,221,1,0,0,0,227,222,1,0,0,0,227,
        223,1,0,0,0,227,224,1,0,0,0,227,225,1,0,0,0,227,226,1,0,0,0,228,
        231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,232,1,0,0,0,231,
        229,1,0,0,0,232,233,5,22,0,0,233,234,5,74,0,0,234,235,5,88,0,0,235,
        21,1,0,0,0,236,243,3,4,2,0,237,243,3,12,6,0,238,243,3,14,7,0,239,
        243,3,16,8,0,240,243,3,18,9,0,241,243,3,20,10,0,242,236,1,0,0,0,
        242,237,1,0,0,0,242,238,1,0,0,0,242,239,1,0,0,0,242,240,1,0,0,0,
        242,241,1,0,0,0,243,23,1,0,0,0,244,245,5,67,0,0,245,246,5,74,0,0,
        246,247,5,33,0,0,247,248,3,26,13,0,248,249,5,88,0,0,249,25,1,0,0,
        0,250,259,3,28,14,0,251,259,3,30,15,0,252,259,3,38,19,0,253,259,
        3,44,22,0,254,259,3,46,23,0,255,259,3,48,24,0,256,259,3,50,25,0,
        257,259,3,52,26,0,258,250,1,0,0,0,258,251,1,0,0,0,258,252,1,0,0,
        0,258,253,1,0,0,0,258,254,1,0,0,0,258,255,1,0,0,0,258,256,1,0,0,
        0,258,257,1,0,0,0,259,27,1,0,0,0,260,261,5,90,0,0,261,266,5,74,0,
        0,262,263,5,87,0,0,263,265,5,74,0,0,264,262,1,0,0,0,265,268,1,0,
        0,0,266,264,1,0,0,0,266,267,1,0,0,0,267,269,1,0,0,0,268,266,1,0,
        0,0,269,270,5,91,0,0,270,29,1,0,0,0,271,272,5,9,0,0,272,273,5,90,
        0,0,273,278,3,32,16,0,274,275,5,87,0,0,275,277,3,32,16,0,276,274,
        1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,279,281,
        1,0,0,0,280,278,1,0,0,0,281,282,5,91,0,0,282,283,5,40,0,0,283,284,
        3,36,18,0,284,31,1,0,0,0,285,286,3,34,17,0,286,287,5,51,0,0,287,
        288,5,85,0,0,288,33,1,0,0,0,289,290,5,74,0,0,290,35,1,0,0,0,291,
        292,3,34,17,0,292,37,1,0,0,0,293,294,5,52,0,0,294,295,3,40,20,0,
        295,296,5,22,0,0,296,297,5,52,0,0,297,39,1,0,0,0,298,303,3,42,21,
        0,299,300,5,88,0,0,300,302,3,42,21,0,301,299,1,0,0,0,302,305,1,0,
        0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,41,1,0,0,0,305,303,1,0,0,
        0,306,307,5,74,0,0,307,308,5,89,0,0,308,309,3,34,17,0,309,43,1,0,
        0,0,310,311,5,5,0,0,311,312,3,34,17,0,312,45,1,0,0,0,313,314,5,49,
        0,0,314,315,3,26,13,0,315,47,1,0,0,0,316,317,5,63,0,0,317,318,3,
        26,13,0,318,49,1,0,0,0,319,320,5,34,0,0,320,321,3,26,13,0,321,51,
        1,0,0,0,322,323,3,54,27,0,323,53,1,0,0,0,324,327,3,34,17,0,325,326,
        5,51,0,0,326,328,5,85,0,0,327,325,1,0,0,0,327,328,1,0,0,0,328,55,
        1,0,0,0,27,64,66,80,82,102,104,114,119,123,135,138,152,154,171,173,
        189,191,209,211,227,229,242,258,266,278,303,327
    ]

class AdaGrammarParser ( Parser ):

    grammarFileName = "AdaGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'abort'", "'abs'", "'abstract'", "'accept'", 
                     "'access'", "'aliased'", "'all'", "'and'", "'array'", 
                     "'at'", "'begin'", "'body'", "'case'", "'constant'", 
                     "'declare'", "'delay'", "'delta'", "'digits'", "'do'", 
                     "'else'", "'elsif'", "'end'", "'entry'", "'exception'", 
                     "'exit'", "'for'", "'function'", "'generic'", "'goto'", 
                     "'if'", "'in'", "'interface'", "'is'", "'limited'", 
                     "'loop'", "'mod'", "'new'", "'not'", "'null'", "'of'", 
                     "'or'", "'others'", "'out'", "'overriding'", "'package'", 
                     "'pragma'", "'private'", "'procedure'", "'protected'", 
                     "'raise'", "'range'", "'record'", "'rem'", "'renames'", 
                     "'requeue'", "'return'", "'reverse'", "'select'", "'separate'", 
                     "'some'", "'subtype'", "'synchronized'", "'tagged'", 
                     "'task'", "'terminate'", "'then'", "'type'", "'until'", 
                     "'use'", "'when'", "'while'", "'with'", "'xor'", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "'/='", "'<'", "'>'", 
                     "'<='", "'>='", "'<>'", "':='", "','", "';'", "':'", 
                     "'('", "')'", "'['", "']'", "'.'", "'..'", "'=>'" ]

    symbolicNames = [ "<INVALID>", "ABORT", "ABS", "ABSTRACT", "ACCEPT", 
                      "ACCESS", "ALIASED", "ALL", "AND", "ARRAY", "AT", 
                      "BEGIN", "BODY", "CASE", "CONSTANT", "DECLARE", "DELAY", 
                      "DELTA", "DIGITS", "DO", "ELSE", "ELSIF", "END", "ENTRY", 
                      "EXCEPTION", "EXIT", "FOR", "FUNCTION", "GENERIC", 
                      "GOTO", "IF", "IN", "INTERFACE", "IS", "LIMITED", 
                      "LOOP", "MOD", "NEW", "NOT", "NULL", "OF", "OR", "OTHERS", 
                      "OUT", "OVERRIDING", "PACKAGE", "PRAGMA", "PRIVATE", 
                      "PROCEDURE", "PROTECTED", "RAISE", "RANGE", "RECORD", 
                      "REM", "RENAMES", "REQUEUE", "RETURN", "REVERSE", 
                      "SELECT", "SEPARATE", "SOME", "SUBTYPE", "SYNCHRONIZED", 
                      "TAGGED", "TASK", "TERMINATE", "THEN", "TYPE", "UNTIL", 
                      "USE", "WHEN", "WHILE", "WITH", "XOR", "ID", "ADD", 
                      "SUB", "MUL", "DIV", "EQUALS", "NOTEQUALS", "LT", 
                      "GT", "LTE", "GTE", "BOX", "ASSIGN", "COMMA", "SEMICOLON", 
                      "COLON", "LPAREN", "RPAREN", "LEFT_BRACKET", "RIGHT_BRACKET", 
                      "PERIOD", "DOT_DOT", "ARROW", "INT", "FLOAT", "CHAR", 
                      "STRING", "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_program = 0
    RULE_package_declaration = 1
    RULE_subprogram_declaration = 2
    RULE_subprogram_specification = 3
    RULE_subprogram_head = 4
    RULE_formal_part = 5
    RULE_subprogram_body = 6
    RULE_task_declaration = 7
    RULE_task_body = 8
    RULE_protected_type_declaration = 9
    RULE_protected_type_body = 10
    RULE_subunit = 11
    RULE_type_declaration = 12
    RULE_type_definition = 13
    RULE_enumeration_type_definition = 14
    RULE_array_type_definition = 15
    RULE_index_subtype_definition = 16
    RULE_subtype_mark = 17
    RULE_component_subtype_definition = 18
    RULE_record_type_definition = 19
    RULE_component_list = 20
    RULE_component_declaration = 21
    RULE_access_type_definition = 22
    RULE_protected_type_definition = 23
    RULE_tagged_type_definition = 24
    RULE_limited_type_definition = 25
    RULE_subtype_definition = 26
    RULE_subtype_indication = 27

    ruleNames =  [ "program", "package_declaration", "subprogram_declaration", 
                   "subprogram_specification", "subprogram_head", "formal_part", 
                   "subprogram_body", "task_declaration", "task_body", "protected_type_declaration", 
                   "protected_type_body", "subunit", "type_declaration", 
                   "type_definition", "enumeration_type_definition", "array_type_definition", 
                   "index_subtype_definition", "subtype_mark", "component_subtype_definition", 
                   "record_type_definition", "component_list", "component_declaration", 
                   "access_type_definition", "protected_type_definition", 
                   "tagged_type_definition", "limited_type_definition", 
                   "subtype_definition", "subtype_indication" ]

    EOF = Token.EOF
    ABORT=1
    ABS=2
    ABSTRACT=3
    ACCEPT=4
    ACCESS=5
    ALIASED=6
    ALL=7
    AND=8
    ARRAY=9
    AT=10
    BEGIN=11
    BODY=12
    CASE=13
    CONSTANT=14
    DECLARE=15
    DELAY=16
    DELTA=17
    DIGITS=18
    DO=19
    ELSE=20
    ELSIF=21
    END=22
    ENTRY=23
    EXCEPTION=24
    EXIT=25
    FOR=26
    FUNCTION=27
    GENERIC=28
    GOTO=29
    IF=30
    IN=31
    INTERFACE=32
    IS=33
    LIMITED=34
    LOOP=35
    MOD=36
    NEW=37
    NOT=38
    NULL=39
    OF=40
    OR=41
    OTHERS=42
    OUT=43
    OVERRIDING=44
    PACKAGE=45
    PRAGMA=46
    PRIVATE=47
    PROCEDURE=48
    PROTECTED=49
    RAISE=50
    RANGE=51
    RECORD=52
    REM=53
    RENAMES=54
    REQUEUE=55
    RETURN=56
    REVERSE=57
    SELECT=58
    SEPARATE=59
    SOME=60
    SUBTYPE=61
    SYNCHRONIZED=62
    TAGGED=63
    TASK=64
    TERMINATE=65
    THEN=66
    TYPE=67
    UNTIL=68
    USE=69
    WHEN=70
    WHILE=71
    WITH=72
    XOR=73
    ID=74
    ADD=75
    SUB=76
    MUL=77
    DIV=78
    EQUALS=79
    NOTEQUALS=80
    LT=81
    GT=82
    LTE=83
    GTE=84
    BOX=85
    ASSIGN=86
    COMMA=87
    SEMICOLON=88
    COLON=89
    LPAREN=90
    RPAREN=91
    LEFT_BRACKET=92
    RIGHT_BRACKET=93
    PERIOD=94
    DOT_DOT=95
    ARROW=96
    INT=97
    FLOAT=98
    CHAR=99
    STRING=100
    LINE_COMMENT=101
    BLOCK_COMMENT=102
    WS=103

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

        def package_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Package_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Package_declarationContext,i)


        def subprogram_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_declarationContext,i)


        def subprogram_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_bodyContext,i)


        def task_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_declarationContext,i)


        def task_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_bodyContext,i)


        def protected_type_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_declarationContext,i)


        def protected_type_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_bodyContext,i)


        def subunit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.SubunitContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.SubunitContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & 137445507073) != 0):
                self.state = 64
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.package_declaration()
                    pass

                elif la_ == 2:
                    self.state = 57
                    self.subprogram_declaration()
                    pass

                elif la_ == 3:
                    self.state = 58
                    self.subprogram_body()
                    pass

                elif la_ == 4:
                    self.state = 59
                    self.task_declaration()
                    pass

                elif la_ == 5:
                    self.state = 60
                    self.task_body()
                    pass

                elif la_ == 6:
                    self.state = 61
                    self.protected_type_declaration()
                    pass

                elif la_ == 7:
                    self.state = 62
                    self.protected_type_body()
                    pass

                elif la_ == 8:
                    self.state = 63
                    self.subunit()
                    pass


                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Package_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE(self):
            return self.getToken(AdaGrammarParser.PACKAGE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.ID)
            else:
                return self.getToken(AdaGrammarParser.ID, i)

        def IS(self):
            return self.getToken(AdaGrammarParser.IS, 0)

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def package_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Package_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Package_declarationContext,i)


        def subprogram_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_declarationContext,i)


        def subprogram_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_bodyContext,i)


        def task_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_declarationContext,i)


        def task_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_bodyContext,i)


        def protected_type_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_declarationContext,i)


        def protected_type_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_bodyContext,i)


        def subunit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.SubunitContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.SubunitContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_package_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackage_declaration" ):
                listener.enterPackage_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackage_declaration" ):
                listener.exitPackage_declaration(self)




    def package_declaration(self):

        localctx = AdaGrammarParser.Package_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_package_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(AdaGrammarParser.PACKAGE)
            self.state = 70
            self.match(AdaGrammarParser.ID)
            self.state = 71
            self.match(AdaGrammarParser.IS)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & 137445507073) != 0):
                self.state = 80
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 72
                    self.package_declaration()
                    pass

                elif la_ == 2:
                    self.state = 73
                    self.subprogram_declaration()
                    pass

                elif la_ == 3:
                    self.state = 74
                    self.subprogram_body()
                    pass

                elif la_ == 4:
                    self.state = 75
                    self.task_declaration()
                    pass

                elif la_ == 5:
                    self.state = 76
                    self.task_body()
                    pass

                elif la_ == 6:
                    self.state = 77
                    self.protected_type_declaration()
                    pass

                elif la_ == 7:
                    self.state = 78
                    self.protected_type_body()
                    pass

                elif la_ == 8:
                    self.state = 79
                    self.subunit()
                    pass


                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(AdaGrammarParser.END)
            self.state = 86
            self.match(AdaGrammarParser.ID)
            self.state = 87
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subprogram_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subprogram_specification(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subprogram_specificationContext,0)


        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_subprogram_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubprogram_declaration" ):
                listener.enterSubprogram_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubprogram_declaration" ):
                listener.exitSubprogram_declaration(self)




    def subprogram_declaration(self):

        localctx = AdaGrammarParser.Subprogram_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_subprogram_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.subprogram_specification()
            self.state = 90
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subprogram_specificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subprogram_head(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subprogram_headContext,0)


        def IS(self):
            return self.getToken(AdaGrammarParser.IS, 0)

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def subprogram_specification(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_specificationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_specificationContext,i)


        def subprogram_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_declarationContext,i)


        def subprogram_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_bodyContext,i)


        def task_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_declarationContext,i)


        def task_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_bodyContext,i)


        def protected_type_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_declarationContext,i)


        def protected_type_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_bodyContext,i)


        def subunit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.SubunitContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.SubunitContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_subprogram_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubprogram_specification" ):
                listener.enterSubprogram_specification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubprogram_specification" ):
                listener.exitSubprogram_specification(self)




    def subprogram_specification(self):

        localctx = AdaGrammarParser.Subprogram_specificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_subprogram_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.subprogram_head()
            self.state = 93
            self.match(AdaGrammarParser.IS)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & 137445244929) != 0):
                self.state = 102
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 94
                    self.subprogram_specification()
                    pass

                elif la_ == 2:
                    self.state = 95
                    self.subprogram_declaration()
                    pass

                elif la_ == 3:
                    self.state = 96
                    self.subprogram_body()
                    pass

                elif la_ == 4:
                    self.state = 97
                    self.task_declaration()
                    pass

                elif la_ == 5:
                    self.state = 98
                    self.task_body()
                    pass

                elif la_ == 6:
                    self.state = 99
                    self.protected_type_declaration()
                    pass

                elif la_ == 7:
                    self.state = 100
                    self.protected_type_body()
                    pass

                elif la_ == 8:
                    self.state = 101
                    self.subunit()
                    pass


                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(AdaGrammarParser.END)
            self.state = 108
            self.match(AdaGrammarParser.ID)
            self.state = 109
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subprogram_headContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE(self):
            return self.getToken(AdaGrammarParser.PROCEDURE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.ID)
            else:
                return self.getToken(AdaGrammarParser.ID, i)

        def formal_part(self):
            return self.getTypedRuleContext(AdaGrammarParser.Formal_partContext,0)


        def FUNCTION(self):
            return self.getToken(AdaGrammarParser.FUNCTION, 0)

        def RETURN(self):
            return self.getToken(AdaGrammarParser.RETURN, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_subprogram_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubprogram_head" ):
                listener.enterSubprogram_head(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubprogram_head" ):
                listener.exitSubprogram_head(self)




    def subprogram_head(self):

        localctx = AdaGrammarParser.Subprogram_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_subprogram_head)
        self._la = 0 # Token type
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(AdaGrammarParser.PROCEDURE)
                self.state = 112
                self.match(AdaGrammarParser.ID)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==90:
                    self.state = 113
                    self.formal_part()


                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(AdaGrammarParser.FUNCTION)
                self.state = 117
                self.match(AdaGrammarParser.ID)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==90:
                    self.state = 118
                    self.formal_part()


                self.state = 121
                self.match(AdaGrammarParser.RETURN)
                self.state = 122
                self.match(AdaGrammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Formal_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(AdaGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AdaGrammarParser.RPAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.ID)
            else:
                return self.getToken(AdaGrammarParser.ID, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.COLON)
            else:
                return self.getToken(AdaGrammarParser.COLON, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.COMMA)
            else:
                return self.getToken(AdaGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_formal_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormal_part" ):
                listener.enterFormal_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormal_part" ):
                listener.exitFormal_part(self)




    def formal_part(self):

        localctx = AdaGrammarParser.Formal_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_formal_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(AdaGrammarParser.LPAREN)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==74:
                self.state = 126
                self.match(AdaGrammarParser.ID)
                self.state = 127
                self.match(AdaGrammarParser.COLON)
                self.state = 128
                self.match(AdaGrammarParser.ID)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==87:
                    self.state = 129
                    self.match(AdaGrammarParser.COMMA)
                    self.state = 130
                    self.match(AdaGrammarParser.ID)
                    self.state = 131
                    self.match(AdaGrammarParser.COLON)
                    self.state = 132
                    self.match(AdaGrammarParser.ID)
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 140
            self.match(AdaGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subprogram_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subprogram_specification(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_specificationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_specificationContext,i)


        def IS(self):
            return self.getToken(AdaGrammarParser.IS, 0)

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def subprogram_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_declarationContext,i)


        def subprogram_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_bodyContext,i)


        def task_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_declarationContext,i)


        def task_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_bodyContext,i)


        def protected_type_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_declarationContext,i)


        def protected_type_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_bodyContext,i)


        def subunit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.SubunitContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.SubunitContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_subprogram_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubprogram_body" ):
                listener.enterSubprogram_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubprogram_body" ):
                listener.exitSubprogram_body(self)




    def subprogram_body(self):

        localctx = AdaGrammarParser.Subprogram_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subprogram_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.subprogram_specification()
            self.state = 143
            self.match(AdaGrammarParser.IS)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & 137445244929) != 0):
                self.state = 152
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 144
                    self.subprogram_specification()
                    pass

                elif la_ == 2:
                    self.state = 145
                    self.subprogram_declaration()
                    pass

                elif la_ == 3:
                    self.state = 146
                    self.subprogram_body()
                    pass

                elif la_ == 4:
                    self.state = 147
                    self.task_declaration()
                    pass

                elif la_ == 5:
                    self.state = 148
                    self.task_body()
                    pass

                elif la_ == 6:
                    self.state = 149
                    self.protected_type_declaration()
                    pass

                elif la_ == 7:
                    self.state = 150
                    self.protected_type_body()
                    pass

                elif la_ == 8:
                    self.state = 151
                    self.subunit()
                    pass


                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(AdaGrammarParser.END)
            self.state = 158
            self.match(AdaGrammarParser.ID)
            self.state = 159
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Task_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TASK(self):
            return self.getToken(AdaGrammarParser.TASK, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.ID)
            else:
                return self.getToken(AdaGrammarParser.ID, i)

        def IS(self):
            return self.getToken(AdaGrammarParser.IS, 0)

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def task_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_declarationContext,i)


        def task_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_bodyContext,i)


        def subprogram_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_declarationContext,i)


        def subprogram_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_bodyContext,i)


        def protected_type_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_declarationContext,i)


        def protected_type_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_bodyContext,i)


        def subunit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.SubunitContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.SubunitContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_task_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTask_declaration" ):
                listener.enterTask_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTask_declaration" ):
                listener.exitTask_declaration(self)




    def task_declaration(self):

        localctx = AdaGrammarParser.Task_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_task_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(AdaGrammarParser.TASK)
            self.state = 162
            self.match(AdaGrammarParser.ID)
            self.state = 163
            self.match(AdaGrammarParser.IS)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & 137445244929) != 0):
                self.state = 171
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 164
                    self.task_declaration()
                    pass

                elif la_ == 2:
                    self.state = 165
                    self.task_body()
                    pass

                elif la_ == 3:
                    self.state = 166
                    self.subprogram_declaration()
                    pass

                elif la_ == 4:
                    self.state = 167
                    self.subprogram_body()
                    pass

                elif la_ == 5:
                    self.state = 168
                    self.protected_type_declaration()
                    pass

                elif la_ == 6:
                    self.state = 169
                    self.protected_type_body()
                    pass

                elif la_ == 7:
                    self.state = 170
                    self.subunit()
                    pass


                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(AdaGrammarParser.END)
            self.state = 177
            self.match(AdaGrammarParser.ID)
            self.state = 178
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Task_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def task_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_declarationContext,i)


        def IS(self):
            return self.getToken(AdaGrammarParser.IS, 0)

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def task_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_bodyContext,i)


        def subprogram_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_declarationContext,i)


        def subprogram_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_bodyContext,i)


        def protected_type_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_declarationContext,i)


        def protected_type_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_bodyContext,i)


        def subunit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.SubunitContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.SubunitContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_task_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTask_body" ):
                listener.enterTask_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTask_body" ):
                listener.exitTask_body(self)




    def task_body(self):

        localctx = AdaGrammarParser.Task_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_task_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.task_declaration()
            self.state = 181
            self.match(AdaGrammarParser.IS)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & 137445244929) != 0):
                self.state = 189
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 182
                    self.task_declaration()
                    pass

                elif la_ == 2:
                    self.state = 183
                    self.task_body()
                    pass

                elif la_ == 3:
                    self.state = 184
                    self.subprogram_declaration()
                    pass

                elif la_ == 4:
                    self.state = 185
                    self.subprogram_body()
                    pass

                elif la_ == 5:
                    self.state = 186
                    self.protected_type_declaration()
                    pass

                elif la_ == 6:
                    self.state = 187
                    self.protected_type_body()
                    pass

                elif la_ == 7:
                    self.state = 188
                    self.subunit()
                    pass


                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194
            self.match(AdaGrammarParser.END)
            self.state = 195
            self.match(AdaGrammarParser.ID)
            self.state = 196
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Protected_type_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROTECTED(self):
            return self.getToken(AdaGrammarParser.PROTECTED, 0)

        def TYPE(self):
            return self.getToken(AdaGrammarParser.TYPE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.ID)
            else:
                return self.getToken(AdaGrammarParser.ID, i)

        def IS(self):
            return self.getToken(AdaGrammarParser.IS, 0)

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def protected_type_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_declarationContext,i)


        def protected_type_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_bodyContext,i)


        def subprogram_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_declarationContext,i)


        def subprogram_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_bodyContext,i)


        def task_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_declarationContext,i)


        def task_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_bodyContext,i)


        def subunit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.SubunitContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.SubunitContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_protected_type_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtected_type_declaration" ):
                listener.enterProtected_type_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtected_type_declaration" ):
                listener.exitProtected_type_declaration(self)




    def protected_type_declaration(self):

        localctx = AdaGrammarParser.Protected_type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_protected_type_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(AdaGrammarParser.PROTECTED)
            self.state = 199
            self.match(AdaGrammarParser.TYPE)
            self.state = 200
            self.match(AdaGrammarParser.ID)
            self.state = 201
            self.match(AdaGrammarParser.IS)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & 137445244929) != 0):
                self.state = 209
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 202
                    self.protected_type_declaration()
                    pass

                elif la_ == 2:
                    self.state = 203
                    self.protected_type_body()
                    pass

                elif la_ == 3:
                    self.state = 204
                    self.subprogram_declaration()
                    pass

                elif la_ == 4:
                    self.state = 205
                    self.subprogram_body()
                    pass

                elif la_ == 5:
                    self.state = 206
                    self.task_declaration()
                    pass

                elif la_ == 6:
                    self.state = 207
                    self.task_body()
                    pass

                elif la_ == 7:
                    self.state = 208
                    self.subunit()
                    pass


                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
            self.match(AdaGrammarParser.END)
            self.state = 215
            self.match(AdaGrammarParser.ID)
            self.state = 216
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Protected_type_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def protected_type_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_declarationContext,i)


        def IS(self):
            return self.getToken(AdaGrammarParser.IS, 0)

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def protected_type_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Protected_type_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Protected_type_bodyContext,i)


        def subprogram_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_declarationContext,i)


        def subprogram_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Subprogram_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Subprogram_bodyContext,i)


        def task_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_declarationContext,i)


        def task_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Task_bodyContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Task_bodyContext,i)


        def subunit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.SubunitContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.SubunitContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_protected_type_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtected_type_body" ):
                listener.enterProtected_type_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtected_type_body" ):
                listener.exitProtected_type_body(self)




    def protected_type_body(self):

        localctx = AdaGrammarParser.Protected_type_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_protected_type_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.protected_type_declaration()
            self.state = 219
            self.match(AdaGrammarParser.IS)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 27)) & ~0x3f) == 0 and ((1 << (_la - 27)) & 137445244929) != 0):
                self.state = 227
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 220
                    self.protected_type_declaration()
                    pass

                elif la_ == 2:
                    self.state = 221
                    self.protected_type_body()
                    pass

                elif la_ == 3:
                    self.state = 222
                    self.subprogram_declaration()
                    pass

                elif la_ == 4:
                    self.state = 223
                    self.subprogram_body()
                    pass

                elif la_ == 5:
                    self.state = 224
                    self.task_declaration()
                    pass

                elif la_ == 6:
                    self.state = 225
                    self.task_body()
                    pass

                elif la_ == 7:
                    self.state = 226
                    self.subunit()
                    pass


                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
            self.match(AdaGrammarParser.END)
            self.state = 233
            self.match(AdaGrammarParser.ID)
            self.state = 234
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubunitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subprogram_declaration(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subprogram_declarationContext,0)


        def subprogram_body(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subprogram_bodyContext,0)


        def task_declaration(self):
            return self.getTypedRuleContext(AdaGrammarParser.Task_declarationContext,0)


        def task_body(self):
            return self.getTypedRuleContext(AdaGrammarParser.Task_bodyContext,0)


        def protected_type_declaration(self):
            return self.getTypedRuleContext(AdaGrammarParser.Protected_type_declarationContext,0)


        def protected_type_body(self):
            return self.getTypedRuleContext(AdaGrammarParser.Protected_type_bodyContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_subunit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubunit" ):
                listener.enterSubunit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubunit" ):
                listener.exitSubunit(self)




    def subunit(self):

        localctx = AdaGrammarParser.SubunitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_subunit)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.subprogram_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.subprogram_body()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.task_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 239
                self.task_body()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.protected_type_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 241
                self.protected_type_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(AdaGrammarParser.TYPE, 0)

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def IS(self):
            return self.getToken(AdaGrammarParser.IS, 0)

        def type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Type_definitionContext,0)


        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_type_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_declaration" ):
                listener.enterType_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_declaration" ):
                listener.exitType_declaration(self)




    def type_declaration(self):

        localctx = AdaGrammarParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(AdaGrammarParser.TYPE)
            self.state = 245
            self.match(AdaGrammarParser.ID)
            self.state = 246
            self.match(AdaGrammarParser.IS)
            self.state = 247
            self.type_definition()
            self.state = 248
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enumeration_type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Enumeration_type_definitionContext,0)


        def array_type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Array_type_definitionContext,0)


        def record_type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Record_type_definitionContext,0)


        def access_type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Access_type_definitionContext,0)


        def protected_type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Protected_type_definitionContext,0)


        def tagged_type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Tagged_type_definitionContext,0)


        def limited_type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Limited_type_definitionContext,0)


        def subtype_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subtype_definitionContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_type_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_definition" ):
                listener.enterType_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_definition" ):
                listener.exitType_definition(self)




    def type_definition(self):

        localctx = AdaGrammarParser.Type_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type_definition)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [90]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.enumeration_type_definition()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.array_type_definition()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.record_type_definition()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.access_type_definition()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.protected_type_definition()
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 6)
                self.state = 255
                self.tagged_type_definition()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 7)
                self.state = 256
                self.limited_type_definition()
                pass
            elif token in [74]:
                self.enterOuterAlt(localctx, 8)
                self.state = 257
                self.subtype_definition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Enumeration_type_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(AdaGrammarParser.LPAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.ID)
            else:
                return self.getToken(AdaGrammarParser.ID, i)

        def RPAREN(self):
            return self.getToken(AdaGrammarParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.COMMA)
            else:
                return self.getToken(AdaGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_enumeration_type_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumeration_type_definition" ):
                listener.enterEnumeration_type_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumeration_type_definition" ):
                listener.exitEnumeration_type_definition(self)




    def enumeration_type_definition(self):

        localctx = AdaGrammarParser.Enumeration_type_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_enumeration_type_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(AdaGrammarParser.LPAREN)
            self.state = 261
            self.match(AdaGrammarParser.ID)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==87:
                self.state = 262
                self.match(AdaGrammarParser.COMMA)
                self.state = 263
                self.match(AdaGrammarParser.ID)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 269
            self.match(AdaGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_type_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(AdaGrammarParser.ARRAY, 0)

        def LPAREN(self):
            return self.getToken(AdaGrammarParser.LPAREN, 0)

        def index_subtype_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Index_subtype_definitionContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Index_subtype_definitionContext,i)


        def RPAREN(self):
            return self.getToken(AdaGrammarParser.RPAREN, 0)

        def OF(self):
            return self.getToken(AdaGrammarParser.OF, 0)

        def component_subtype_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Component_subtype_definitionContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.COMMA)
            else:
                return self.getToken(AdaGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_array_type_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_type_definition" ):
                listener.enterArray_type_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_type_definition" ):
                listener.exitArray_type_definition(self)




    def array_type_definition(self):

        localctx = AdaGrammarParser.Array_type_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_type_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(AdaGrammarParser.ARRAY)
            self.state = 272
            self.match(AdaGrammarParser.LPAREN)
            self.state = 273
            self.index_subtype_definition()
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==87:
                self.state = 274
                self.match(AdaGrammarParser.COMMA)
                self.state = 275
                self.index_subtype_definition()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 281
            self.match(AdaGrammarParser.RPAREN)
            self.state = 282
            self.match(AdaGrammarParser.OF)
            self.state = 283
            self.component_subtype_definition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_subtype_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subtype_mark(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subtype_markContext,0)


        def RANGE(self):
            return self.getToken(AdaGrammarParser.RANGE, 0)

        def BOX(self):
            return self.getToken(AdaGrammarParser.BOX, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_index_subtype_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_subtype_definition" ):
                listener.enterIndex_subtype_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_subtype_definition" ):
                listener.exitIndex_subtype_definition(self)




    def index_subtype_definition(self):

        localctx = AdaGrammarParser.Index_subtype_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_index_subtype_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.subtype_mark()
            self.state = 286
            self.match(AdaGrammarParser.RANGE)
            self.state = 287
            self.match(AdaGrammarParser.BOX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subtype_markContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_subtype_mark

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtype_mark" ):
                listener.enterSubtype_mark(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtype_mark" ):
                listener.exitSubtype_mark(self)




    def subtype_mark(self):

        localctx = AdaGrammarParser.Subtype_markContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_subtype_mark)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(AdaGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Component_subtype_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subtype_mark(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subtype_markContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_component_subtype_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent_subtype_definition" ):
                listener.enterComponent_subtype_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent_subtype_definition" ):
                listener.exitComponent_subtype_definition(self)




    def component_subtype_definition(self):

        localctx = AdaGrammarParser.Component_subtype_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_component_subtype_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.subtype_mark()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Record_type_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECORD(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.RECORD)
            else:
                return self.getToken(AdaGrammarParser.RECORD, i)

        def component_list(self):
            return self.getTypedRuleContext(AdaGrammarParser.Component_listContext,0)


        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_record_type_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord_type_definition" ):
                listener.enterRecord_type_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord_type_definition" ):
                listener.exitRecord_type_definition(self)




    def record_type_definition(self):

        localctx = AdaGrammarParser.Record_type_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_record_type_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(AdaGrammarParser.RECORD)
            self.state = 294
            self.component_list()
            self.state = 295
            self.match(AdaGrammarParser.END)
            self.state = 296
            self.match(AdaGrammarParser.RECORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Component_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def component_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Component_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Component_declarationContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.SEMICOLON)
            else:
                return self.getToken(AdaGrammarParser.SEMICOLON, i)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_component_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent_list" ):
                listener.enterComponent_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent_list" ):
                listener.exitComponent_list(self)




    def component_list(self):

        localctx = AdaGrammarParser.Component_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_component_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.component_declaration()
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==88:
                self.state = 299
                self.match(AdaGrammarParser.SEMICOLON)
                self.state = 300
                self.component_declaration()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Component_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def COLON(self):
            return self.getToken(AdaGrammarParser.COLON, 0)

        def subtype_mark(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subtype_markContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_component_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent_declaration" ):
                listener.enterComponent_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent_declaration" ):
                listener.exitComponent_declaration(self)




    def component_declaration(self):

        localctx = AdaGrammarParser.Component_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_component_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(AdaGrammarParser.ID)
            self.state = 307
            self.match(AdaGrammarParser.COLON)
            self.state = 308
            self.subtype_mark()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_type_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCESS(self):
            return self.getToken(AdaGrammarParser.ACCESS, 0)

        def subtype_mark(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subtype_markContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_access_type_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccess_type_definition" ):
                listener.enterAccess_type_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccess_type_definition" ):
                listener.exitAccess_type_definition(self)




    def access_type_definition(self):

        localctx = AdaGrammarParser.Access_type_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_access_type_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(AdaGrammarParser.ACCESS)
            self.state = 311
            self.subtype_mark()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Protected_type_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROTECTED(self):
            return self.getToken(AdaGrammarParser.PROTECTED, 0)

        def type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Type_definitionContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_protected_type_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtected_type_definition" ):
                listener.enterProtected_type_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtected_type_definition" ):
                listener.exitProtected_type_definition(self)




    def protected_type_definition(self):

        localctx = AdaGrammarParser.Protected_type_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_protected_type_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(AdaGrammarParser.PROTECTED)
            self.state = 314
            self.type_definition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tagged_type_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAGGED(self):
            return self.getToken(AdaGrammarParser.TAGGED, 0)

        def type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Type_definitionContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_tagged_type_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagged_type_definition" ):
                listener.enterTagged_type_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagged_type_definition" ):
                listener.exitTagged_type_definition(self)




    def tagged_type_definition(self):

        localctx = AdaGrammarParser.Tagged_type_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_tagged_type_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(AdaGrammarParser.TAGGED)
            self.state = 317
            self.type_definition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Limited_type_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIMITED(self):
            return self.getToken(AdaGrammarParser.LIMITED, 0)

        def type_definition(self):
            return self.getTypedRuleContext(AdaGrammarParser.Type_definitionContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_limited_type_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimited_type_definition" ):
                listener.enterLimited_type_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimited_type_definition" ):
                listener.exitLimited_type_definition(self)




    def limited_type_definition(self):

        localctx = AdaGrammarParser.Limited_type_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_limited_type_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(AdaGrammarParser.LIMITED)
            self.state = 320
            self.type_definition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subtype_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subtype_indication(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subtype_indicationContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_subtype_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtype_definition" ):
                listener.enterSubtype_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtype_definition" ):
                listener.exitSubtype_definition(self)




    def subtype_definition(self):

        localctx = AdaGrammarParser.Subtype_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_subtype_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.subtype_indication()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Subtype_indicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subtype_mark(self):
            return self.getTypedRuleContext(AdaGrammarParser.Subtype_markContext,0)


        def RANGE(self):
            return self.getToken(AdaGrammarParser.RANGE, 0)

        def BOX(self):
            return self.getToken(AdaGrammarParser.BOX, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_subtype_indication

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtype_indication" ):
                listener.enterSubtype_indication(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtype_indication" ):
                listener.exitSubtype_indication(self)




    def subtype_indication(self):

        localctx = AdaGrammarParser.Subtype_indicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_subtype_indication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.subtype_mark()
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 325
                self.match(AdaGrammarParser.RANGE)
                self.state = 326
                self.match(AdaGrammarParser.BOX)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





