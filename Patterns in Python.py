'''
#16.Star pattern
n = int(input('Enter no. of rows:'))
for i in reversed(range(1,n+1)):
    print('*'*i)

Output:
*****
****
***
**
*
________________________________________________________
# same star pattern while:
n = 5
while n >= 1:
    print('*'*n)
    n-=1
output:-
*****
****
***
**
*
--------------------------------------------------------------------
#17. number pattern
for i in range(1,6):
    for j in range(i,6):
        print(j, end="")
    print()
for i in reversed(range(1, 5)):
    for j in range(i,6):
        print(j,end="")
    print()
Output:
12345
2345
345
45
5
45
345
2345
12345
___________________________________________________________________
#18. star pattern
n = int(input('Enter no. of rows:'))
for i in range(1,n+1):
    print('*'*i)
output:-
*
**
***
****
*****

_________________________________________________
19.Number 0 1 pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i+j)%2 ==0:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
o/p
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
----------------------------------------------
20.Alphabeticl pattern:
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end='')
    print()
Output:-
A
AB
ABC
ABCD
ABCDE
_______________________________________________________
# 21. number pattern
for i in range(1,6):
    for j in reversed(range(1,i+1)):
        print(j,end='')
    print()
output:-
1
21
321
4321
54321
_________________________________________________________
#22. using if...elif
for i in range(1,6):
   for j in range(1,i+1):
      if i == j == 1:
         print(j,end="")
      elif i == 2:
         print(j+1,end="")
      elif i == 3:
         print(j + 3, end="")
      elif i == 4:
         print(j+6,end="")
      else:
         print(j+10,end="")
   print()
output:-
1
23
456
78910
1112131415
_________________________________________________________
23.Number 0 1 pattern upper triangular
n = 5
for i in range(1, n + 1):
    for j in range(i):
        if (i+j)%2 ==0:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
o/p
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

-------------------------------------------
#24. Number Pattern:
for i in range(1,8):
    for k in reversed(range(i,8)):
        print(" ",end="")
    for k in range(1,i):
        print(k,end="")
    for k in reversed(range(1,i+1)):
        print(k,end="")
    print()
Output:-
          1
        1 2 1
      1 2 3 2 1
    1 2 3 4 3 2 1
  1 2 3 4 5 4 3 2 1
 1 2 3 4 5 6 5 4 3 2 1
1 2 3 4 5 6 7 6 5 4 3 2 1
__________________________________________________________________
#25.Number pattern
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
output:
1
22
333
4444
55555
_________________________________________________________
#26.Number pattern
for i in range(1,8):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in reversed(range(1, 8)):
    for j in range(1,i):
        print(j,end="")
    print()
Output:
1
12
123
1234
12345
123456
1234567
123456
12345
1234
123
12
1
___________________________________________________________
27. Number Pattern
for i in range(1,8):
    for j in range(i-1,7):
        print(chr(65+(j-i+1)),end="")
    for j in range(1, 6,3):
        print(" "*(i-1), end="")
    for k in reversed(range(i-1, 7)):
        print(chr(65+(k - i + 1)), end="")
    print()
Output:-
ABCDEFGGFEDCBA
ABCDEF  FEDCBA
ABCDE    EDCBA
ABCD      DCBA
ABC        CBA
AB          BA
A            A
_________________________________________________________________
#number pattern1
#n = int(input('Enter no. of rows:'))
for i in range(1,6):
    for j in range(1,6):
        print(i,j,end='\t')
    print()
o/p
1 1	1 2	1 3	1 4	1 5
2 1	2 2	2 3	2 4	2 5
3 1	3 2	3 3	3 4	3 5
4 1	4 2	4 3	4 4	4 5
5 1	5 2	5 3	5 4	5 5

#number pattern matrix
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= i:#below diagonal elements are equal to no. of rows
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()

o/p
1 2 3 4 5
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5


for i in range(1,6):
   for j in range(i-2,i+1):
      print(2*i+j,end="")
   print()
output:-
123
456
789
101112
131415


for i in range(1,6):
    for j in range(1,i+1):
        print(j+i-1,end="")
    print()

Output:-
1
23
345
4567
56789

'''


