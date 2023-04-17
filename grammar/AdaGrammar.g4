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
ARRAY: 'array';
OF: 'of';
RECORD: 'record';
WITH: 'with';
SELECT: 'select';
WHEN: 'when';
OTHERS: 'others';
LOOP: 'loop';
EXIT: 'exit';
CONTINUE: 'continue';
RETURN: 'return';
THEN: 'then';
WHILE: 'while';

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

statementList: statement+
    ;

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
