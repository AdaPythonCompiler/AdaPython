parser grammar AdaGrammarParser;

options {tokenVocab=AdaGrammarLexer;}

/* Parser rules */

program: (
    package_import
    | package_use
    | program_declaration
)*;


program_declaration: program_head IS (
    // | program_declaration
    variable_declaration
    | full_variable_declaration
)* begin_end_block?;

variable_declaration: ID COLON type SEMICOLON;

full_variable_declaration: ID COLON type ASSIGN expression SEMICOLON;

type: INT | FLOAT | CHAR | STRING | ID;

package_import: WITH ID PERIOD ID SEMICOLON;

package_use: USE ID PERIOD ID SEMICOLON;

input_vars: LPAREN (ID COLON ID (COMMA ID COLON ID)*)? RPAREN;

program_head: PROCEDURE ID input_vars? | FUNCTION ID input_vars? RETURN ID;

begin_end_block : BEGIN (statement)* END ID SEMICOLON; // ID!!!

statement : 
    simple_statement 
    // | if_statement 
    // | case_statement 
    //| loop_statement 
    //| exit_statement 
    //| return_statement 
    //| null_statement
    ;

simple_statement : 
    assignment_statement 
    | procedure_call_statement
    //| function_call_statement

    ;
procedure_call_statement : ID LPAREN (expression (COMMA expression)*)? RPAREN SEMICOLON;

assignment_statement : ID ASSIGN expression SEMICOLON;

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
    | NEW ID 
    | NULL 
    | aggregate 
    | qualified_expression 
    | function_call;

aggregate : LPAREN (element_association (COMMA element_association)*)? RPAREN;

qualified_expression : ID PERIOD ID;

function_call : ID LPAREN (expression (COMMA expression)*)? RPAREN;

element_association : expression (ARROW expression)?;


// function Sum (A : Integer, B : Integer) return Integer is
// -- This function takes two integers as input and returns their sum
// begin
//     return A + B;
// end Sum;


// procedure Main is
//    --  Variable declarations
//    A, B : Integer := 0;
//    C    : Integer := 100;
//    D    : Integer;
// begin
//    --  Ada uses a regular assignment statement for incrementation.
//    A := A + 1;

//    --  Regular addition
//    D := A + B + C;
// end Main;


// procedure Proc
//  (Var1 : Integer;
//   Var2 : out Integer;
//   Var3 : in out Integer);