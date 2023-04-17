grammar AdaGrammar;

/* TOKENS */

/* Keywords */
PROGRAM: 'program';
BEGIN: 'begin';
END: 'end';
IF: 'if';
ELSE: 'else';
PROCEDURE: 'procedure';
FUNCTION: 'function';
IS: 'is';
TYPE: 'type';


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
AND: 'and';
OR: 'or';
NOT: 'not';

/* Punctuation */
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
LPAREN: '(';
RPAREN: ')';
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

/* Parser rules */
