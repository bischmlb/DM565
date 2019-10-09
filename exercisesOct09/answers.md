### Exercise 2.4
**Give context-free grammars that generate the followinglanguages. In all parts, the alphabet Σ is {0,1}.**

*{w| w contains at least three 1s}*

```
S -> T1T1T1
T -> 0T | 1T | ε
```
*{w| w starts and ends with the same symbol}*

```
S -> 0T0 | 1T1
T -> 0T | 1T | ε
```

*{w| the length of w is odd}*

```
S -> 0T | 1T
T -> 0S | 1S | ε
```

*{w| the length of w is odd and its middle symbol is a 0}*

```
S -> 0S0 | 0S1 | 1S0 | 1S1 | 0
```

*{w| w = w^R, that is, w is a palindrome}*
```
S -> 0S0 | 1S1 | 1 | 0 | ε
```

*The empty set*
```
S -> S
```

### Exercise 2.6

*The set of strings over the alphabet {a,b} with more a’s than b’s*

```
S -> TaT
T -> TT | aTb | bTa | a | ε
```
*The complement of the language {anbn| n ≥ 0}*

For this exercise we have to split the language up in three. Remember complement MEANS NEGATED.  This means, we need the combinations for scenarios where we would either have more a's than b's, more b's than a's OR we would have a format that is not a followed by b. (so ba)

```
S -> S1 | S2 | S3
S1 -> aS1b | aS1 | a
S2 -> aS2b | S2b | b
S3 -> XbXaX
X -> aX | bX | ε
```

### Exercise 2.16
```
Concatenation:

Imagine two languages L1 L2
L1 = {a^nb^n}
L2 = {ww^R}
S1 -> aS1b | ε
S2 -> aS2a | bS2b | ε

L = {a^nb^n}{ww^R}
S -> S1S2
S1 -> aS1b | ε
S2 -> aS2a | bS2b | ε
```

```
Union:

Imagine two languages L1 L2
L1 = {a^ib^j | i > j }
L2 = {a^ib^j | i < j }
S1 -> aS1b | aS1 | a
S2 -> aS2b | S2b | b

L = {a^ib^j | i > j } | {a^ib^j | i < j }
S -> S1 | S2
S1 -> aS1b | aS1 | a
S2 -> aS2b | S2b | b
```

Ved star viser vi at den er closed fordi det er muligt at blive ved med at extende med en ny S combination.

```
Star
Imagine a language L
L = {a^ib^j | i > j }
S -> aS1b | aS1 | a

L = {a^ib^j | i > j }*
S1 -> SS1 | ε
```

### Problem 2.18

Forestil at vi producerer stringen ababab


```
S -> SS -> TS -> abS -> abSS -> abTS -> ababS -> ababT-> ababab
S -> SS -> SSS -> TSS -> abSS -> abTS -> ababS -> ababT -> ababab
```
Beskrivelse af grammar G:
```
L(G) = {a^nb^n | n >= 1}
```

lav S->SS om til S->TS. Grunden til den der ambiguous er fordi vi har forksellige left-most måder at generere T på.
