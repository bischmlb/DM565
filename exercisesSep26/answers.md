### 1
**Use the command-line possibilities discussed under the topic of data discovery to inspect these files, i.e., what does file and wc say about them? Inspect them using od with appropriate options. How do they differ? Discuss pros and cons of the formats. Try recode to change from one character encoding to another.**

file

```
λ file *
File_Ex_Latin1.txt:     ISO-8859 text
File_Ex_MS-DOS_Eol.txt: ASCII text, with CRLF line terminators
File_Ex_UTF8.txt:       UTF-8 Unicode text
File_Ex_Unix_Eol.txt:   ASCII text
```

wc

```
λ wc *
 1  1 11 File_Ex_Latin1.txt
 2  5 24 File_Ex_MS-DOS_Eol.txt
 1  1 14 File_Ex_UTF8.txt
 2  5 22 File_Ex_Unix_Eol.txt
 6 12 71 total
```

using od -tcuC we can see that these two files have different ways to represent characters. ISO8859-1 (latin1) is a single-byte encoding that can only represent the first 256 unicode characters, while UTF-8 can represent any unicode character. We can see that a lot of the characters are the same, while some of them differ.

```
λ od -tcuC File_Ex_UTF8.txt && od -tcuC File_Ex_Latin1.txt
0000000   B   l 303 245   b 303 246   r   g   r 303 270   d  \n
         66 108 195 165  98 195 166 114 103 114 195 184 100  10
0000016
0000000   B   l 345   b 346   r   g   r 370   d  \n
         66 108 229  98 230 114 103 114 248 100  10
0000013
```

When we octal dump the other two files, we can confirm what was initially discovered with the file command, that MS-DOS compared to Unix-Eol uses CRLF line terminators in addition to them both being an ASCII text file. However, character encodings are the same. This is because DOS uses carriage return and line feed ("\r\n") as a line ending, where Unix uses just line feed ("\n").

```
λ od -tcuC File_Ex_Unix_Eol.txt && od -tcuC File_Ex_MS-DOS_Eol.txt
0000000   I   t       a   l   l       e   n   d   s   ;  \n   b   u   t
         73 116  32  97 108 108  32 101 110 100 115  59  10  98 117 116
0000020       h   o   w   ?  \n
         32 104 111 119  63  10
0000026
0000000   I   t       a   l   l       e   n   d   s   ;  \r  \n   b   u
         73 116  32  97 108 108  32 101 110 100 115  59  13  10  98 117
0000020   t       h   o   w   ?  \r  \n
        116  32 104 111 119  63  13  10
0000030
```

### 2
**Using the Python csv package, read a file in the default csv format and output it in tsv format.**

see ```pythonCsv.py```

### 3
**Define separate grep (or grep -E) regular expressions matching lines with
Scandinavian email address.
CPR numbers.
phone numbers written as 2 groups of 4 digits or 4 groups of 2 digits; groups separated by one space.
dates in the Danish format 1/1 1970.
In all of these problems, we are interested in the format. Thus, you do not have to worry about exactly which characters are legal in email addresses, if months have 30 or 31 days, or whether CPR numbers are legal according to checksums rules etc.**

1. Scandinavian email address:  
Format ex: *something@something.dk/swe/nor*  
grep:
```
λ grep -E "[a-å]+@[a-å]+\.dk|se|no" testGrep.txt
mathiasbischoff@gmail.dk
mathiasbischoff@gmail.no
mathiasbischoff@gmail.se
svenskeren@hotmail.se
nordmanden@live.no
danskeren@gmail.dk
```
2. CPR numbers:  
Format ex: *123456-1234*  
```
λ grep -E "[0-9]{6}+\-[0-9]{4}" testGrep.txt
210396-1301
230994-2304
091291-0301
```  
3. phone numbers written as 2 groups of 4 digits or 4 groups of 2 digits; groups separated by one space.  
Format ex: *12 34 56 78* or *1234 5678*  
```
λ grep -E "[0-9]{2} [0-9]{2} [0-9]{2} [0-9]{2}|[0-9]{4} [0-9]{4}" testGrep.txt
26 30 35 34
2630 3534
3177 2143
31 77 21 43
```
4. dates in the Danish format 1/1 1970.  
Format ex: *1/2 1999*
```
λ grep -E "[0-9]{1,2}/[0-9]{1,2} [0-9]{4}" testGrep.txt
26/3 1996
22/3 1992
12/9 2001
1/3 1990
```
### 4
**Using /usr/share/dict/words, define separate grep (or grep -E) regular expressions matching lines (words, since there is only one word per line in that file) with
consecutive repetition of at least three characters.
a consecutive repetition of the same sequence of four characters.
palindromes of lengths 4, 5, and 6.
words without vowels (a, e, i, o, u, y); use an option.**

1. Conescutive repetion of at least three characters:  
```grep -E "([A-Za-z])\1{1}" usr/share/dict/words```  

2. a consecutive repetition of the same sequence of four characters:  
```grep -E "([A-Za-z][A-Za-z][A-Za-z][A-Za-z])\1{1,}"```

3. palindromes of lengths 4, 5, and 6.  
```grep -E "(^.)(.).?\2\1$" testGrep.txt && grep -E "(^.)(.)(.)\3\2\1$" testGrep.txt```
or
```grep -E"(^.)(.)(.?).?\3\2\1$" testGrep.txt``` however this last oportunity will also print for length 7.

4. words without vowels (a, e, i, o, u, y); use an option.
```grep -E "^[^AaEeIiOoUuYyÆæØøÅå]*$" words```

### 5
Define separate grep (or grep -E) regular expressions matching lines with
an opening and closing html headline tag, e.g., ```<h2 >My Headline </h2>``` use an option to make it case insensitive, then use an option to print the line number for every match. You may require that headlines are on a line by themselves (and of course not nested).
numbers in the range 1000 through 9999.
numbers in the range 100 through 9999.

headlines:
```
λ grep -Ein "<[h][1-9]>" testGrep.txt
34:<h2> lille headline </h2>
35:<H3> STOR HEADLINE </H3>
```
1000-9999:
```
λ grep -E "^[0-9][0-9][0-9][0-9]$" testGrep.txt
```
100-9999 (just add ? for optional):
```
λ grep -E "^[0-9][0-9][0-9][0-9]?$" testGrep.txt
```
