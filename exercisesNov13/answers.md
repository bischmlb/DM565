### 1
**Extend SCIL with a new construction  
repeat 〈statement_list〉 until 〈expression〉  
You must go through all the relevant phases. You can get significant inspiration from considering the while-loop equivalent.**

Først skal vi ind i parseren, og sørge for at den genkende vores to nye udtryk, **repeat** og **until**. Dette gøres i ```lexer_parser.py```  
Brug udtrykket for while som inspiration.  
Brug while i ```AST.py``` som inspiration.  
I ```pretty_printer.py``` kan vi igen alternate while, så vores nye repeat <statement> until <expression> kan printes.  
I ```code_generation.py``` skal vi nu sørge for at vores nye construction skal oversættes til assembler kode. Igen matcher vi mere eller mindre ```while```. Det eneste vi potientielt skal ændre på, er hvornår vi sammenligner udtryk.


***
### 2
**It is a little annoying to have to declare a variable and write dummy = f() in situations where we do not really want the function to return any value. Change this in SCIL by allowing an expression as a statement. It is ok (and easiest) to still require that all functions return a value. At the point where you now do not use the value, you should remember to pop it off the stack.**

Vi kan adde statement_expression til vores parser.  
I ```AST.py``` skal vi sørge for at den skal gemme vores expression.  
pretty printer ...



***

### 3

**Discuss how to add break and continue statements to while-loops so they can be used as illustrated below, where we add positive values from an array until reaching the (stop) value zero.**
```
i = -1;
sum = 0;
while i+1 < length(A) do{
   i += 1;
   if A[i] == 0 then break;
   if A[i] < 0 then continue;
   sum += A[i];
}
```
**Discuss what would be needed in the different phases of SCIL to add this feature. (Note that the motivating program example is not a SCIL program, but this is irrelevant for the discussion of how to add the feature, and we just assume that SCIL already has arrays, etc.)**

**After this discussion, consider nested while-loops using these features. How should it work, and does your solution supply the right functionality?**

Brug ```symbols.py``` og brug anvendte labels i while løkke i ```code_generation.py``` til at jumpe til ønskede conclusion, alt efter om break eller continue.

***
### 4
**Discuss what should be done in the different phases if we wanted to add the type boolean and allow the operators and, or, and not.**

***

### 5
**Discuss how C-style for-loops could be added to SCIL via syntactic sugar.**

***

### 6
**It will not be covered at the exercises, but implementing any of the above-mentioned extra features in SCIL will of course only boost your understanding of compiler construction.**

***
