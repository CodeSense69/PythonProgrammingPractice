'''game = [1,2,2,4,5]
def myfunction101():
    for mygame in game:
        print(mygame)
    game[2]=78
    for mygame in game:
        print(mygame)
print(myfunction101())
game = [[0, 0 , 0],
        [0 ,0 , 0],     
        [0 ,0 , 0]]

def myfunction():
    print("   0  1  2")
    for count,row in enumerate(game):
        print(count,row)
myfunction()'''
'''game = [[0, 0 , 0],
        [0 ,0 , 0],     
        [0 ,0 , 0]]
def myfunction():
    print("   0 ,1 ,2")
    for count,row in enumerate(game):
        print(count,row)
myfunction()

fruits = ["mango" , "orange" , "banana" , "watermelon"]
veggies = ["lettuce" , "tomato" , "brinjal" , "bittergourd"]
veggies.append(fruits)
print(veggies)'''

'''game = [[0, 0 , 0],
        [0 ,0 , 0],     
        [0 ,0 , 0]]
game[2][1] = 22
print(game)'''


#MISCELLANEOUS FUNCTIONS:
'''fruits = ["mango" , "orange" , "banana" , "watermelon"]
veggies = ["lettuce" , "tomato" , "brinjal" , "bittergourd"]
veggies.append(fruits)
print(veggies)'''

'''def addition(x, y):
    print(x+int(y))
addition(7.8 , "7")'''

'''def myfunction(x,y):
    if type(x) == str or type(y)==str:
        print(str(x)+str(y))
    else: 
        print(float(x)+float(y))
myfunction("hello " , 8)'''

#LOCAL AND GLOBAL VARIABLES CONCEPT: 
'''list1 = ["hello" , 5 , 34 , " why"]
def myfunction():
    addition = list1[0]+list1[3]
    print(addition)
myfunction()'''


#VVI GLOBAL AND LOCAL FUNCTION COMPARISONS:
'''message = "this is the message outside the function"
def myfunction():
    global message
    message = "this is the message inside the function"
    print(message)
myfunction()
print(message)'''

# SOME SHIT:
'''paagalinsaan = [1,2,3,4,5]
def myfunction():
    paagalinsaan[1]=paagalinsaan[3]+paagalinsaan[4]
    print(paagalinsaan)
myfunction()'''

'''variable = 0
if not variable:
    print("okay")'''
#whereas
#IDEA TO REMOVE AN ELEMENT FROM A TUPLE AND PRINT INDIVIDUAL ITEMS:
'''list1 = ("hello" , "wassup" , "buddy" ,"not so", "nice" , "meeting" , "you")
for items_1 in list1:
    if not items_1 in ("not so"):
        print("List_Item" , items_1)'''
'''WAY TO MODIFY TUPLES AND PRINT THE TUPLE ITSELF:
list2 = ("hey" , "buddy" , "whats" , "up" , "panni" , "thendi")
def myfunction():
    mynewlist = list2[:2]+list2[4:]
    print(mynewlist)
myfunction()'''
'''FOR FINDING THE EVEN NUMBERS OUT OF A LIST OF NUMBERS:
list1 = [10, 21, 4, 45, 66, 93] 
for number in list1:
    if number%2 == 0:
        print(number)'''

'''PRINTING A NUMBERED LIST:
mylist = ["apple" , "banana" , "cat" , "dog"]
for integer in range(len(mylist)):
    print(integer,mylist[integer])'''

'''CHECKING FOR ID'S OF VARIABLES/OBJECTS:
message = "I want to play a game" 
print(id(message))
def myfunction():
    message = "A game ryt"
    print(id(message))
print(message)
myfunction()
print(message)
print(id(message))'''

'''TO CHECK FOR MODIFICATION OF A GLOBAL VAR BY A FUNCTION:
message = [0,1,2,3,4,5]
def myfunction():
    message[2]  = 898
    print(message)
print(message)
print(id(message))
myfunction()
print(message)
print(id(message))'''

'''ASSIGNING A GLOBAL VAR TO A LOCAL VAR AND REASSIGNING IT:
hello = ["hello" , "sweetie"]
def myfunctionsweetie(hellolocal):
    hellolocal[1] = "bro wtf"
    print(hellolocal)
hello = myfunctionsweetie(hello)'''

'''FILE WRITING/READING:
with open('flexfile.txt' , 'r') as MyFile:
    output1 = MyFile.readlines()
    for qualities in output1:
        new_output = qualities.split(' ')[1]
        print(new_output)'''

'''ADDITIONAL CODE:
message = ['hello 1','how 2', 'are 3', 'you 4','dude 5']
for items in message:
    variable = items.split(' ')[1]
    print(variable)'''
#LIST COMPREHENSION:
'''nums = [1,2,3,4,5,6,7,8,9,10]

mylist=[]
for n in nums:
    mylist.append(n*n)
print(mylist)'''
#I want n for each n in nums,in mylist
'''nums = [1,2,3,4,5,6,7,8,9,10]
#(what it should return , what should be the input , from which object is the input recieved)
mylist = [n*n for n in nums]
print(mylist)'''

#maps and lambdas-corey schaffer
#more on list comprehension


#CODE TO PICK OUT THE INTEGERS FROM A STRING:
'''test_string = "He had 2 apples and 7 banana's in his basket of 11 fruits"
print("original string is: " + test_string)
#res = result 
#FOR any i IN the (split)test_string IF i is an integer (i.isdigit()) , print the (int(i)):
res = [int(i) for i in test_string.split() if i.isdigit()==True]
for items in res:
    print(items)'''

#Practicing the smort code(1):
'''test_string = "hello everyone it is 2 am but were chilling with 7 icecreams and 4 popcorn buckets"
print("The Original String Is: " + test_string)
result = [int(i) for i in test_string.split() if i.isdigit()==True]
for items in result:
    print(items) '''

'''HOORAYYYYYY-TAKES INTEGERS FROM FILE:
with open("file.txt" , 'r') as MyFile:
    output = MyFile.readlines()
    for list_items in output:
        new_output = [int(i) for i in list_items.split() if i.isdigit() ]
        print(new_output)'''

        
'''FORMAT FUNCTION:
age = 16
place = "Muscat"
attribute = "happy"
txt = "hello my name is harshal and I am {} and I live in {} and I am {}"
print(txt.format(age,place,attribute))'''

'''MESSED UP INDEXES WHICH HAVE TO BE CORRECTED:
age = 16
wearables = "A Red Jacket"
place = "Muscat"
txt = "hello my name is harshal and I wear {1} and I live in {2} and I am {0}"
print(txt.format(age,wearables,place))'''


#PASS KEYWORD SOME SHIT:
'''myvariable = 'hello world wassup bois and girls'
def myfunctionforsplitting():
    for letters in myvariable:
        if letters == ' ':
           pass
           print('this is the pass block')
        print('The Current Letter Is: ' , letters)
myfunctionforsplitting()   '''    
#ESCAPE CHARACTERS:
#variable = "We are the \'Champions\' My Friend"
#print(variable)

#BOOL FUNCTION:
'''print(bool(""))
print(bool(["abc" , 1 , 2 , 3]))'''


#DETERMINING WHETHER A NUMBER IS A PERFECT SQUARE OR NOT:
'''import math

# Taking the input from user
number = int(input("Enter the Number"))

root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")'''

'''import math
def myfunction(n):
    root = math.sqrt(n)
    if int(root+0.5)**2 == n:
        print(str(n)+' is a perfect square')
    else:
        print(str(n) + ' is not a perfect square')
myfunction(81010902)'''

'''import itertools
import math


def is_perfect_square(number: int):
    closest_int = int(math.sqrt(number))
    for i in itertools.count(closest_int):
        if (squared := i * i) == number:
            return True
        if squared > number:
            return False


print(is_perfect_square(25))
print(is_perfect_square(161**2))
print(is_perfect_square(161**2 - 1))
#You can use range instead of itertools.count since it won't take more than 1-2 iterations
#To find if numbers is a perfect square you can first take it's root, then round it to an integer, then look if consecutive integers squared == number. If any of these squared integers bigger than your number then it isn't a perfect square
'''
#FINAL CODE FOR PERFECT SQUARES:
'''import math
def is_square(n): 
    if n<0:
        print('False')
    elif math.sqrt(n).is_integer():
        print('True')
    else:
        print('False')
is_square()'''

#FOR CHECKING WHETHER WALK IS LESS THAN 10 MINS AND RETURNS YOU TO THE SAME POSITION:
'''def is_valid_walk(walk):
    x=0
    y=0
    for direction in walk:
        if direction == 'n':
            y += 1
        if direction == 'w':
            x -= 1
        if direction == 'e':
            x += 1
        if direction == 's':
            y -= 1
    if (len(walk)==10 and x==0 and y==0):
        print("True")
    else:
        print('False')
is_valid_walk(['s', 'n', 's', 's', 'n', 's', 'n', 'n'])'''

'''def bool_to_word(boolean):
    if boolean == True:
        print('Yes')
    else:
        print('No')
bool_to_word(True)'''
'''TO FIND THE DESCENDING ORDER OF DIGITS:
def descending_order(num):
    variable = list(str(num))
    variable.sort(reverse=True)
    s = "".join(variable)
    print(int(s))
descending_order(19293182)'''
'''
def descending_order(num):
    variable=list(str(num))
    variable.sort(reverse=True)
    mynewvariable = "".join(variable)
    print(mynewvariable)
descending_order(182918291849)'''

#more practice on parameters
'''game = [[0, 0 , 0],
        [0 ,0 , 0],     
        [0 ,0 , 0]]
def game_board(player,row,column):
    print("   0  1  2")
    for count,row in enumerate(game):
        print(count,row)
game_board(1,2,3)'''

'''game = [[1, 2 , 3],
        [0 ,0 , 0],     
        [0 ,0 , 0]]
def win(current_player):
    for row in game:
        print(row)
        all_match = True
        for item in row:
            if item != row[0]:
                all_match = False
        if all_match:
            print("Winner")
        else:
            print("nah thats not it!")
win(game)'''


'''import random
for i in range(3):
    print(random.randrange(0, 101, 5))
random.randrange()
random.randint()
random.choice()
shuffle ( from random import shuffle)'''

'''PRINTS A RANDOM LETTER FROM A STRING:
import random
mystring = 'hello wassup bhaijaan'
newbie = list(mystring)
print(random.choice(newbie))'''

'''import random
mystring = 'hello wassup bhaijaan'
print(mystring[random.randrange(0,len(mystring))])'''

'''mystring = 'hello wassup bhaijaan'
print(id(mystring[0:0]))
print(id(mystring[5]))'''

'''SLICES THE STRING FROM THE START TO ANY RANDOM POINT:
import random
mystring = 'hello wassup bhaijaan'
print(mystring[0:random.randrange(0,len(mystring))])'''

#PROGRAM TO PRINT THE BOOMERANGS:
'''list2 = [1,2,1,2,3,4,3,5,2,5,3,5]
def count_boomerangs(lst):
    for n in range(len(lst)):
        if n <= len(lst)-3 and lst[n] == lst[n+2]:
            variable = [lst[n],lst[n+1],lst[n+2]]
            print(variable)
                
    
count_boomerangs(list2)'''

'''Method to print counter of number of boomerangs:
def count_boomerangs(lst):
    c=0
    for i in range(len(lst)):
        if i+3<= len(lst):
            if lst[i]==lst[i+2] and lst[i] != lst[i+1]:
                c+=1
    print(c)
count_boomerangs(list2)'''

'''SUM OF SQUARES:
list1 = [3,3,3,3,3]
def myfunction(lst):
    variable = [num*num for num in lst]
    print(sum(variable))
myfunction(list1)'''

'''SUM OF NUMBERS IN A LIST:
list1 = [11, 5, 17, 18, 23]  
total = 0
for ele in range(0, len(list1)): 
    total = total + list1[ele] 
print(total)'''

#TO FILTER THE STRINGS OUT AND LEAVE THE INTEGERS:
'''list1 = [1, 2, 1, 0, 15] 
newlst = []
for items in list1:
    if type(items)==int:
        newlst.append(items)
print(newlst)'''

'''REVERSE ORDER OF WORDS:
aahhello = 'what do you mean'
def reverseorderwords(stringnew):
    x=stringnew.split(' ')
    print(' '.join(x[::-1]))
reverseorderwords(aahhello)'''

'''AVERAGE OF NUMBERS:
mymarks = [1, 5, 87, 45, 8, 8]
def get_average(marks):
    print(int(sum(mymarks)/2))
get_average(mymarks)'''

'''THE GRAVITY CUBE QUESTION:
mylist = [3,2,1,2]
def flipgrav(d,a):
    if d == 'R':
        a.sort(reverse=False)
    elif d == 'L':
        a.sort(reverse=True)
    print(a)
flipgrav('R',[3, 2, 1, 2])'''

'''def set_alarm(employed, vacation):
    if employed and not vacation:
        print(True)
    else:
        print(False)
set_alarm(False,False)'''

'''PYTHON PROGRAM TO CHECK WHETHER THE NUMBER OF Xs AND Os ARE SAME IN A STRING:
def xo(s):
    variable = s.lower()
    if variable.count('x')==variable.count('o'):
        print(True)
    else:
        print(False)'''

#Python program to return the sum of elements of two arrays:
'''def array_plus_array(arr1,arr2):
    variable = arr1+arr2
    print(sum(variable))
array_plus_array([1,2,3,4],[5,6,7,8])'''

'''TO PRINT THE NUMBER OF YEARS IN WHICH THE POPULATION WOULD REACH THE GIVEN VALUE:
def nb_year(p0, percent, aug, p):
    count = 0
    current_value = p0
    while current_value<=p:
        current_value = current_value+(current_value*(percent/100))+aug
        count+=1
    print(count)
nb_year(1500000, 0.25, 1000, 2000000)'''

'''THE PYTHON PROGRAM TO REVERSE EACH WORD BUT MAINTAIN THE ORDER:
ALSO INCLUDES HOW TO MODIFY EACH ITEM OF A LIST WITHOUT FOR LOOP
def reverse_words(text):
    variable=text.split()
    for i in range(len(variable)):
        variable[i]=variable[i][::-1]
    print(' '.join(variable))
       
reverse_words('elbuod decaps sdrow')'''

'''TO PRINT -1 if index is out of range or to 
give the nth power of the number at the nth "valid" index:
def index(array, n):
    try:
        print(array[n]**n)
    except Exception as e:
        print(-1)
index([1, 2, 3, 4],4)'''
'''def greet(name):
    print(f'Hello, {name} how are you doing today?')
greet('Harshal')
'''
'''WARN THE SHEEP ABOUT THE WOLVES PROGRAM:'''
'''def warn_the_sheep(queue):
    for i in range(len(queue)):
        if queue[i]=='wolf' and i != len(queue)-1:
            print(f"Oi! Sheep number {len(queue)-i-1}! You are about to be eaten by a wolf!")
    if queue[len(queue)-1] == 'wolf':
        print('Pls go away and stop eating my sheep')

warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep'])
'''
'''ATTEMPT 1 AT MATCHING STRINGS:
def myfunction(a,b):
    variable1 = list(a)
    variable2 = list(b)
    for i in range(len(variable1)):
        if variable1[i]=='*':
           variable1[i]=variable2[i] 
    if "".join(variable1)=="".join(variable2):
        print(True)
    elif a=='*':
        print(True)
    elif a==b:
        print(True)
    else:
        print(False)
myfunction('*','codewars')'''

#ATTEMPT 2 AT MATCHING STRINGS:
'''def solve(a,b):
    for i in range(len(a)):
        if a[i]=='*' and a.replace('*','') != b and a!='*' and len(a)<=len(b):
            return(True)
    if len(a)>len(b) and a.replace('*','')!=b:
        return(False)
    elif a[i]!='*' and a!=b and a.replace('*','')!=b:
        return(False)
    elif a.replace('*','') == b:
        return(True)
    elif a =='*':
        return(True)
    elif a==b:
        return(True)
    elif len(a)>len(b) and a.replace('*','')==b:
        return(True)
solve("*s","codewars")''' 

'''SIMPLE STRING MATCHING FINAL SOLUTION - BIG TIME:
def solve(a,b):
    for i in range(len(a)):
        newvar = a.replace('*',b[i:i+len(b)-len(a)+1])
        if a[i]=='*' and len(b)>=len(a) and newvar==b:
            return(True)
        if a[i]=='*' and len(a)>len(b) and a.replace('*','')==b:
            return(True)
    if a[i]=='*' and len(a)>len(b) and a.replace('*','')!=b:
        return(False)
    if a==b:
        return(True)
    if a[i]!='*' and a!=b:
        return(False)
    else:
        return(False)'''

'''ARE YOU PLAYING THE BANJO:
def areYouPlayingBanjo(name):
    if list(name)[0]=='R':
        print(f"{name} plays banjo")
    elif list(name)[1]=='r':
        print(f"{name} plays banjo")
    else:
        print(f"{name} does not play banjo")
    print(list(name))
areYouPlayingBanjo("Rikke")'''

'''SUM OF ALL NUMBERS FROM 1 TO THE GIVEN NUMBER:
def summation(num):
    newlst = []
    for i in range(num):
        newlst.append(i)
    newlst.append(num)
    print(sum(newlst))
summation(2)'''

'''def hello(name='World'):
    if name!='':
        name = name.title()
        print(f"Hello, {name}!")
    elif name=='':
        print('Hello, World!')
hello("")'''

'''AUTOMORPHIC NUMBER CHECKER:
def automorphic(n):
    square_number = n*n
    if len(str(n))>1 and str(square_number)[-len(str(n)):] == str(n):
        print("Automorphic")
    elif len(str(n))==1 and str(square_number)[-1] == str(n):
        print("Automorphic")
    else:
        print("Not!!")
automorphic(12)'''

'''CHECKS WHETHER A ENDS WITH B:
def solution(a,b):
    if a[-len(b):]==b:
        print(True)
    elif b=='':
        print(True)
    else:
        print(False)
solution('samurai','')'''

'''PRINT THE AREA IF SQUARE OR PERIMETER IF RECTANGLE:
def area_or_perimeter(l,w):
    perimeter = 2*(l+w)
    area = l*w
    if l==w:
        print(area)
    if l!=w:
        print(perimeter)
area_or_perimeter(8,8)'''

'''GODDAMN THESE ARE FUNCTIONS ?
title()
capitalize()
endswith()
seek()
tell()
'''
#more about the print function and streams under the sys module https://www.stackabuse.com/writing-to-a-file-with-pythons-print-function/
#more about the python buffer's https://www.djangospin.com/python-file-buffering/

#REMOVES BOTH INSTANCES OF THE DOUBLE LETTER ATTEMPT 1:
'''def double(s):
    for i in range(len(s)):
        newvar = s.replace(s[i:i+2],'')
        if i < len(s)-1:
            if s[i]==s[i+1] and s.replace(s[i:i+2],'')[0]!=s.replace(s[i:i+2],'')[1]:
                print(newvar)
            if newvar[0]==newvar[1]:
                print('')
double('abbbzz')'''

#REMOVES ONE INSTANCE OF THE DOUBLE LETTERS:
'''def double(s):
    mylist = list(dict.fromkeys(list(s)))
    print(''.join(mylist))
double('abbbzz')'''
'''def double(s):
    i=0
    while i <len(s)-1:
        if s[i]==s[i+1]:
            print(s.replace(s[i:i+2],''))
        i+=1
double('abbbzz')'''

#PROGRAM TO PRINT EVERY THIRD ELEMENT IN A STRING:
'''def evryThird(s):
    print(s[::3]+s[1::3])

evryThird("abcdefghijk")'''

'''def myfunction(redacted,string):
    for i in range(len(string)):
        if string[i]==redacted :
            print(string.replace(redacted,''))
redacted = input("Enter the chosen name here")
string = input("Enter Sentence here")
myfunction(redacted,string)'''

'''DETECT THE FIRST DOUBLE:
def first_double(s):
    for i in range(len(s)):
        if i<len(s)-1 and s[i]==s[i+1]:
            return(s[i]+s[i+1])
            break
first_double('abcc')'''
