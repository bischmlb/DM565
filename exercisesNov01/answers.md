## 1

**Consider allowing that the same identifier is used for a variable and a function in the same scope, i.e., one could in principle have a function call that looked like f(f). Discuss if it is possible to handle this and which changes should be made in SCIL to allow this if it is possible. Then consider if we could reasonably allow local variables in a function and formal parameters to have the same name. **

Vi skal ind og redigere i symboltable ```symbol.py```. Hvis vi ønsker at tillade variable navn og formal paramters at have samme navn, kunne man lave f.eks seperate lookup funktioner - en til variabler og en til parametre.

***

## 2

**Consider the construction (written in a style corresponding to the right-hand side of a grammar rule)**
```
signtest(E){
   neg:  S
   zero: S
   pos:  S
}
```
**The intention is that the expression E is evaluated and depending on the sign, one of three statements are executed. Consider which changes should be made in a compiler for the phases scanner, parser (AST), symbol collection, and type checking.**

Hvis man skulle implementere kunne man se det som 3 IF-statements  
eksempel:

```
if (E=0){
  S:zero
}else{
  if (E>0){
    pos
  }else{
    neg
  }
}
```

Lav et slags p_statement_signtest i parseren ```lexer_parser.py```, svarende til eksemplet.
Tilsvarende skal vi lave et AST, og ændre i ```AST.py```, for eksempel en ```class signtest```  
Symbolchecking og typechecking er ikke nødvendigt.  
Til sidst skal vi i codegeneration og lave en intermediate kode. eksempelvis:
```assembly
exec E
  pop reg1
  mov 0, reg2
  cmp reg1, reg2
  jmpE zero
  ....

```
***

## 3
**In SCIL, all functions must execute a return before terminating. However, such a return statement does not necessarily have to be located as the last statement in a sequence; it could, for instance, be placed in both branches of an if-then-else statement, or, in principle, just in one branch of an if-then-else statement, if we are certain that that branch will always be executed. Assume that we are interested in giving the user a warning if we think it is possible a return statement has been forgotten. Discuss what a reasonable strategy would be. Assume we implement this in SCIL in a separate phase. Consider representative language constructions and discuss what code to write in order to implement this feature. **

En måde at gøre dette på, ville være at åbne op for foreksempel typechecking og lave en postvisit function, der sikrer sig at en functions body har et return statement.

***

## 4
**
Consider a construction such as
**
```
for (i = 1; i < 100; i++){
   S
}
```

**Some programming languages will forbid changing the loop variable inside the loop, i.e., it is OK if S is print(i) or A[i] = i*i, but i = 42 or i -= 1 should be forbidden. What would be a good way to organize this check in the symbol collection / type checking phases?**

I symboltabellen, kan vi i symval_init tilføje en boolean der f.eks kunne hedde symval.mutable. Her skal vi bare huske at tjekke for hver value vi slår op, om den er mutable.

***

## 5
**In the type checking phase, we want to verify, among other things, that functions are called with the right number of parameters. Think about how you would do this for a function call f(1, 2, 3). What are the steps the compiler should go through? Does your method also work for, for example, f(0, 1, f(2, f(3, 4, 5), 6))? How is this handled in SCIL? **  

Vi kunne rekursivt tælle paramtrene, og gemme dem i en variabel. I ```type_checking.py``` er der for eksempel allerede en variabel der hedder ```self.number_of_actual_parameters = []```, som gemmer antallet af parametre, og appender dem til stacken som den møder dem.

***

## 6
**Change the scope rules of SCIL so that functions can only access their own variables or variables in the main scope. We still allow writing nested functions. Change the lookup function in symbols.py to make that change. Verify that the compiler still works fine for some programs such as factorial.src. Observe that the compiler also works for a program such as static_nested_scope.src, but now it works differently. Write a SCIL program that works with the original compiler, but is rejected after your change.**
