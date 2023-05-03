grammar Ada;
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


/* Parser rules */

//tutaj oackage_use
program:
    (package_import
    | package_declaration
    | subprogram_declaration )*
    ;

package_declaration: PACKAGE ID IS 
    (package_declaration 
    | subprogram_declaration 
    | subprogram_body 
    | subunit)* END ID SEMICOLON
    ;

package_import: WITH ID PERIOD ID SEMICOLON;

package_use: USE ID PERIOD ID SEMICOLON;

subprogram_declaration: subprogram_specification;

subprogram_specification: subprogram_head IS 
    (subprogram_specification 
    | subprogram_declaration 
    | begin_end_block
    | sequence_of_statements
    | subunit)*  END ID SEMICOLON;

subprogram_head: PROCEDURE ID | FUNCTION ID  RETURN ID;


subprogram_body: subprogram_specification IS 
    (subprogram_specification 
    | subprogram_declaration 
    | subprogram_body 
    | subunit)*  END ID SEMICOLON
    ;

subunit: 
    subprogram_declaration 
    | subprogram_body 
    ;


type_declaration : TYPE ID IS type_definition SEMICOLON;

type_definition : 
    enumeration_type_definition 
    | array_type_definition 
    | record_type_definition 
    | subtype_definition;

enumeration_type_definition : LPAREN ID (COMMA ID)* RPAREN;

array_type_definition : ARRAY LPAREN index_subtype_definition (COMMA index_subtype_definition)* RPAREN OF component_subtype_definition;

index_subtype_definition : subtype_mark RANGE BOX;

subtype_mark : ID;

component_subtype_definition : subtype_mark;

record_type_definition : RECORD component_list END RECORD;

component_list : component_declaration (SEMICOLON component_declaration)*;

component_declaration : ID COLON subtype_mark;

subtype_definition : subtype_indication;

subtype_indication : subtype_mark (RANGE BOX)?;

constant_declaration : CONSTANT ID COLON subtype_mark ASSIGN expression SEMICOLON;

variable_declaration : ID COLON subtype_mark ASSIGN expression SEMICOLON;

expression : relation (AND relation | AND THEN relation | OR relation | OR ELSE relation | XOR relation )*;

relation: simple_expression (relational_operator | simple_expression)?;

relational_operator: 
    EQUALS | 
    NOTEQUALS 
    | LT 
    | GT 
    | LTE 
    | GTE;

simple_expression: term ((unary_adding_operator | binary_adding_operator) term)*;

unary_adding_operator: 
    ADD 
    | SUB
    ;

binary_adding_operator:  
    ADD 
    | SUB 
    | CONCAT;

term: factor ((MUL | DIV) factor)*;

factor: primary (POW primary)*
    | ABS primary
    | NOT primary
    ;

primary: 
    ID 
    | INT 
    | FLOAT 
    | CHAR 
    | STRING 
    | LPAREN expression RPAREN 
    | NOT primary 
    | ABS primary 
    | NEW subtype_mark 
    | NULL 
    | aggregate 
    | qualified_expression 
    | function_call;

aggregate : LPAREN (element_association (COMMA element_association)*)? RPAREN;

element_association : expression (ARROW expression)?;

qualified_expression : ID PERIOD ID;

function_call : ID LPAREN (actual_parameter (COMMA actual_parameter)*)? RPAREN;

actual_parameter : expression;

assignment_statement : target ASSIGN expression SEMICOLON;

target : ID;

procedure_call_statement : ID LPAREN (actual_parameter (COMMA actual_parameter)*)? RPAREN SEMICOLON;

sequence_of_statements : statement (SEMICOLON statement)*;

statement : 
    simple_statement 
    | if_statement 
    | case_statement 
    | loop_statement 
    | exit_statement 
    | return_statement 
    | null_statement ;

simple_statement : 
    assignment_statement 
    | procedure_call_statement;

if_statement : IF condition THEN sequence_of_statements (ELSIF condition THEN sequence_of_statements)* (ELSE sequence_of_statements)? END IF SEMICOLON;

condition : expression;

case_statement : CASE expression IS case_statement_alternative (case_statement_alternative)* END CASE SEMICOLON;

case_statement_alternative : WHEN (choice_list | OTHERS) ARROW sequence_of_statements;

choice_list : expression (COMMA expression)*;

loop_statement : 
    iteration_scheme 
    | while_loop
    | for_loop;

iteration_scheme :
    basic_loop 
    | for_loop 
    | while_loop;

basic_loop : LOOP sequence_of_statements END LOOP SEMICOLON;

for_loop : FOR ID IN discrete_range LOOP sequence_of_statements END LOOP SEMICOLON;

discrete_range : range;

range : simple_expression RANGE BOX simple_expression;

while_loop : WHILE condition LOOP sequence_of_statements END LOOP SEMICOLON;

begin_end_block : BEGIN sequence_of_statements END SEMICOLON;

exit_statement : EXIT ID? WHEN condition? SEMICOLON;

return_statement : RETURN expression? SEMICOLON;

null_statement : NULL SEMICOLON;