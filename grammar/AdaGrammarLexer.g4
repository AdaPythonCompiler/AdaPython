lexer grammar AdaGrammarLexer;
/* Keywords from book*/
ABS: 'abs';
ACCESS: 'access';
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
LIMITED: 'limited';
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
PROTECTED: 'protected';
RANGE: 'range';
RECORD: 'record';
RETURN: 'return';
REVERSE: 'reverse';
SUBTYPE: 'subtype';
TAGGED: 'tagged';
TASK: 'task';
THEN: 'then';
TYPE: 'type';
USE: 'use';
WHEN: 'when';
WHILE: 'while';
WITH: 'with';
XOR: 'xor';

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