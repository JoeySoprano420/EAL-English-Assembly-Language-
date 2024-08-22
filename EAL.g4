grammar EAL;

// Parser rules
program: statement+ ;
statement: declaration | operation | condition | loop | functionCall | comment ;
declaration: 'declare' type ID '=' expression ';' ;
operation: 'mov' ID ',' expression | 'add' ID ',' expression ;
condition: 'if' expression 'is' comparison 'then' statement ('else' statement)? ;
loop: 'repeat' expression 'times' statement ;
functionCall: 'call' ID '(' (expression (',' expression)*)? ')' ;
print: 'print' STRING ;
comment: '>>' (.*? '\n') ;

expression: NUMBER | ID ;
comparison: 'greater' 'than' NUMBER | 'less' 'than' NUMBER | 'equal' 'to' NUMBER ;

type: 'int' | 'float' | 'string' | 'bool' ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;
STRING: '"' [a-zA-Z0-9 ]* '"' ;
WS: [ \t\n]+ -> skip ;
