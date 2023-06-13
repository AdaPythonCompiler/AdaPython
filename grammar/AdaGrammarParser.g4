parser grammar AdaGrammarParser;

options {tokenVocab=AdaGrammarLexer;}

/* Parser rules */

program: (
    package_import
    | package_use
    | program_declaration
)*;

package_import: WITH ID PERIOD ID SEMICOLON;

package_use: USE ID PERIOD ID SEMICOLON;

program_declaration: program_head IS (
    variable_declaration
    | type_array_declaration
    | full_variable_declaration
    | program_declaration
)* begin_end_block?;

program_head: PROCEDURE ID input_vars? | FUNCTION ID input_vars? RETURN ID;

input_vars: LPAREN (ID COLON ID (COMMA ID COLON ID)*)? RPAREN;

variable_declaration: ID COLON type SEMICOLON;

full_variable_declaration: ID COLON type ASSIGN expression SEMICOLON;

type_array_declaration: TYPE ID IS RANGE simple_expression DOT_DOT simple_expression SEMICOLON;

type: INT_TYPE | FLOAT_TYPE | CHAR_TYPE | STRING_TYPE | BOOLEAN_TYPE | ID;

begin_end_block : (BEGIN (statement)*)? END ID SEMICOLON; // ID!!!

statement : 
    (simple_statement
    | if_statement
    | loop_statement 
    | case_statement
    );

if_statement : IF expression THEN (statement)* (elsif_statement)* (else_statement)? END IF SEMICOLON;

elsif_statement : ELSIF expression THEN (statement)*;

else_statement : ELSE (statement)*;

loop_statement :
    basic_loop 
    | for_loop 
    | while_loop;

basic_loop : LOOP (statement)* END LOOP SEMICOLON;

for_loop : FOR ID IN range LOOP (statement)* END LOOP SEMICOLON;

range : simple_expression DOT_DOT simple_expression;

while_loop : WHILE expression LOOP (statement)* END LOOP SEMICOLON;

case_statement : CASE expression IS (case_statement_alternative)* END CASE SEMICOLON;

case_statement_alternative : WHEN expression ARROW (statement)*;


simple_statement : 
    assignment_statement 
    | procedure_call_statement
    ;
procedure_call_statement : ID LPAREN (expression (COMMA expression)*)? RPAREN SEMICOLON;

assignment_statement : ID ASSIGN expression SEMICOLON;

expression : relation (AND relation | AND THEN relation | OR relation | OR ELSE relation | XOR relation )*;

relation: simple_expression (relational_operator simple_expression)?;

relational_operator: 
    EQUALS | 
    NOTEQUALS 
    | LT 
    | GT 
    | LTE 
    | GTE;

simple_expression: term ((unary_adding_operator | binary_adding_operator) term)* ;

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
    | NEW ID 
    | NULL 
    | aggregate 
    | qualified_expression 
    | function_call
    | OTHERS;

aggregate : LPAREN (element_association (COMMA element_association)*)? RPAREN;

qualified_expression : ID PERIOD ID;

function_call : ID LPAREN (expression (COMMA expression)*)? RPAREN;

element_association : expression (ARROW expression)?;
