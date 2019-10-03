### 5

**1:**  
Allow user to choose between while and as_long_as.  

```py
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'as_long_as' : 'WHILE',
    'do': 'DO',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'var': 'VAR',
    'print': 'PRINT'
}
```

Added line ``` 'as_long_as' : 'WHILE' ``` which means we have multiple WHILE tokens. But is a solution, since the while statement is defined as:  

```py
def p_statement_while(t):
    'statement_while :  WHILE expression DO statement'
    t[0] = AST.statement_while(t[2], t[4], t.lexer.lineno)
```
As we can see, it basically just uses the WHILE token, which could both be *while* and *as_long_as* after out implementation of previous line.

**2:**  
Change end of statement symbol from semicolon to period.  

Change in line 48:
```py
t_SEMICOL = r'\.'
```
However, now it no longer allows ; as end of statement symbol.

**3:**  
Allow vertical lines for line up.  

```py
def t_vert_line(t):
    r'\|'
    pass
```
Does not check for context, but just allows the symbol.


Last 3 exercises allows for following program to be compiled:
```
var i
var s
var dummy

as_long_as i < 10 do {
|  print 0.
|  s = s + i.
|  i = i + 1.
|  if i == 10 then {
|  |  print 42.
|  } else {
|  |  dummy = 0.
|  }
}
````

**4:**  
```py
t.lexer.lineno += t.value.count("\n")
```
Above line actually counts amount of times \n appears as in the code, and uses that to keep track of linenumbers.
