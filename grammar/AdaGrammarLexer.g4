lexer grammar AdaGrammarLexer;
/* Keywords from book*/
ABS: 'abs';
ALL: 'all';
AND: 'and';
ARRAY: 'array';
AT: 'at';
BEGIN: 'begin';
BODY: 'body';
CASE: 'case';
CONSTANT: 'constant';
DECLARE: 'declare';
DO: 'do';
ELSE: 'else';
ELSIF: 'elsif';
END: 'end';
EXIT: 'exit';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
IN: 'in';
IS: 'is';
LOOP: 'loop';
MOD: 'mod';
NEW: 'new';
NOT: 'not';
NULL: 'null';
OF: 'of';
OR: 'or';
OTHERS: 'others';
PACKAGE: 'package';
PRAGMA: 'pragma';
PRIVATE: 'private';
PROCEDURE: 'procedure';
RANGE: 'range';
RECORD: 'record';
RETURN: 'return';
REVERSE: 'reverse';
SUBTYPE: 'subtype';
THEN: 'then';
TYPE: 'type';
USE: 'use';
WHEN: 'when';
WHILE: 'while';
WITH: 'with';
XOR: 'xor';
INT_TYPE: 'Integer';
FLOAT_TYPE: 'Float';
CHAR_TYPE: 'Char';
STRING_TYPE: 'String';
BOOLEAN_TYPE: 'Boolean';
/* Identifiers */
ID: [a-zA-Z] [a-zA-Z0-9_]*;

/* Operators */
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
EQUALS: '=';
NOTEQUALS: '/=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
BOX: '<>';
ASSIGN: ':=';
CONCAT: '&';
POW: '**';

/* Punctuation */
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
LPAREN: '(';
RPAREN: ')';
LEFT_BRACKET: '['  ;
RIGHT_BRACKET: ']'  ;
PERIOD: '.';
DOT_DOT: '..' ;
ARROW: '=>';


/* LITERALS */
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
CHAR: '\'' . '\'';
STRING: '"' .*? '"';

/* Comments */
LINE_COMMENT: '--' .? '\n' -> skip;
BLOCK_COMMENT: '/' .? '/' -> skip;

/* Whitespace */
WS: [ \t\r\n]+ -> skip;