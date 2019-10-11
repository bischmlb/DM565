
### 3.5

|    | Nullable | FIRST                     | FOLLOW                       |
|----|----------|---------------------------|------------------------------|
| S' | false    | $, {, WORD, begin, \, end | -                            |
| S  | true     | {, w, begin, end, \       | \, $, }                      |
| B  | false    | \                         | {, WORD, begin, end, \       |
| E  | false    | \                         | {, WORD, begin, end, \, $, } |
| X  | false    | {, WORD, begin, end, \    | {, WORD, begin, end, \, $, } |

**Parsing table**

|    | $ | \   | begin | end | WORD | {   | } |
|----|---|-----|-------|-----|------|-----|---|
| S' | 0 | 0   | 0     | 0   | 0    | 0   |   |
| S  | 1 | 1,2 | 1,2   | 1,2 | 1,2  | 1,2 | 1 |
| B  |   | 3   |       |     |      |     |   |
| E  |   | 4   |       |     |      |     |   |
| X  |   | 5   | 5     | 5   | 5    | 5   | 5 |

Hvis nullable, skal der også sættes tegn ved follow sæt.

Parsing table tager kun udgangspunkt i de første 5 expressions.

Vi kan se at der er flere produktioner til samme udtryk, og grammatikken er derfor forkert.



### 3.8
**Make up a tiny grammar containing left recursion, and use it to demonstrate
that left recursion is not a problem for LR parsing. Then show a small example
comparing growth of the LR parse stack with left recursion versus right recursion.**  

Left recursion:  
```
0 S'-> S$
1 S -> Sx
2 S -> x

LR(0) -parser - fordi vi har 0 lookahead.
```

Første statement:
```
S'-> .S$
S -> .Sx
S -> .x
```
3
Hvis vi læser S (fra 1)

```
S'-> S.$
S -> S.x
```
2
Hvis vi læser X (fra 1)

```
S -> x.
```
4
Hvis vi læser X (fra 3)
```
S->Sx.
```
***
Right:  
```
0 S'-> S$
1 S -> xS
2 S -> x
LR(1): 1 lookahead
```

(1) Første statement:
```
S'-> .S$    ?
S -> .xS    $
S -> .x     $
```
2 hvis vi læser S (fra 1)
```
S' -> S.$   ?
```
3 hvis vi læser x (fra 1)
```
S -> x.S    $
S -> x      $
S -> .xS    $
S -> .x     $
```
hvis vi læser x igen (fra 3)
```
Samme som 3, vi kører i cirkel, rekursion
```

4 Hvis vi læser S (fra 3)
```
S -> xS.    $
```


### 3.10
**Diagram the LR(1) states for the grammar of Exercise 3.7 (without left-factoring),
and construct the LR(1) parsing table. Indicate clearly any conflicts.**  
Med udgangspunkt i forrige konstruerede LR parse stack (fra 3.8) med right recursion, kan vi konstruere følgende parsing table:  

|   | x    | $ | S  |
|---|------|---|----|
| 1 | S3   |   | g2 |
| 2 |      | a |    |
| 3 | S3   |r2 | g4 |
| 4 |      |r1 |    | |

```
Input : xxx$

Stack  Read  | State

1       xxx$ | S3  
1x3     xx$  | S3  
1x3x3   x$   | S3  
1x3x3x3 $    | r2  
1x3x3S4 $    | r1  
1x3S4   $    | r1  
1S2     $    | a  
```
