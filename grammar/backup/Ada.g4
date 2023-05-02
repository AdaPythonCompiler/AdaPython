grammar Ada;

// Keywords
IF: 'if';
THEN: 'then';
ELSE: 'else';
END_IF: 'end' 'if';
LOOP: 'loop';
END_LOOP: 'end' 'loop';
EXIT: 'exit';
TYPE: 'type';
IS: 'is';
END: 'end';
RECORD: 'record';
ARRAY: 'array';
OF: 'of';
RANGE: 'range';
TO: 'to';
NOT: 'not';
RETURN: 'return';
PROCEDURE: 'procedure';
INTEGER: 'integer';
FLOAT: 'float';
CHARACTER: 'character';
BOOLEAN: 'boolean';
WHILE: 'while';
FOR: 'for';
IN: 'in';
REVERSE: 'reverse';
BEGIN: 'begin';

// Operators and Punctuation
ASSIGN: ':=';
SEMI: ';';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MOD: 'mod';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
COLON: ':';
DOT_DOT: '..' ;

// Literals
ID: [a-zA-Z] [a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT_LITERAL: [0-9]+ '.' [0-9]+;
CHAR: '\'' . '\'';
STRING: '"' .*? '"';
BOOL_LITERAL: 'true' | 'false';

// Boolean Operators
AND: 'and';
OR: 'or';

// Comparison Operators
EQ: '=';
NEQ: '/=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';

// Whitespace and Comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '--' ~[\r\n]* -> skip;

// Rules
prog: stmt*;

stmt: assignment
    | if_stmt
    | loop_stmt
    | exit_stmt
    | while_loop
    | for_loop
    | return_stmt
    | proc_call
    | proc_def
    ;

assignment: ID ASSIGN expr SEMI;

if_stmt: IF bool_expr THEN stmt* (ELSE stmt*)? END_IF;

loop_stmt: LOOP stmt* END_LOOP;

while_loop : WHILE bool_expr LOOP stmt* END LOOP SEMI;

for_loop : FOR ID IN (expr (REVERSE)? RANGE expr) LOOP stmt* END LOOP SEMI;

exit_stmt: EXIT SEMI;

return_stmt: RETURN expr SEMI;

begin_stmt: BEGIN stmt* END SEMI;

proc_call: ID LPAREN (expr (COMMA expr)*)? RPAREN SEMI;

proc_def: PROCEDURE ID (LPAREN (param (COMMA param)*)? RPAREN)? IS stmt* END ID SEMI;

param: ID COLON param_type;

param_type: 
    INTEGER
    | BOOLEAN
    | FLOAT
    | CHARACTER
    ;

type_def: TYPE ID IS type_decl SEMI;

type_decl: scalar_type
         | array_type
         // Add more type declarations as needed
         ;

scalar_type: INTEGER
           | FLOAT
           | CHARACTER
           | BOOLEAN
           // Add more scalar types as needed
           ;

array_type: ARRAY LPAREN index_spec RPAREN OF type_decl;

index_spec: discrete_range (COMMA discrete_range)*;

discrete_range: ID RANGE expr DOT_DOT expr;

expr: term ((PLUS | MINUS) term)*;

term: factor ((MULTIPLY | DIVIDE | MOD) factor)*;

factor: LPAREN expr RPAREN
      | ID
      | INT
      | FLOAT_LITERAL
      | CHAR
      | STRING
      | BOOL_LITERAL
      | NOT factor
      ;

bool_expr: bool_term ((AND | OR) bool_term)*;

bool_term: bool_factor ((EQ | NEQ | LT | LTE | GT | GTE) bool_factor)*;

bool_factor: LPAREN bool_expr RPAREN
           | ID
           | INT
           | FLOAT_LITERAL
           | CHAR
           | STRING
           | BOOL_LITERAL
           | NOT bool_factor
           ;

