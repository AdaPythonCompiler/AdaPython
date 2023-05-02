import sys
from antlr4 import *

from generated.AdaGrammarLexer import AdaGrammarLexer
from generated.AdaGrammarParser import AdaGrammarParser
from generated.AdaGrammarParserVisitor import AdaGrammarParserVisitor


class AdaVisitor(AdaGrammarParserVisitor):
    pass
