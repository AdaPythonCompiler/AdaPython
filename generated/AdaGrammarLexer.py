# Generated from grammar/AdaGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,81,554,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,
        23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,
        26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,
        39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,
        41,1,41,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,44,1,
        44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,
        46,1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,49,1,49,5,49,440,
        8,49,10,49,12,49,443,9,49,1,50,1,50,1,51,1,51,1,52,1,52,1,53,1,53,
        1,54,1,54,1,55,1,55,1,55,1,56,1,56,1,57,1,57,1,58,1,58,1,58,1,59,
        1,59,1,59,1,60,1,60,1,60,1,61,1,61,1,61,1,62,1,62,1,63,1,63,1,63,
        1,64,1,64,1,65,1,65,1,66,1,66,1,67,1,67,1,68,1,68,1,69,1,69,1,70,
        1,70,1,71,1,71,1,72,1,72,1,72,1,73,1,73,1,73,1,74,4,74,502,8,74,
        11,74,12,74,503,1,75,4,75,507,8,75,11,75,12,75,508,1,75,1,75,4,75,
        513,8,75,11,75,12,75,514,1,76,1,76,1,76,1,76,1,77,1,77,5,77,523,
        8,77,10,77,12,77,526,9,77,1,77,1,77,1,78,1,78,1,78,1,78,3,78,534,
        8,78,1,78,1,78,1,78,1,78,1,79,1,79,3,79,542,8,79,1,79,1,79,1,79,
        1,79,1,80,4,80,549,8,80,11,80,12,80,550,1,80,1,80,1,524,0,81,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,
        29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,
        51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,
        73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,
        95,48,97,49,99,50,101,51,103,52,105,53,107,54,109,55,111,56,113,
        57,115,58,117,59,119,60,121,61,123,62,125,63,127,64,129,65,131,66,
        133,67,135,68,137,69,139,70,141,71,143,72,145,73,147,74,149,75,151,
        76,153,77,155,78,157,79,159,80,161,81,1,0,4,2,0,65,90,97,122,4,0,
        48,57,65,90,95,95,97,122,1,0,48,57,3,0,9,10,13,13,32,32,561,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,
        0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,
        0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,
        0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,
        0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,
        0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,
        0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,
        0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,
        0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,
        111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,
        0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,
        1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,
        0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,
        0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,0,153,1,0,0,0,0,155,1,0,0,0,0,
        157,1,0,0,0,0,159,1,0,0,0,0,161,1,0,0,0,1,163,1,0,0,0,3,167,1,0,
        0,0,5,174,1,0,0,0,7,178,1,0,0,0,9,182,1,0,0,0,11,188,1,0,0,0,13,
        191,1,0,0,0,15,197,1,0,0,0,17,202,1,0,0,0,19,207,1,0,0,0,21,216,
        1,0,0,0,23,224,1,0,0,0,25,227,1,0,0,0,27,232,1,0,0,0,29,238,1,0,
        0,0,31,242,1,0,0,0,33,247,1,0,0,0,35,251,1,0,0,0,37,260,1,0,0,0,
        39,263,1,0,0,0,41,266,1,0,0,0,43,269,1,0,0,0,45,277,1,0,0,0,47,282,
        1,0,0,0,49,286,1,0,0,0,51,290,1,0,0,0,53,294,1,0,0,0,55,299,1,0,
        0,0,57,302,1,0,0,0,59,305,1,0,0,0,61,312,1,0,0,0,63,320,1,0,0,0,
        65,327,1,0,0,0,67,335,1,0,0,0,69,345,1,0,0,0,71,355,1,0,0,0,73,361,
        1,0,0,0,75,368,1,0,0,0,77,375,1,0,0,0,79,383,1,0,0,0,81,391,1,0,
        0,0,83,398,1,0,0,0,85,403,1,0,0,0,87,408,1,0,0,0,89,413,1,0,0,0,
        91,417,1,0,0,0,93,422,1,0,0,0,95,428,1,0,0,0,97,433,1,0,0,0,99,437,
        1,0,0,0,101,444,1,0,0,0,103,446,1,0,0,0,105,448,1,0,0,0,107,450,
        1,0,0,0,109,452,1,0,0,0,111,454,1,0,0,0,113,457,1,0,0,0,115,459,
        1,0,0,0,117,461,1,0,0,0,119,464,1,0,0,0,121,467,1,0,0,0,123,470,
        1,0,0,0,125,473,1,0,0,0,127,475,1,0,0,0,129,478,1,0,0,0,131,480,
        1,0,0,0,133,482,1,0,0,0,135,484,1,0,0,0,137,486,1,0,0,0,139,488,
        1,0,0,0,141,490,1,0,0,0,143,492,1,0,0,0,145,494,1,0,0,0,147,497,
        1,0,0,0,149,501,1,0,0,0,151,506,1,0,0,0,153,516,1,0,0,0,155,520,
        1,0,0,0,157,529,1,0,0,0,159,539,1,0,0,0,161,548,1,0,0,0,163,164,
        5,97,0,0,164,165,5,98,0,0,165,166,5,115,0,0,166,2,1,0,0,0,167,168,
        5,97,0,0,168,169,5,99,0,0,169,170,5,99,0,0,170,171,5,101,0,0,171,
        172,5,115,0,0,172,173,5,115,0,0,173,4,1,0,0,0,174,175,5,97,0,0,175,
        176,5,108,0,0,176,177,5,108,0,0,177,6,1,0,0,0,178,179,5,97,0,0,179,
        180,5,110,0,0,180,181,5,100,0,0,181,8,1,0,0,0,182,183,5,97,0,0,183,
        184,5,114,0,0,184,185,5,114,0,0,185,186,5,97,0,0,186,187,5,121,0,
        0,187,10,1,0,0,0,188,189,5,97,0,0,189,190,5,116,0,0,190,12,1,0,0,
        0,191,192,5,98,0,0,192,193,5,101,0,0,193,194,5,103,0,0,194,195,5,
        105,0,0,195,196,5,110,0,0,196,14,1,0,0,0,197,198,5,98,0,0,198,199,
        5,111,0,0,199,200,5,100,0,0,200,201,5,121,0,0,201,16,1,0,0,0,202,
        203,5,99,0,0,203,204,5,97,0,0,204,205,5,115,0,0,205,206,5,101,0,
        0,206,18,1,0,0,0,207,208,5,99,0,0,208,209,5,111,0,0,209,210,5,110,
        0,0,210,211,5,115,0,0,211,212,5,116,0,0,212,213,5,97,0,0,213,214,
        5,110,0,0,214,215,5,116,0,0,215,20,1,0,0,0,216,217,5,100,0,0,217,
        218,5,101,0,0,218,219,5,99,0,0,219,220,5,108,0,0,220,221,5,97,0,
        0,221,222,5,114,0,0,222,223,5,101,0,0,223,22,1,0,0,0,224,225,5,100,
        0,0,225,226,5,111,0,0,226,24,1,0,0,0,227,228,5,101,0,0,228,229,5,
        108,0,0,229,230,5,115,0,0,230,231,5,101,0,0,231,26,1,0,0,0,232,233,
        5,101,0,0,233,234,5,108,0,0,234,235,5,115,0,0,235,236,5,105,0,0,
        236,237,5,102,0,0,237,28,1,0,0,0,238,239,5,101,0,0,239,240,5,110,
        0,0,240,241,5,100,0,0,241,30,1,0,0,0,242,243,5,101,0,0,243,244,5,
        120,0,0,244,245,5,105,0,0,245,246,5,116,0,0,246,32,1,0,0,0,247,248,
        5,102,0,0,248,249,5,111,0,0,249,250,5,114,0,0,250,34,1,0,0,0,251,
        252,5,102,0,0,252,253,5,117,0,0,253,254,5,110,0,0,254,255,5,99,0,
        0,255,256,5,116,0,0,256,257,5,105,0,0,257,258,5,111,0,0,258,259,
        5,110,0,0,259,36,1,0,0,0,260,261,5,105,0,0,261,262,5,102,0,0,262,
        38,1,0,0,0,263,264,5,105,0,0,264,265,5,110,0,0,265,40,1,0,0,0,266,
        267,5,105,0,0,267,268,5,115,0,0,268,42,1,0,0,0,269,270,5,108,0,0,
        270,271,5,105,0,0,271,272,5,109,0,0,272,273,5,105,0,0,273,274,5,
        116,0,0,274,275,5,101,0,0,275,276,5,100,0,0,276,44,1,0,0,0,277,278,
        5,108,0,0,278,279,5,111,0,0,279,280,5,111,0,0,280,281,5,112,0,0,
        281,46,1,0,0,0,282,283,5,109,0,0,283,284,5,111,0,0,284,285,5,100,
        0,0,285,48,1,0,0,0,286,287,5,110,0,0,287,288,5,101,0,0,288,289,5,
        119,0,0,289,50,1,0,0,0,290,291,5,110,0,0,291,292,5,111,0,0,292,293,
        5,116,0,0,293,52,1,0,0,0,294,295,5,110,0,0,295,296,5,117,0,0,296,
        297,5,108,0,0,297,298,5,108,0,0,298,54,1,0,0,0,299,300,5,111,0,0,
        300,301,5,102,0,0,301,56,1,0,0,0,302,303,5,111,0,0,303,304,5,114,
        0,0,304,58,1,0,0,0,305,306,5,111,0,0,306,307,5,116,0,0,307,308,5,
        104,0,0,308,309,5,101,0,0,309,310,5,114,0,0,310,311,5,115,0,0,311,
        60,1,0,0,0,312,313,5,112,0,0,313,314,5,97,0,0,314,315,5,99,0,0,315,
        316,5,107,0,0,316,317,5,97,0,0,317,318,5,103,0,0,318,319,5,101,0,
        0,319,62,1,0,0,0,320,321,5,112,0,0,321,322,5,114,0,0,322,323,5,97,
        0,0,323,324,5,103,0,0,324,325,5,109,0,0,325,326,5,97,0,0,326,64,
        1,0,0,0,327,328,5,112,0,0,328,329,5,114,0,0,329,330,5,105,0,0,330,
        331,5,118,0,0,331,332,5,97,0,0,332,333,5,116,0,0,333,334,5,101,0,
        0,334,66,1,0,0,0,335,336,5,112,0,0,336,337,5,114,0,0,337,338,5,111,
        0,0,338,339,5,99,0,0,339,340,5,101,0,0,340,341,5,100,0,0,341,342,
        5,117,0,0,342,343,5,114,0,0,343,344,5,101,0,0,344,68,1,0,0,0,345,
        346,5,112,0,0,346,347,5,114,0,0,347,348,5,111,0,0,348,349,5,116,
        0,0,349,350,5,101,0,0,350,351,5,99,0,0,351,352,5,116,0,0,352,353,
        5,101,0,0,353,354,5,100,0,0,354,70,1,0,0,0,355,356,5,114,0,0,356,
        357,5,97,0,0,357,358,5,110,0,0,358,359,5,103,0,0,359,360,5,101,0,
        0,360,72,1,0,0,0,361,362,5,114,0,0,362,363,5,101,0,0,363,364,5,99,
        0,0,364,365,5,111,0,0,365,366,5,114,0,0,366,367,5,100,0,0,367,74,
        1,0,0,0,368,369,5,114,0,0,369,370,5,101,0,0,370,371,5,116,0,0,371,
        372,5,117,0,0,372,373,5,114,0,0,373,374,5,110,0,0,374,76,1,0,0,0,
        375,376,5,114,0,0,376,377,5,101,0,0,377,378,5,118,0,0,378,379,5,
        101,0,0,379,380,5,114,0,0,380,381,5,115,0,0,381,382,5,101,0,0,382,
        78,1,0,0,0,383,384,5,115,0,0,384,385,5,117,0,0,385,386,5,98,0,0,
        386,387,5,116,0,0,387,388,5,121,0,0,388,389,5,112,0,0,389,390,5,
        101,0,0,390,80,1,0,0,0,391,392,5,116,0,0,392,393,5,97,0,0,393,394,
        5,103,0,0,394,395,5,103,0,0,395,396,5,101,0,0,396,397,5,100,0,0,
        397,82,1,0,0,0,398,399,5,116,0,0,399,400,5,97,0,0,400,401,5,115,
        0,0,401,402,5,107,0,0,402,84,1,0,0,0,403,404,5,116,0,0,404,405,5,
        104,0,0,405,406,5,101,0,0,406,407,5,110,0,0,407,86,1,0,0,0,408,409,
        5,116,0,0,409,410,5,121,0,0,410,411,5,112,0,0,411,412,5,101,0,0,
        412,88,1,0,0,0,413,414,5,117,0,0,414,415,5,115,0,0,415,416,5,101,
        0,0,416,90,1,0,0,0,417,418,5,119,0,0,418,419,5,104,0,0,419,420,5,
        101,0,0,420,421,5,110,0,0,421,92,1,0,0,0,422,423,5,119,0,0,423,424,
        5,104,0,0,424,425,5,105,0,0,425,426,5,108,0,0,426,427,5,101,0,0,
        427,94,1,0,0,0,428,429,5,119,0,0,429,430,5,105,0,0,430,431,5,116,
        0,0,431,432,5,104,0,0,432,96,1,0,0,0,433,434,5,120,0,0,434,435,5,
        111,0,0,435,436,5,114,0,0,436,98,1,0,0,0,437,441,7,0,0,0,438,440,
        7,1,0,0,439,438,1,0,0,0,440,443,1,0,0,0,441,439,1,0,0,0,441,442,
        1,0,0,0,442,100,1,0,0,0,443,441,1,0,0,0,444,445,5,43,0,0,445,102,
        1,0,0,0,446,447,5,45,0,0,447,104,1,0,0,0,448,449,5,42,0,0,449,106,
        1,0,0,0,450,451,5,47,0,0,451,108,1,0,0,0,452,453,5,61,0,0,453,110,
        1,0,0,0,454,455,5,47,0,0,455,456,5,61,0,0,456,112,1,0,0,0,457,458,
        5,60,0,0,458,114,1,0,0,0,459,460,5,62,0,0,460,116,1,0,0,0,461,462,
        5,60,0,0,462,463,5,61,0,0,463,118,1,0,0,0,464,465,5,62,0,0,465,466,
        5,61,0,0,466,120,1,0,0,0,467,468,5,60,0,0,468,469,5,62,0,0,469,122,
        1,0,0,0,470,471,5,58,0,0,471,472,5,61,0,0,472,124,1,0,0,0,473,474,
        5,38,0,0,474,126,1,0,0,0,475,476,5,42,0,0,476,477,5,42,0,0,477,128,
        1,0,0,0,478,479,5,44,0,0,479,130,1,0,0,0,480,481,5,59,0,0,481,132,
        1,0,0,0,482,483,5,58,0,0,483,134,1,0,0,0,484,485,5,40,0,0,485,136,
        1,0,0,0,486,487,5,41,0,0,487,138,1,0,0,0,488,489,5,91,0,0,489,140,
        1,0,0,0,490,491,5,93,0,0,491,142,1,0,0,0,492,493,5,46,0,0,493,144,
        1,0,0,0,494,495,5,46,0,0,495,496,5,46,0,0,496,146,1,0,0,0,497,498,
        5,61,0,0,498,499,5,62,0,0,499,148,1,0,0,0,500,502,7,2,0,0,501,500,
        1,0,0,0,502,503,1,0,0,0,503,501,1,0,0,0,503,504,1,0,0,0,504,150,
        1,0,0,0,505,507,7,2,0,0,506,505,1,0,0,0,507,508,1,0,0,0,508,506,
        1,0,0,0,508,509,1,0,0,0,509,510,1,0,0,0,510,512,5,46,0,0,511,513,
        7,2,0,0,512,511,1,0,0,0,513,514,1,0,0,0,514,512,1,0,0,0,514,515,
        1,0,0,0,515,152,1,0,0,0,516,517,5,39,0,0,517,518,9,0,0,0,518,519,
        5,39,0,0,519,154,1,0,0,0,520,524,5,34,0,0,521,523,9,0,0,0,522,521,
        1,0,0,0,523,526,1,0,0,0,524,525,1,0,0,0,524,522,1,0,0,0,525,527,
        1,0,0,0,526,524,1,0,0,0,527,528,5,34,0,0,528,156,1,0,0,0,529,530,
        5,45,0,0,530,531,5,45,0,0,531,533,1,0,0,0,532,534,9,0,0,0,533,532,
        1,0,0,0,533,534,1,0,0,0,534,535,1,0,0,0,535,536,5,10,0,0,536,537,
        1,0,0,0,537,538,6,78,0,0,538,158,1,0,0,0,539,541,5,47,0,0,540,542,
        9,0,0,0,541,540,1,0,0,0,541,542,1,0,0,0,542,543,1,0,0,0,543,544,
        5,47,0,0,544,545,1,0,0,0,545,546,6,79,0,0,546,160,1,0,0,0,547,549,
        7,3,0,0,548,547,1,0,0,0,549,550,1,0,0,0,550,548,1,0,0,0,550,551,
        1,0,0,0,551,552,1,0,0,0,552,553,6,80,0,0,553,162,1,0,0,0,9,0,441,
        503,508,514,524,533,541,550,1,6,0,0
    ]

class AdaGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ABS = 1
    ACCESS = 2
    ALL = 3
    AND = 4
    ARRAY = 5
    AT = 6
    BEGIN = 7
    BODY = 8
    CASE = 9
    CONSTANT = 10
    DECLARE = 11
    DO = 12
    ELSE = 13
    ELSIF = 14
    END = 15
    EXIT = 16
    FOR = 17
    FUNCTION = 18
    IF = 19
    IN = 20
    IS = 21
    LIMITED = 22
    LOOP = 23
    MOD = 24
    NEW = 25
    NOT = 26
    NULL = 27
    OF = 28
    OR = 29
    OTHERS = 30
    PACKAGE = 31
    PRAGMA = 32
    PRIVATE = 33
    PROCEDURE = 34
    PROTECTED = 35
    RANGE = 36
    RECORD = 37
    RETURN = 38
    REVERSE = 39
    SUBTYPE = 40
    TAGGED = 41
    TASK = 42
    THEN = 43
    TYPE = 44
    USE = 45
    WHEN = 46
    WHILE = 47
    WITH = 48
    XOR = 49
    ID = 50
    ADD = 51
    SUB = 52
    MUL = 53
    DIV = 54
    EQUALS = 55
    NOTEQUALS = 56
    LT = 57
    GT = 58
    LTE = 59
    GTE = 60
    BOX = 61
    ASSIGN = 62
    CONCAT = 63
    POW = 64
    COMMA = 65
    SEMICOLON = 66
    COLON = 67
    LPAREN = 68
    RPAREN = 69
    LEFT_BRACKET = 70
    RIGHT_BRACKET = 71
    PERIOD = 72
    DOT_DOT = 73
    ARROW = 74
    INT = 75
    FLOAT = 76
    CHAR = 77
    STRING = 78
    LINE_COMMENT = 79
    BLOCK_COMMENT = 80
    WS = 81

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'abs'", "'access'", "'all'", "'and'", "'array'", "'at'", "'begin'", 
            "'body'", "'case'", "'constant'", "'declare'", "'do'", "'else'", 
            "'elsif'", "'end'", "'exit'", "'for'", "'function'", "'if'", 
            "'in'", "'is'", "'limited'", "'loop'", "'mod'", "'new'", "'not'", 
            "'null'", "'of'", "'or'", "'others'", "'package'", "'pragma'", 
            "'private'", "'procedure'", "'protected'", "'range'", "'record'", 
            "'return'", "'reverse'", "'subtype'", "'tagged'", "'task'", 
            "'then'", "'type'", "'use'", "'when'", "'while'", "'with'", 
            "'xor'", "'+'", "'-'", "'*'", "'/'", "'='", "'/='", "'<'", "'>'", 
            "'<='", "'>='", "'<>'", "':='", "'&'", "'**'", "','", "';'", 
            "':'", "'('", "')'", "'['", "']'", "'.'", "'..'", "'=>'" ]

    symbolicNames = [ "<INVALID>",
            "ABS", "ACCESS", "ALL", "AND", "ARRAY", "AT", "BEGIN", "BODY", 
            "CASE", "CONSTANT", "DECLARE", "DO", "ELSE", "ELSIF", "END", 
            "EXIT", "FOR", "FUNCTION", "IF", "IN", "IS", "LIMITED", "LOOP", 
            "MOD", "NEW", "NOT", "NULL", "OF", "OR", "OTHERS", "PACKAGE", 
            "PRAGMA", "PRIVATE", "PROCEDURE", "PROTECTED", "RANGE", "RECORD", 
            "RETURN", "REVERSE", "SUBTYPE", "TAGGED", "TASK", "THEN", "TYPE", 
            "USE", "WHEN", "WHILE", "WITH", "XOR", "ID", "ADD", "SUB", "MUL", 
            "DIV", "EQUALS", "NOTEQUALS", "LT", "GT", "LTE", "GTE", "BOX", 
            "ASSIGN", "CONCAT", "POW", "COMMA", "SEMICOLON", "COLON", "LPAREN", 
            "RPAREN", "LEFT_BRACKET", "RIGHT_BRACKET", "PERIOD", "DOT_DOT", 
            "ARROW", "INT", "FLOAT", "CHAR", "STRING", "LINE_COMMENT", "BLOCK_COMMENT", 
            "WS" ]

    ruleNames = [ "ABS", "ACCESS", "ALL", "AND", "ARRAY", "AT", "BEGIN", 
                  "BODY", "CASE", "CONSTANT", "DECLARE", "DO", "ELSE", "ELSIF", 
                  "END", "EXIT", "FOR", "FUNCTION", "IF", "IN", "IS", "LIMITED", 
                  "LOOP", "MOD", "NEW", "NOT", "NULL", "OF", "OR", "OTHERS", 
                  "PACKAGE", "PRAGMA", "PRIVATE", "PROCEDURE", "PROTECTED", 
                  "RANGE", "RECORD", "RETURN", "REVERSE", "SUBTYPE", "TAGGED", 
                  "TASK", "THEN", "TYPE", "USE", "WHEN", "WHILE", "WITH", 
                  "XOR", "ID", "ADD", "SUB", "MUL", "DIV", "EQUALS", "NOTEQUALS", 
                  "LT", "GT", "LTE", "GTE", "BOX", "ASSIGN", "CONCAT", "POW", 
                  "COMMA", "SEMICOLON", "COLON", "LPAREN", "RPAREN", "LEFT_BRACKET", 
                  "RIGHT_BRACKET", "PERIOD", "DOT_DOT", "ARROW", "INT", 
                  "FLOAT", "CHAR", "STRING", "LINE_COMMENT", "BLOCK_COMMENT", 
                  "WS" ]

    grammarFileName = "AdaGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


