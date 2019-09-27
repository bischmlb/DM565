### 1
**Use the command-line tool sort to sort on the first names. Which effect does sort -k 2 have? Now sort on the email addresses.**

sort -k 2 will sort them using the second word on that specific line. -k specifies a key which defines the location of what to sort.
***
### 2
**Use tr twice to delete ":" and change "@" to "$".**

```
λ cat participants.txt | tr -d ':' | tr '@' '$'
Anders Nicolai Knudsen Email anknu18$student.sdu.dk
Marie Gabriele Christ Email machr14$student.sdu.dk
Abyayananda Maiti Email abmai13$student.sdu.dk
Sushmita Gupta Email sugup13$student.sdu.dk
Martin Rud Ehmsen Email maehm10$student.sdu.dk
Bárður Árantsson Email baara07$student.sdu.dk
Jens Svalgaard Kohrt Email jeko404$student.sdu.dk
Morten Nyhave Nielsen Email monie02$student.sdu.dk
Lars Jacobsen Email lajac01$student.sdu.dk
```
***
### 3
**Use cut several times to remove anything other than the user name, i.e., first remove @student.sdu.dk, and then continue.**
```
λ cut -d "@" -f 1 participants.txt | cut -d ":" -f 2 | tr -d "^ " > usernames.txt
anknu18
machr14
abmai13
sugup13
maehm10
baara07
jeko404
monie02
lajac01

 ```

### 4
**Make a file with as many copies of the line @student.sdu.dk as there are lines in the original file. You can of course find out how many lines are needed using wc. ツ One way to create that file is to use seq n, where n is the number of lines you need, followed by an appropriate sed substitution using a regular expression. Now paste this file together with the file of user names from above to create full email addresses again.**  

make the file.

```
λ seq 9 | tr -d [0-9] | sed -s 'i @student.sdu.dk' | sed -n 'p;n' > emails.txt | cat emails.txt
@student.sdu.dk
@student.sdu.dk
@student.sdu.dk
@student.sdu.dk
@student.sdu.dk
@student.sdu.dk
@student.sdu.dk
@student.sdu.dk
@student.sdu.dk

```
paste for full emails.
used delimiter d "" because default is " "

```
λ paste -d "" usernames.txt emails.txt > fullEmails.txt | cat fullEmails.txt
anknu18@student.sdu.dk
machr14@student.sdu.dk
abmai13@student.sdu.dk
sugup13@student.sdu.dk
maehm10@student.sdu.dk
baara07@student.sdu.dk
jeko404@student.sdu.dk
monie02@student.sdu.dk
lajac01@student.sdu.dk
```

***
### 5
**Use awk to put a line number and a colon in front of the full emails from above. Remove the space following the colon in the original file, and then join these two results on the email address field.**

```
λ awk ' { print NR ":" $0 } ' fullEmails.txt > awkfullEmails.txt | cat awkfullEmails.txt
1:anknu18@student.sdu.dk
2:machr14@student.sdu.dk
3:abmai13@student.sdu.dk
4:sugup13@student.sdu.dk
5:maehm10@student.sdu.dk
6:baara07@student.sdu.dk
7:jeko404@student.sdu.dk
8:monie02@student.sdu.dk
9:lajac01@student.sdu.dk
```
