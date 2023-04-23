grammar AdaGrammar;

/* TOKENS */

/* Keywords */
ABORT: 'abort';
ABS: 'abs';
ABSTRACT: 'abstract';
ACCEPT: 'accept';
ACCESS: 'access';
ALIASED: 'aliased';
ALL: 'all';
AND: 'and';
ARRAY: 'array';
AT: 'at';
BEGIN: 'begin';
BODY: 'body';
CASE: 'case';
CONSTANT: 'constant';
DECLARE: 'declare';
DELAY: 'delay';
DELTA: 'delta';
DIGITS: 'digits';
DO: 'do';
ELSE: 'else';
ELSIF: 'elsif';
END: 'end';
ENTRY: 'entry';
EXCEPTION: 'exception';
EXIT: 'exit';
FOR: 'for';
FUNCTION: 'function';
GENERIC: 'generic';
GOTO: 'goto';
IF: 'if';
IN: 'in';
INTERFACE: 'interface';
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
OUT: 'out';
OVERRIDING: 'overriding';
PACKAGE: 'package';
PRAGMA: 'pragma';
PRIVATE: 'private';
PROCEDURE: 'procedure';
PROTECTED: 'protected';
RAISE: 'raise';
RANGE: 'range';
RECORD: 'record';
REM: 'rem';
RENAMES: 'renames';
REQUEUE: 'requeue';
RETURN: 'return';
REVERSE: 'reverse';
SELECT: 'select';
SEPARATE: 'separate';
SOME: 'some';
SUBTYPE: 'subtype';
SYNCHRONIZED: 'synchronized';
TAGGED: 'tagged';
TASK: 'task';
TERMINATE: 'terminate';
THEN: 'then';
TYPE: 'type';
UNTIL: 'until';
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

/* Parser rules */

program: statementList;

statementList: statement+;

statement: assignment
         | procedureCall
         | conditionalStatement
         | loopStatement
         | exitStatement
         | returnStatement
         | nullStatement
         ;


expression: expression (AND | OR) expression
         | expression (LT | GT | LTE | GTE) expression
         | expression (ADD | SUB) expression
         | expression (MUL | DIV) expression
         | NOT expression
         | LPAREN expression RPAREN
         | ID
         | INT
         | FLOAT
         | CHAR
         | STRING
         ;

assignment: ID EQUALS expression SEMICOLON;

procedureCall: ID LPAREN argumentList RPAREN SEMICOLON;

argumentList: expression (COMMA expression)*;

conditionalStatement: IF expression THEN statementList (ELSE statementList)? END IF SEMICOLON;

loopStatement: WHILE expression LOOP statementList END LOOP SEMICOLON;

exitStatement: EXIT;

returnStatement: RETURN expression SEMICOLON;

nullStatement: SEMICOLON;
