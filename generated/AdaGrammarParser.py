# Generated from AdaGrammarParser.g4 by ANTLR 4.12.0
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
        4,1,81,425,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,5,0,78,8,0,10,0,12,
        0,81,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,5,3,99,8,3,10,3,12,3,102,9,3,1,3,3,3,105,8,3,1,4,1,4,1,4,
        3,4,110,8,4,1,4,1,4,1,4,3,4,115,8,4,1,4,1,4,3,4,119,8,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,5,5,129,8,5,10,5,12,5,132,9,5,3,5,134,8,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,
        8,1,9,1,9,5,9,154,8,9,10,9,12,9,157,9,9,3,9,159,8,9,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,3,10,169,8,10,1,11,1,11,1,11,1,11,5,11,175,
        8,11,10,11,12,11,178,9,11,1,11,5,11,181,8,11,10,11,12,11,184,9,11,
        1,11,3,11,187,8,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,
        197,8,12,10,12,12,12,200,9,12,1,13,1,13,5,13,204,8,13,10,13,12,13,
        207,9,13,1,14,1,14,1,14,3,14,212,8,14,1,15,1,15,5,15,216,8,15,10,
        15,12,15,219,9,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,
        16,5,16,231,8,16,10,16,12,16,234,9,16,1,16,1,16,1,16,1,16,1,17,1,
        17,1,17,1,17,1,18,1,18,1,18,1,18,5,18,248,8,18,10,18,12,18,251,9,
        18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,5,19,261,8,19,10,19,12,
        19,264,9,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,5,20,274,8,20,
        10,20,12,20,277,9,20,1,21,1,21,3,21,281,8,21,1,22,1,22,1,22,1,22,
        1,22,5,22,288,8,22,10,22,12,22,291,9,22,3,22,293,8,22,1,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,5,24,316,8,24,10,24,12,24,319,9,24,
        1,25,1,25,1,25,1,25,3,25,325,8,25,1,26,1,26,1,27,1,27,1,27,3,27,
        332,8,27,1,27,1,27,5,27,336,8,27,10,27,12,27,339,9,27,1,28,1,28,
        1,29,1,29,1,30,1,30,1,30,5,30,348,8,30,10,30,12,30,351,9,30,1,31,
        1,31,1,31,5,31,356,8,31,10,31,12,31,359,9,31,1,31,1,31,1,31,1,31,
        3,31,365,8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,387,8,32,
        1,33,1,33,1,33,1,33,5,33,393,8,33,10,33,12,33,396,9,33,3,33,398,
        8,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,5,35,
        411,8,35,10,35,12,35,414,9,35,3,35,416,8,35,1,35,1,35,1,36,1,36,
        1,36,3,36,423,8,36,1,36,0,0,37,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        70,72,0,5,1,0,45,50,1,0,55,60,1,0,51,52,2,0,51,52,63,63,1,0,53,54,
        448,0,79,1,0,0,0,2,82,1,0,0,0,4,88,1,0,0,0,6,94,1,0,0,0,8,118,1,
        0,0,0,10,120,1,0,0,0,12,137,1,0,0,0,14,142,1,0,0,0,16,149,1,0,0,
        0,18,158,1,0,0,0,20,168,1,0,0,0,22,170,1,0,0,0,24,192,1,0,0,0,26,
        201,1,0,0,0,28,211,1,0,0,0,30,213,1,0,0,0,32,224,1,0,0,0,34,239,
        1,0,0,0,36,243,1,0,0,0,38,256,1,0,0,0,40,269,1,0,0,0,42,280,1,0,
        0,0,44,282,1,0,0,0,46,297,1,0,0,0,48,302,1,0,0,0,50,320,1,0,0,0,
        52,326,1,0,0,0,54,328,1,0,0,0,56,340,1,0,0,0,58,342,1,0,0,0,60,344,
        1,0,0,0,62,364,1,0,0,0,64,386,1,0,0,0,66,388,1,0,0,0,68,401,1,0,
        0,0,70,405,1,0,0,0,72,419,1,0,0,0,74,78,3,2,1,0,75,78,3,4,2,0,76,
        78,3,6,3,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,81,1,0,0,
        0,79,77,1,0,0,0,79,80,1,0,0,0,80,1,1,0,0,0,81,79,1,0,0,0,82,83,5,
        43,0,0,83,84,5,50,0,0,84,85,5,72,0,0,85,86,5,50,0,0,86,87,5,66,0,
        0,87,3,1,0,0,0,88,89,5,40,0,0,89,90,5,50,0,0,90,91,5,72,0,0,91,92,
        5,50,0,0,92,93,5,66,0,0,93,5,1,0,0,0,94,95,3,8,4,0,95,100,5,20,0,
        0,96,99,3,12,6,0,97,99,3,14,7,0,98,96,1,0,0,0,98,97,1,0,0,0,99,102,
        1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,104,1,0,0,0,102,100,1,
        0,0,0,103,105,3,18,9,0,104,103,1,0,0,0,104,105,1,0,0,0,105,7,1,0,
        0,0,106,107,5,32,0,0,107,109,5,50,0,0,108,110,3,10,5,0,109,108,1,
        0,0,0,109,110,1,0,0,0,110,119,1,0,0,0,111,112,5,17,0,0,112,114,5,
        50,0,0,113,115,3,10,5,0,114,113,1,0,0,0,114,115,1,0,0,0,115,116,
        1,0,0,0,116,117,5,35,0,0,117,119,5,50,0,0,118,106,1,0,0,0,118,111,
        1,0,0,0,119,9,1,0,0,0,120,133,5,68,0,0,121,122,5,50,0,0,122,123,
        5,67,0,0,123,130,5,50,0,0,124,125,5,65,0,0,125,126,5,50,0,0,126,
        127,5,67,0,0,127,129,5,50,0,0,128,124,1,0,0,0,129,132,1,0,0,0,130,
        128,1,0,0,0,130,131,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,133,
        121,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,136,5,69,0,0,136,
        11,1,0,0,0,137,138,5,50,0,0,138,139,5,67,0,0,139,140,3,16,8,0,140,
        141,5,66,0,0,141,13,1,0,0,0,142,143,5,50,0,0,143,144,5,67,0,0,144,
        145,3,16,8,0,145,146,5,62,0,0,146,147,3,48,24,0,147,148,5,66,0,0,
        148,15,1,0,0,0,149,150,7,0,0,0,150,17,1,0,0,0,151,155,5,6,0,0,152,
        154,3,20,10,0,153,152,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,
        156,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,158,151,1,0,0,0,158,
        159,1,0,0,0,159,160,1,0,0,0,160,161,5,14,0,0,161,162,5,50,0,0,162,
        163,5,66,0,0,163,19,1,0,0,0,164,169,3,42,21,0,165,169,3,22,11,0,
        166,169,3,28,14,0,167,169,3,38,19,0,168,164,1,0,0,0,168,165,1,0,
        0,0,168,166,1,0,0,0,168,167,1,0,0,0,169,21,1,0,0,0,170,171,5,18,
        0,0,171,172,3,48,24,0,172,176,5,38,0,0,173,175,3,20,10,0,174,173,
        1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,182,
        1,0,0,0,178,176,1,0,0,0,179,181,3,24,12,0,180,179,1,0,0,0,181,184,
        1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,186,1,0,0,0,184,182,
        1,0,0,0,185,187,3,26,13,0,186,185,1,0,0,0,186,187,1,0,0,0,187,188,
        1,0,0,0,188,189,5,14,0,0,189,190,5,18,0,0,190,191,5,66,0,0,191,23,
        1,0,0,0,192,193,5,13,0,0,193,194,3,48,24,0,194,198,5,38,0,0,195,
        197,3,20,10,0,196,195,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,
        199,1,0,0,0,199,25,1,0,0,0,200,198,1,0,0,0,201,205,5,12,0,0,202,
        204,3,20,10,0,203,202,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,
        206,1,0,0,0,206,27,1,0,0,0,207,205,1,0,0,0,208,212,3,30,15,0,209,
        212,3,32,16,0,210,212,3,36,18,0,211,208,1,0,0,0,211,209,1,0,0,0,
        211,210,1,0,0,0,212,29,1,0,0,0,213,217,5,21,0,0,214,216,3,20,10,
        0,215,214,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,
        0,218,220,1,0,0,0,219,217,1,0,0,0,220,221,5,14,0,0,221,222,5,21,
        0,0,222,223,5,66,0,0,223,31,1,0,0,0,224,225,5,16,0,0,225,226,5,50,
        0,0,226,227,5,19,0,0,227,228,3,34,17,0,228,232,5,21,0,0,229,231,
        3,20,10,0,230,229,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,
        1,0,0,0,233,235,1,0,0,0,234,232,1,0,0,0,235,236,5,14,0,0,236,237,
        5,21,0,0,237,238,5,66,0,0,238,33,1,0,0,0,239,240,3,54,27,0,240,241,
        5,73,0,0,241,242,3,54,27,0,242,35,1,0,0,0,243,244,5,42,0,0,244,245,
        3,48,24,0,245,249,5,21,0,0,246,248,3,20,10,0,247,246,1,0,0,0,248,
        251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,252,1,0,0,0,251,
        249,1,0,0,0,252,253,5,14,0,0,253,254,5,21,0,0,254,255,5,66,0,0,255,
        37,1,0,0,0,256,257,5,8,0,0,257,258,3,48,24,0,258,262,5,20,0,0,259,
        261,3,40,20,0,260,259,1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,262,
        263,1,0,0,0,263,265,1,0,0,0,264,262,1,0,0,0,265,266,5,14,0,0,266,
        267,5,8,0,0,267,268,5,66,0,0,268,39,1,0,0,0,269,270,5,41,0,0,270,
        271,3,48,24,0,271,275,5,74,0,0,272,274,3,20,10,0,273,272,1,0,0,0,
        274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,41,1,0,0,0,277,
        275,1,0,0,0,278,281,3,46,23,0,279,281,3,44,22,0,280,278,1,0,0,0,
        280,279,1,0,0,0,281,43,1,0,0,0,282,283,5,50,0,0,283,292,5,68,0,0,
        284,289,3,48,24,0,285,286,5,65,0,0,286,288,3,48,24,0,287,285,1,0,
        0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,293,1,0,
        0,0,291,289,1,0,0,0,292,284,1,0,0,0,292,293,1,0,0,0,293,294,1,0,
        0,0,294,295,5,69,0,0,295,296,5,66,0,0,296,45,1,0,0,0,297,298,5,50,
        0,0,298,299,5,62,0,0,299,300,3,48,24,0,300,301,5,66,0,0,301,47,1,
        0,0,0,302,317,3,50,25,0,303,304,5,3,0,0,304,316,3,50,25,0,305,306,
        5,3,0,0,306,307,5,38,0,0,307,316,3,50,25,0,308,309,5,27,0,0,309,
        316,3,50,25,0,310,311,5,27,0,0,311,312,5,12,0,0,312,316,3,50,25,
        0,313,314,5,44,0,0,314,316,3,50,25,0,315,303,1,0,0,0,315,305,1,0,
        0,0,315,308,1,0,0,0,315,310,1,0,0,0,315,313,1,0,0,0,316,319,1,0,
        0,0,317,315,1,0,0,0,317,318,1,0,0,0,318,49,1,0,0,0,319,317,1,0,0,
        0,320,324,3,54,27,0,321,322,3,52,26,0,322,323,3,54,27,0,323,325,
        1,0,0,0,324,321,1,0,0,0,324,325,1,0,0,0,325,51,1,0,0,0,326,327,7,
        1,0,0,327,53,1,0,0,0,328,337,3,60,30,0,329,332,3,56,28,0,330,332,
        3,58,29,0,331,329,1,0,0,0,331,330,1,0,0,0,332,333,1,0,0,0,333,334,
        3,60,30,0,334,336,1,0,0,0,335,331,1,0,0,0,336,339,1,0,0,0,337,335,
        1,0,0,0,337,338,1,0,0,0,338,55,1,0,0,0,339,337,1,0,0,0,340,341,7,
        2,0,0,341,57,1,0,0,0,342,343,7,3,0,0,343,59,1,0,0,0,344,349,3,62,
        31,0,345,346,7,4,0,0,346,348,3,62,31,0,347,345,1,0,0,0,348,351,1,
        0,0,0,349,347,1,0,0,0,349,350,1,0,0,0,350,61,1,0,0,0,351,349,1,0,
        0,0,352,357,3,64,32,0,353,354,5,64,0,0,354,356,3,64,32,0,355,353,
        1,0,0,0,356,359,1,0,0,0,357,355,1,0,0,0,357,358,1,0,0,0,358,365,
        1,0,0,0,359,357,1,0,0,0,360,361,5,1,0,0,361,365,3,64,32,0,362,363,
        5,24,0,0,363,365,3,64,32,0,364,352,1,0,0,0,364,360,1,0,0,0,364,362,
        1,0,0,0,365,63,1,0,0,0,366,387,5,50,0,0,367,387,5,75,0,0,368,387,
        5,76,0,0,369,387,5,77,0,0,370,387,5,78,0,0,371,372,5,68,0,0,372,
        373,3,48,24,0,373,374,5,69,0,0,374,387,1,0,0,0,375,376,5,24,0,0,
        376,387,3,64,32,0,377,378,5,1,0,0,378,387,3,64,32,0,379,380,5,23,
        0,0,380,387,5,50,0,0,381,387,5,25,0,0,382,387,3,66,33,0,383,387,
        3,68,34,0,384,387,3,70,35,0,385,387,5,28,0,0,386,366,1,0,0,0,386,
        367,1,0,0,0,386,368,1,0,0,0,386,369,1,0,0,0,386,370,1,0,0,0,386,
        371,1,0,0,0,386,375,1,0,0,0,386,377,1,0,0,0,386,379,1,0,0,0,386,
        381,1,0,0,0,386,382,1,0,0,0,386,383,1,0,0,0,386,384,1,0,0,0,386,
        385,1,0,0,0,387,65,1,0,0,0,388,397,5,68,0,0,389,394,3,72,36,0,390,
        391,5,65,0,0,391,393,3,72,36,0,392,390,1,0,0,0,393,396,1,0,0,0,394,
        392,1,0,0,0,394,395,1,0,0,0,395,398,1,0,0,0,396,394,1,0,0,0,397,
        389,1,0,0,0,397,398,1,0,0,0,398,399,1,0,0,0,399,400,5,69,0,0,400,
        67,1,0,0,0,401,402,5,50,0,0,402,403,5,72,0,0,403,404,5,50,0,0,404,
        69,1,0,0,0,405,406,5,50,0,0,406,415,5,68,0,0,407,412,3,48,24,0,408,
        409,5,65,0,0,409,411,3,48,24,0,410,408,1,0,0,0,411,414,1,0,0,0,412,
        410,1,0,0,0,412,413,1,0,0,0,413,416,1,0,0,0,414,412,1,0,0,0,415,
        407,1,0,0,0,415,416,1,0,0,0,416,417,1,0,0,0,417,418,5,69,0,0,418,
        71,1,0,0,0,419,422,3,48,24,0,420,421,5,74,0,0,421,423,3,48,24,0,
        422,420,1,0,0,0,422,423,1,0,0,0,423,73,1,0,0,0,41,77,79,98,100,104,
        109,114,118,130,133,155,158,168,176,182,186,198,205,211,217,232,
        249,262,275,280,289,292,315,317,324,331,337,349,357,364,386,394,
        397,412,415,422
    ]

class AdaGrammarParser ( Parser ):

    grammarFileName = "AdaGrammarParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'abs'", "'all'", "'and'", "'array'", 
                     "'at'", "'begin'", "'body'", "'case'", "'constant'", 
                     "'declare'", "'do'", "'else'", "'elsif'", "'end'", 
                     "'exit'", "'for'", "'function'", "'if'", "'in'", "'is'", 
                     "'loop'", "'mod'", "'new'", "'not'", "'null'", "'of'", 
                     "'or'", "'others'", "'package'", "'pragma'", "'private'", 
                     "'procedure'", "'range'", "'record'", "'return'", "'reverse'", 
                     "'subtype'", "'then'", "'type'", "'use'", "'when'", 
                     "'while'", "'with'", "'xor'", "'Integer'", "'Float'", 
                     "'Char'", "'String'", "'Boolean'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'='", "'/='", "'<'", "'>'", "'<='", 
                     "'>='", "'<>'", "':='", "'&'", "'**'", "','", "';'", 
                     "':'", "'('", "')'", "'['", "']'", "'.'", "'..'", "'=>'" ]

    symbolicNames = [ "<INVALID>", "ABS", "ALL", "AND", "ARRAY", "AT", "BEGIN", 
                      "BODY", "CASE", "CONSTANT", "DECLARE", "DO", "ELSE", 
                      "ELSIF", "END", "EXIT", "FOR", "FUNCTION", "IF", "IN", 
                      "IS", "LOOP", "MOD", "NEW", "NOT", "NULL", "OF", "OR", 
                      "OTHERS", "PACKAGE", "PRAGMA", "PRIVATE", "PROCEDURE", 
                      "RANGE", "RECORD", "RETURN", "REVERSE", "SUBTYPE", 
                      "THEN", "TYPE", "USE", "WHEN", "WHILE", "WITH", "XOR", 
                      "INT_TYPE", "FLOAT_TYPE", "CHAR_TYPE", "STRING_TYPE", 
                      "BOOLEAN_TYPE", "ID", "ADD", "SUB", "MUL", "DIV", 
                      "EQUALS", "NOTEQUALS", "LT", "GT", "LTE", "GTE", "BOX", 
                      "ASSIGN", "CONCAT", "POW", "COMMA", "SEMICOLON", "COLON", 
                      "LPAREN", "RPAREN", "LEFT_BRACKET", "RIGHT_BRACKET", 
                      "PERIOD", "DOT_DOT", "ARROW", "INT", "FLOAT", "CHAR", 
                      "STRING", "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_program = 0
    RULE_package_import = 1
    RULE_package_use = 2
    RULE_program_declaration = 3
    RULE_program_head = 4
    RULE_input_vars = 5
    RULE_variable_declaration = 6
    RULE_full_variable_declaration = 7
    RULE_type = 8
    RULE_begin_end_block = 9
    RULE_statement = 10
    RULE_if_statement = 11
    RULE_elsif_statement = 12
    RULE_else_statement = 13
    RULE_loop_statement = 14
    RULE_basic_loop = 15
    RULE_for_loop = 16
    RULE_range = 17
    RULE_while_loop = 18
    RULE_case_statement = 19
    RULE_case_statement_alternative = 20
    RULE_simple_statement = 21
    RULE_procedure_call_statement = 22
    RULE_assignment_statement = 23
    RULE_expression = 24
    RULE_relation = 25
    RULE_relational_operator = 26
    RULE_simple_expression = 27
    RULE_unary_adding_operator = 28
    RULE_binary_adding_operator = 29
    RULE_term = 30
    RULE_factor = 31
    RULE_primary = 32
    RULE_aggregate = 33
    RULE_qualified_expression = 34
    RULE_function_call = 35
    RULE_element_association = 36

    ruleNames =  [ "program", "package_import", "package_use", "program_declaration", 
                   "program_head", "input_vars", "variable_declaration", 
                   "full_variable_declaration", "type", "begin_end_block", 
                   "statement", "if_statement", "elsif_statement", "else_statement", 
                   "loop_statement", "basic_loop", "for_loop", "range", 
                   "while_loop", "case_statement", "case_statement_alternative", 
                   "simple_statement", "procedure_call_statement", "assignment_statement", 
                   "expression", "relation", "relational_operator", "simple_expression", 
                   "unary_adding_operator", "binary_adding_operator", "term", 
                   "factor", "primary", "aggregate", "qualified_expression", 
                   "function_call", "element_association" ]

    EOF = Token.EOF
    ABS=1
    ALL=2
    AND=3
    ARRAY=4
    AT=5
    BEGIN=6
    BODY=7
    CASE=8
    CONSTANT=9
    DECLARE=10
    DO=11
    ELSE=12
    ELSIF=13
    END=14
    EXIT=15
    FOR=16
    FUNCTION=17
    IF=18
    IN=19
    IS=20
    LOOP=21
    MOD=22
    NEW=23
    NOT=24
    NULL=25
    OF=26
    OR=27
    OTHERS=28
    PACKAGE=29
    PRAGMA=30
    PRIVATE=31
    PROCEDURE=32
    RANGE=33
    RECORD=34
    RETURN=35
    REVERSE=36
    SUBTYPE=37
    THEN=38
    TYPE=39
    USE=40
    WHEN=41
    WHILE=42
    WITH=43
    XOR=44
    INT_TYPE=45
    FLOAT_TYPE=46
    CHAR_TYPE=47
    STRING_TYPE=48
    BOOLEAN_TYPE=49
    ID=50
    ADD=51
    SUB=52
    MUL=53
    DIV=54
    EQUALS=55
    NOTEQUALS=56
    LT=57
    GT=58
    LTE=59
    GTE=60
    BOX=61
    ASSIGN=62
    CONCAT=63
    POW=64
    COMMA=65
    SEMICOLON=66
    COLON=67
    LPAREN=68
    RPAREN=69
    LEFT_BRACKET=70
    RIGHT_BRACKET=71
    PERIOD=72
    DOT_DOT=73
    ARROW=74
    INT=75
    FLOAT=76
    CHAR=77
    STRING=78
    LINE_COMMENT=79
    BLOCK_COMMENT=80
    WS=81

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

        def package_import(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Package_importContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Package_importContext,i)


        def package_use(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Package_useContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Package_useContext,i)


        def program_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Program_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Program_declarationContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AdaGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9899899748352) != 0):
                self.state = 77
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [43]:
                    self.state = 74
                    self.package_import()
                    pass
                elif token in [40]:
                    self.state = 75
                    self.package_use()
                    pass
                elif token in [17, 32]:
                    self.state = 76
                    self.program_declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Package_importContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH(self):
            return self.getToken(AdaGrammarParser.WITH, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.ID)
            else:
                return self.getToken(AdaGrammarParser.ID, i)

        def PERIOD(self):
            return self.getToken(AdaGrammarParser.PERIOD, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_package_import

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackage_import" ):
                listener.enterPackage_import(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackage_import" ):
                listener.exitPackage_import(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackage_import" ):
                return visitor.visitPackage_import(self)
            else:
                return visitor.visitChildren(self)




    def package_import(self):

        localctx = AdaGrammarParser.Package_importContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_package_import)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(AdaGrammarParser.WITH)
            self.state = 83
            self.match(AdaGrammarParser.ID)
            self.state = 84
            self.match(AdaGrammarParser.PERIOD)
            self.state = 85
            self.match(AdaGrammarParser.ID)
            self.state = 86
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Package_useContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(AdaGrammarParser.USE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.ID)
            else:
                return self.getToken(AdaGrammarParser.ID, i)

        def PERIOD(self):
            return self.getToken(AdaGrammarParser.PERIOD, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_package_use

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPackage_use" ):
                listener.enterPackage_use(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPackage_use" ):
                listener.exitPackage_use(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackage_use" ):
                return visitor.visitPackage_use(self)
            else:
                return visitor.visitChildren(self)




    def package_use(self):

        localctx = AdaGrammarParser.Package_useContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_package_use)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(AdaGrammarParser.USE)
            self.state = 89
            self.match(AdaGrammarParser.ID)
            self.state = 90
            self.match(AdaGrammarParser.PERIOD)
            self.state = 91
            self.match(AdaGrammarParser.ID)
            self.state = 92
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program_head(self):
            return self.getTypedRuleContext(AdaGrammarParser.Program_headContext,0)


        def IS(self):
            return self.getToken(AdaGrammarParser.IS, 0)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Variable_declarationContext,i)


        def full_variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Full_variable_declarationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Full_variable_declarationContext,i)


        def begin_end_block(self):
            return self.getTypedRuleContext(AdaGrammarParser.Begin_end_blockContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_program_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram_declaration" ):
                listener.enterProgram_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram_declaration" ):
                listener.exitProgram_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_declaration" ):
                return visitor.visitProgram_declaration(self)
            else:
                return visitor.visitChildren(self)




    def program_declaration(self):

        localctx = AdaGrammarParser.Program_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_program_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.program_head()
            self.state = 95
            self.match(AdaGrammarParser.IS)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 98
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 96
                    self.variable_declaration()
                    pass

                elif la_ == 2:
                    self.state = 97
                    self.full_variable_declaration()
                    pass


                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6 or _la==14:
                self.state = 103
                self.begin_end_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_headContext(ParserRuleContext):
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

        def input_vars(self):
            return self.getTypedRuleContext(AdaGrammarParser.Input_varsContext,0)


        def FUNCTION(self):
            return self.getToken(AdaGrammarParser.FUNCTION, 0)

        def RETURN(self):
            return self.getToken(AdaGrammarParser.RETURN, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_program_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram_head" ):
                listener.enterProgram_head(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram_head" ):
                listener.exitProgram_head(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_head" ):
                return visitor.visitProgram_head(self)
            else:
                return visitor.visitChildren(self)




    def program_head(self):

        localctx = AdaGrammarParser.Program_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_program_head)
        self._la = 0 # Token type
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(AdaGrammarParser.PROCEDURE)
                self.state = 107
                self.match(AdaGrammarParser.ID)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==68:
                    self.state = 108
                    self.input_vars()


                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(AdaGrammarParser.FUNCTION)
                self.state = 112
                self.match(AdaGrammarParser.ID)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==68:
                    self.state = 113
                    self.input_vars()


                self.state = 116
                self.match(AdaGrammarParser.RETURN)
                self.state = 117
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


    class Input_varsContext(ParserRuleContext):
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
            return AdaGrammarParser.RULE_input_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_vars" ):
                listener.enterInput_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_vars" ):
                listener.exitInput_vars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_vars" ):
                return visitor.visitInput_vars(self)
            else:
                return visitor.visitChildren(self)




    def input_vars(self):

        localctx = AdaGrammarParser.Input_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_input_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(AdaGrammarParser.LPAREN)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 121
                self.match(AdaGrammarParser.ID)
                self.state = 122
                self.match(AdaGrammarParser.COLON)
                self.state = 123
                self.match(AdaGrammarParser.ID)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==65:
                    self.state = 124
                    self.match(AdaGrammarParser.COMMA)
                    self.state = 125
                    self.match(AdaGrammarParser.ID)
                    self.state = 126
                    self.match(AdaGrammarParser.COLON)
                    self.state = 127
                    self.match(AdaGrammarParser.ID)
                    self.state = 132
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 135
            self.match(AdaGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def COLON(self):
            return self.getToken(AdaGrammarParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(AdaGrammarParser.TypeContext,0)


        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = AdaGrammarParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(AdaGrammarParser.ID)
            self.state = 138
            self.match(AdaGrammarParser.COLON)
            self.state = 139
            self.type_()
            self.state = 140
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Full_variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def COLON(self):
            return self.getToken(AdaGrammarParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(AdaGrammarParser.TypeContext,0)


        def ASSIGN(self):
            return self.getToken(AdaGrammarParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_full_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFull_variable_declaration" ):
                listener.enterFull_variable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFull_variable_declaration" ):
                listener.exitFull_variable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFull_variable_declaration" ):
                return visitor.visitFull_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def full_variable_declaration(self):

        localctx = AdaGrammarParser.Full_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_full_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(AdaGrammarParser.ID)
            self.state = 143
            self.match(AdaGrammarParser.COLON)
            self.state = 144
            self.type_()
            self.state = 145
            self.match(AdaGrammarParser.ASSIGN)
            self.state = 146
            self.expression()
            self.state = 147
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(AdaGrammarParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(AdaGrammarParser.FLOAT_TYPE, 0)

        def CHAR_TYPE(self):
            return self.getToken(AdaGrammarParser.CHAR_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(AdaGrammarParser.STRING_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(AdaGrammarParser.BOOLEAN_TYPE, 0)

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = AdaGrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2216615441596416) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Begin_end_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def BEGIN(self):
            return self.getToken(AdaGrammarParser.BEGIN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_begin_end_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBegin_end_block" ):
                listener.enterBegin_end_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBegin_end_block" ):
                listener.exitBegin_end_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBegin_end_block" ):
                return visitor.visitBegin_end_block(self)
            else:
                return visitor.visitChildren(self)




    def begin_end_block(self):

        localctx = AdaGrammarParser.Begin_end_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_begin_end_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 151
                self.match(AdaGrammarParser.BEGIN)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1130297955778816) != 0):
                    self.state = 152
                    self.statement()
                    self.state = 157
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 160
            self.match(AdaGrammarParser.END)
            self.state = 161
            self.match(AdaGrammarParser.ID)
            self.state = 162
            self.match(AdaGrammarParser.SEMICOLON)
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

        def simple_statement(self):
            return self.getTypedRuleContext(AdaGrammarParser.Simple_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(AdaGrammarParser.If_statementContext,0)


        def loop_statement(self):
            return self.getTypedRuleContext(AdaGrammarParser.Loop_statementContext,0)


        def case_statement(self):
            return self.getTypedRuleContext(AdaGrammarParser.Case_statementContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = AdaGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.state = 164
                self.simple_statement()
                pass
            elif token in [18]:
                self.state = 165
                self.if_statement()
                pass
            elif token in [16, 21, 42]:
                self.state = 166
                self.loop_statement()
                pass
            elif token in [8]:
                self.state = 167
                self.case_statement()
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


    class If_statementContext(ParserRuleContext):
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

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.StatementContext,i)


        def elsif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Elsif_statementContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Elsif_statementContext,i)


        def else_statement(self):
            return self.getTypedRuleContext(AdaGrammarParser.Else_statementContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = AdaGrammarParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(AdaGrammarParser.IF)
            self.state = 171
            self.expression()
            self.state = 172
            self.match(AdaGrammarParser.THEN)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1130297955778816) != 0):
                self.state = 173
                self.statement()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 179
                self.elsif_statement()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 185
                self.else_statement()


            self.state = 188
            self.match(AdaGrammarParser.END)
            self.state = 189
            self.match(AdaGrammarParser.IF)
            self.state = 190
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elsif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSIF(self):
            return self.getToken(AdaGrammarParser.ELSIF, 0)

        def expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(AdaGrammarParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_elsif_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElsif_statement" ):
                listener.enterElsif_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElsif_statement" ):
                listener.exitElsif_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsif_statement" ):
                return visitor.visitElsif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elsif_statement(self):

        localctx = AdaGrammarParser.Elsif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elsif_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(AdaGrammarParser.ELSIF)
            self.state = 193
            self.expression()
            self.state = 194
            self.match(AdaGrammarParser.THEN)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1130297955778816) != 0):
                self.state = 195
                self.statement()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(AdaGrammarParser.ELSE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = AdaGrammarParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_else_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(AdaGrammarParser.ELSE)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1130297955778816) != 0):
                self.state = 202
                self.statement()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_loop(self):
            return self.getTypedRuleContext(AdaGrammarParser.Basic_loopContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(AdaGrammarParser.For_loopContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(AdaGrammarParser.While_loopContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_loop_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_statement" ):
                listener.enterLoop_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_statement" ):
                listener.exitLoop_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_statement" ):
                return visitor.visitLoop_statement(self)
            else:
                return visitor.visitChildren(self)




    def loop_statement(self):

        localctx = AdaGrammarParser.Loop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_loop_statement)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.basic_loop()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.for_loop()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.while_loop()
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


    class Basic_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOOP(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.LOOP)
            else:
                return self.getToken(AdaGrammarParser.LOOP, i)

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_basic_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasic_loop" ):
                listener.enterBasic_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasic_loop" ):
                listener.exitBasic_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_loop" ):
                return visitor.visitBasic_loop(self)
            else:
                return visitor.visitChildren(self)




    def basic_loop(self):

        localctx = AdaGrammarParser.Basic_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_basic_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(AdaGrammarParser.LOOP)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1130297955778816) != 0):
                self.state = 214
                self.statement()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 220
            self.match(AdaGrammarParser.END)
            self.state = 221
            self.match(AdaGrammarParser.LOOP)
            self.state = 222
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(AdaGrammarParser.FOR, 0)

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def IN(self):
            return self.getToken(AdaGrammarParser.IN, 0)

        def range_(self):
            return self.getTypedRuleContext(AdaGrammarParser.RangeContext,0)


        def LOOP(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.LOOP)
            else:
                return self.getToken(AdaGrammarParser.LOOP, i)

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = AdaGrammarParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(AdaGrammarParser.FOR)
            self.state = 225
            self.match(AdaGrammarParser.ID)
            self.state = 226
            self.match(AdaGrammarParser.IN)
            self.state = 227
            self.range_()
            self.state = 228
            self.match(AdaGrammarParser.LOOP)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1130297955778816) != 0):
                self.state = 229
                self.statement()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self.match(AdaGrammarParser.END)
            self.state = 236
            self.match(AdaGrammarParser.LOOP)
            self.state = 237
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Simple_expressionContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Simple_expressionContext,i)


        def DOT_DOT(self):
            return self.getToken(AdaGrammarParser.DOT_DOT, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = AdaGrammarParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.simple_expression()
            self.state = 240
            self.match(AdaGrammarParser.DOT_DOT)
            self.state = 241
            self.simple_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
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

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = AdaGrammarParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_while_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(AdaGrammarParser.WHILE)
            self.state = 244
            self.expression()
            self.state = 245
            self.match(AdaGrammarParser.LOOP)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1130297955778816) != 0):
                self.state = 246
                self.statement()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self.match(AdaGrammarParser.END)
            self.state = 253
            self.match(AdaGrammarParser.LOOP)
            self.state = 254
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.CASE)
            else:
                return self.getToken(AdaGrammarParser.CASE, i)

        def expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,0)


        def IS(self):
            return self.getToken(AdaGrammarParser.IS, 0)

        def END(self):
            return self.getToken(AdaGrammarParser.END, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def case_statement_alternative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Case_statement_alternativeContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Case_statement_alternativeContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_case_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_statement" ):
                listener.enterCase_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_statement" ):
                listener.exitCase_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase_statement" ):
                return visitor.visitCase_statement(self)
            else:
                return visitor.visitChildren(self)




    def case_statement(self):

        localctx = AdaGrammarParser.Case_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_case_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(AdaGrammarParser.CASE)
            self.state = 257
            self.expression()
            self.state = 258
            self.match(AdaGrammarParser.IS)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 259
                self.case_statement_alternative()
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 265
            self.match(AdaGrammarParser.END)
            self.state = 266
            self.match(AdaGrammarParser.CASE)
            self.state = 267
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_statement_alternativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(AdaGrammarParser.WHEN, 0)

        def expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,0)


        def ARROW(self):
            return self.getToken(AdaGrammarParser.ARROW, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_case_statement_alternative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_statement_alternative" ):
                listener.enterCase_statement_alternative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_statement_alternative" ):
                listener.exitCase_statement_alternative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase_statement_alternative" ):
                return visitor.visitCase_statement_alternative(self)
            else:
                return visitor.visitChildren(self)




    def case_statement_alternative(self):

        localctx = AdaGrammarParser.Case_statement_alternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_case_statement_alternative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(AdaGrammarParser.WHEN)
            self.state = 270
            self.expression()
            self.state = 271
            self.match(AdaGrammarParser.ARROW)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1130297955778816) != 0):
                self.state = 272
                self.statement()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_statement(self):
            return self.getTypedRuleContext(AdaGrammarParser.Assignment_statementContext,0)


        def procedure_call_statement(self):
            return self.getTypedRuleContext(AdaGrammarParser.Procedure_call_statementContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_simple_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_statement" ):
                listener.enterSimple_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_statement" ):
                listener.exitSimple_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_statement" ):
                return visitor.visitSimple_statement(self)
            else:
                return visitor.visitChildren(self)




    def simple_statement(self):

        localctx = AdaGrammarParser.Simple_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_simple_statement)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.assignment_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.procedure_call_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Procedure_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def LPAREN(self):
            return self.getToken(AdaGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AdaGrammarParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

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
            return AdaGrammarParser.RULE_procedure_call_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedure_call_statement" ):
                listener.enterProcedure_call_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedure_call_statement" ):
                listener.exitProcedure_call_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure_call_statement" ):
                return visitor.visitProcedure_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def procedure_call_statement(self):

        localctx = AdaGrammarParser.Procedure_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_procedure_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(AdaGrammarParser.ID)
            self.state = 283
            self.match(AdaGrammarParser.LPAREN)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125900233998338) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 1921) != 0):
                self.state = 284
                self.expression()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==65:
                    self.state = 285
                    self.match(AdaGrammarParser.COMMA)
                    self.state = 286
                    self.expression()
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 294
            self.match(AdaGrammarParser.RPAREN)
            self.state = 295
            self.match(AdaGrammarParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(AdaGrammarParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(AdaGrammarParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_assignment_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_statement" ):
                listener.enterAssignment_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_statement" ):
                listener.exitAssignment_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = AdaGrammarParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(AdaGrammarParser.ID)
            self.state = 298
            self.match(AdaGrammarParser.ASSIGN)
            self.state = 299
            self.expression()
            self.state = 300
            self.match(AdaGrammarParser.SEMICOLON)
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

        def relation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.RelationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.RelationContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.AND)
            else:
                return self.getToken(AdaGrammarParser.AND, i)

        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.THEN)
            else:
                return self.getToken(AdaGrammarParser.THEN, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.OR)
            else:
                return self.getToken(AdaGrammarParser.OR, i)

        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.ELSE)
            else:
                return self.getToken(AdaGrammarParser.ELSE, i)

        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.XOR)
            else:
                return self.getToken(AdaGrammarParser.XOR, i)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = AdaGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.relation()
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 17592320262152) != 0):
                self.state = 315
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 303
                    self.match(AdaGrammarParser.AND)
                    self.state = 304
                    self.relation()
                    pass

                elif la_ == 2:
                    self.state = 305
                    self.match(AdaGrammarParser.AND)
                    self.state = 306
                    self.match(AdaGrammarParser.THEN)
                    self.state = 307
                    self.relation()
                    pass

                elif la_ == 3:
                    self.state = 308
                    self.match(AdaGrammarParser.OR)
                    self.state = 309
                    self.relation()
                    pass

                elif la_ == 4:
                    self.state = 310
                    self.match(AdaGrammarParser.OR)
                    self.state = 311
                    self.match(AdaGrammarParser.ELSE)
                    self.state = 312
                    self.relation()
                    pass

                elif la_ == 5:
                    self.state = 313
                    self.match(AdaGrammarParser.XOR)
                    self.state = 314
                    self.relation()
                    pass


                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Simple_expressionContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Simple_expressionContext,i)


        def relational_operator(self):
            return self.getTypedRuleContext(AdaGrammarParser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = AdaGrammarParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.simple_expression()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2269814212194729984) != 0):
                self.state = 321
                self.relational_operator()
                self.state = 322
                self.simple_expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(AdaGrammarParser.EQUALS, 0)

        def NOTEQUALS(self):
            return self.getToken(AdaGrammarParser.NOTEQUALS, 0)

        def LT(self):
            return self.getToken(AdaGrammarParser.LT, 0)

        def GT(self):
            return self.getToken(AdaGrammarParser.GT, 0)

        def LTE(self):
            return self.getToken(AdaGrammarParser.LTE, 0)

        def GTE(self):
            return self.getToken(AdaGrammarParser.GTE, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_relational_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_operator" ):
                listener.enterRelational_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_operator" ):
                listener.exitRelational_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operator" ):
                return visitor.visitRelational_operator(self)
            else:
                return visitor.visitChildren(self)




    def relational_operator(self):

        localctx = AdaGrammarParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2269814212194729984) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.TermContext,i)


        def unary_adding_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Unary_adding_operatorContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Unary_adding_operatorContext,i)


        def binary_adding_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Binary_adding_operatorContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Binary_adding_operatorContext,i)


        def getRuleIndex(self):
            return AdaGrammarParser.RULE_simple_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_expression" ):
                listener.enterSimple_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_expression" ):
                listener.exitSimple_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_expression" ):
                return visitor.visitSimple_expression(self)
            else:
                return visitor.visitChildren(self)




    def simple_expression(self):

        localctx = AdaGrammarParser.Simple_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_simple_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.term()
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9216616637413720064) != 0):
                self.state = 331
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 329
                    self.unary_adding_operator()
                    pass

                elif la_ == 2:
                    self.state = 330
                    self.binary_adding_operator()
                    pass


                self.state = 333
                self.term()
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_adding_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(AdaGrammarParser.ADD, 0)

        def SUB(self):
            return self.getToken(AdaGrammarParser.SUB, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_unary_adding_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_adding_operator" ):
                listener.enterUnary_adding_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_adding_operator" ):
                listener.exitUnary_adding_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_adding_operator" ):
                return visitor.visitUnary_adding_operator(self)
            else:
                return visitor.visitChildren(self)




    def unary_adding_operator(self):

        localctx = AdaGrammarParser.Unary_adding_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_unary_adding_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            _la = self._input.LA(1)
            if not(_la==51 or _la==52):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Binary_adding_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(AdaGrammarParser.ADD, 0)

        def SUB(self):
            return self.getToken(AdaGrammarParser.SUB, 0)

        def CONCAT(self):
            return self.getToken(AdaGrammarParser.CONCAT, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_binary_adding_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_adding_operator" ):
                listener.enterBinary_adding_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_adding_operator" ):
                listener.exitBinary_adding_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_adding_operator" ):
                return visitor.visitBinary_adding_operator(self)
            else:
                return visitor.visitChildren(self)




    def binary_adding_operator(self):

        localctx = AdaGrammarParser.Binary_adding_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_binary_adding_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -9216616637413720064) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.FactorContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.MUL)
            else:
                return self.getToken(AdaGrammarParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.DIV)
            else:
                return self.getToken(AdaGrammarParser.DIV, i)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = AdaGrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.factor()
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53 or _la==54:
                self.state = 345
                _la = self._input.LA(1)
                if not(_la==53 or _la==54):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 346
                self.factor()
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.PrimaryContext,i)


        def POW(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.POW)
            else:
                return self.getToken(AdaGrammarParser.POW, i)

        def ABS(self):
            return self.getToken(AdaGrammarParser.ABS, 0)

        def NOT(self):
            return self.getToken(AdaGrammarParser.NOT, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = AdaGrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.primary()
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==64:
                    self.state = 353
                    self.match(AdaGrammarParser.POW)
                    self.state = 354
                    self.primary()
                    self.state = 359
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(AdaGrammarParser.ABS)
                self.state = 361
                self.primary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 362
                self.match(AdaGrammarParser.NOT)
                self.state = 363
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def LPAREN(self):
            return self.getToken(AdaGrammarParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(AdaGrammarParser.RPAREN, 0)

        def NOT(self):
            return self.getToken(AdaGrammarParser.NOT, 0)

        def primary(self):
            return self.getTypedRuleContext(AdaGrammarParser.PrimaryContext,0)


        def ABS(self):
            return self.getToken(AdaGrammarParser.ABS, 0)

        def NEW(self):
            return self.getToken(AdaGrammarParser.NEW, 0)

        def NULL(self):
            return self.getToken(AdaGrammarParser.NULL, 0)

        def aggregate(self):
            return self.getTypedRuleContext(AdaGrammarParser.AggregateContext,0)


        def qualified_expression(self):
            return self.getTypedRuleContext(AdaGrammarParser.Qualified_expressionContext,0)


        def function_call(self):
            return self.getTypedRuleContext(AdaGrammarParser.Function_callContext,0)


        def OTHERS(self):
            return self.getToken(AdaGrammarParser.OTHERS, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = AdaGrammarParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_primary)
        try:
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(AdaGrammarParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(AdaGrammarParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
                self.match(AdaGrammarParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 369
                self.match(AdaGrammarParser.CHAR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 370
                self.match(AdaGrammarParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 371
                self.match(AdaGrammarParser.LPAREN)
                self.state = 372
                self.expression()
                self.state = 373
                self.match(AdaGrammarParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 375
                self.match(AdaGrammarParser.NOT)
                self.state = 376
                self.primary()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 377
                self.match(AdaGrammarParser.ABS)
                self.state = 378
                self.primary()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 379
                self.match(AdaGrammarParser.NEW)
                self.state = 380
                self.match(AdaGrammarParser.ID)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 381
                self.match(AdaGrammarParser.NULL)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 382
                self.aggregate()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 383
                self.qualified_expression()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 384
                self.function_call()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 385
                self.match(AdaGrammarParser.OTHERS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(AdaGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AdaGrammarParser.RPAREN, 0)

        def element_association(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.Element_associationContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.Element_associationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.COMMA)
            else:
                return self.getToken(AdaGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_aggregate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregate" ):
                listener.enterAggregate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregate" ):
                listener.exitAggregate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregate" ):
                return visitor.visitAggregate(self)
            else:
                return visitor.visitChildren(self)




    def aggregate(self):

        localctx = AdaGrammarParser.AggregateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_aggregate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(AdaGrammarParser.LPAREN)
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125900233998338) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 1921) != 0):
                self.state = 389
                self.element_association()
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==65:
                    self.state = 390
                    self.match(AdaGrammarParser.COMMA)
                    self.state = 391
                    self.element_association()
                    self.state = 396
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 399
            self.match(AdaGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Qualified_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AdaGrammarParser.ID)
            else:
                return self.getToken(AdaGrammarParser.ID, i)

        def PERIOD(self):
            return self.getToken(AdaGrammarParser.PERIOD, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_qualified_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualified_expression" ):
                listener.enterQualified_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualified_expression" ):
                listener.exitQualified_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualified_expression" ):
                return visitor.visitQualified_expression(self)
            else:
                return visitor.visitChildren(self)




    def qualified_expression(self):

        localctx = AdaGrammarParser.Qualified_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_qualified_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(AdaGrammarParser.ID)
            self.state = 402
            self.match(AdaGrammarParser.PERIOD)
            self.state = 403
            self.match(AdaGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AdaGrammarParser.ID, 0)

        def LPAREN(self):
            return self.getToken(AdaGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(AdaGrammarParser.RPAREN, 0)

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
            return AdaGrammarParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = AdaGrammarParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(AdaGrammarParser.ID)
            self.state = 406
            self.match(AdaGrammarParser.LPAREN)
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125900233998338) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & 1921) != 0):
                self.state = 407
                self.expression()
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==65:
                    self.state = 408
                    self.match(AdaGrammarParser.COMMA)
                    self.state = 409
                    self.expression()
                    self.state = 414
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 417
            self.match(AdaGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_associationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AdaGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AdaGrammarParser.ExpressionContext,i)


        def ARROW(self):
            return self.getToken(AdaGrammarParser.ARROW, 0)

        def getRuleIndex(self):
            return AdaGrammarParser.RULE_element_association

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement_association" ):
                listener.enterElement_association(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement_association" ):
                listener.exitElement_association(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_association" ):
                return visitor.visitElement_association(self)
            else:
                return visitor.visitChildren(self)




    def element_association(self):

        localctx = AdaGrammarParser.Element_associationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_element_association)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.expression()
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==74:
                self.state = 420
                self.match(AdaGrammarParser.ARROW)
                self.state = 421
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





