#FINAL METHOD FOR REMOVING DOUBLES USING 2 FUNCTIONS:
'''def first_double(s):
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i+1]:
            return( s[i] + s[i+1] )'''


'''def double(s):
    while d:= first_double(s):
        s=s.replace(d,'')
    print(s)
double('abba')  PYTHON 3.8''' #walrus operator used from python 3.8

#(OR)

'''def double(s):
    while True:
        d = first_double(s)
        if not d:
            break
        s=s.replace(d,'')
    print(s)
double('abbca') PYTHON 3.6'''


'''METHOD THAT REQUIRES THE MOST LOGIC - REMOVING DOUBLES FROM A STRING:
def double(s):
    stack = []
    for c in s:
        if len(stack)==0:
            stack.append(c)
            print(stack)
            continue
        if stack[-1]!=c:
            stack.append(c)
            print(stack)
            continue        
        if stack[-1]==c:
            stack.pop()
            print(stack)
    print("".join(stack))
double('abba')'''

'''DECODE A PIG LATIN WORD:
def pig_latin(word):
    newlst = list(word)
    if word[-2:]=='ay':
        new_word = f'{word[-3]}{word[:-3]}'
        print(new_word)

word = input('Enter a name here')
pig_latin(word)'''

'''IF YOU DONT WANT TO REPLACE REDACT IF REDACT IS PART OF A TEXT:
def redacted_text(redact,text):
    newtext = text.split()
    for i in range(len(newtext)):
        if newtext[i]==redact:
            newtext[i]='REDACTED'
            print(' '.join(newtext))'''

'''IF YOU WANT TO REPLACE REDACT IF ITS A PART OF A TEXT ALSO:
def redacted_text(redact,text):
    print(text.replace(redact,'REDACTED'))
redacted_text('Harshal' , 'Harshaloof Is A Genius')'''

#PICKLE MODULE
#PYTHON SPAM PROGRAM
'''import pyautogui,time
time.sleep(5)
f='Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello '
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('Enter')'''

#RETURN FIRST NON CONSECUTIVE INTEGER AND RETURN'S NULL FOR A FULL CONSECUTIVE LIST AND AN EMPTY LIST:
'''def first_non_consecutive(arr):
    for i in range(len(arr)):
        if i<len(arr)-1 and arr[i+1]!=arr[i]+1:
            print(arr[i+1])
first_non_consecutive([1,2,3,4,6,7,8])'''

#STONES ON THE TABLE:
'''def solution(stones):
    count=0
    for i in range(len(stones)):
        if i<len(stones)-1 and stones[i]==stones[i+1]:
            count+=1
    print(count)
solution("RGBRGBRGGB")'''

#STRING MATCHER
'''def split(word):
    return[char for char in word]
def is_matching(st,st1,st2):
    newvariable = list(st1+st2)
    while newvariable.count(' '):
        newvariable.remove(' ')
    newvariable.sort(key = str.lower)
    new1 = ''.join(newvariable).lower()
    newlst = list(st)
    while newlst.count(' '):
        newlst.remove(' ')
    newlst.sort(key = str.lower)
    new2 = ''.join(newlst).lower()
    
    if new1 == new2:
        print(True)

    else:
        print(False)
    print(new1)
    print(new2)
is_matching('It is ALL for the BEST' , 'IT IS all'  , 'FOR THE best')'''


#sorted()
# for case insensitive sorting use key  = str.lower in sort() function since sort() is case sensitive by default
#remove function remove()

'''variable = st1
newvariable = variable.split()
print(''.join(newvariable))'''

#THE NEXT HAPPY YEAR

'''FIRST ATTEMPT:
def split(string):
    return[char for char in string]
def next_happy_year(year):
    stringyear = str(year)
    newvar = split(stringyear)
    setnew = set(stringyear)
    year+=1
    while len(setnew)!=len(newvar):
        year+=1
        setnew = set(str(year))
        newvar=split(str(year))
    return(year)



next_happy_year(1987)'''

'''CORRECT ATTEMPT:
def next_happy_year(year):   
    year += 1
    while len(set(str(year)))!=len(str(year)):
        year+=1
        
    return year
nexr_happy_year(1987)'''

'''FUNCTION TO CONVERT KILOMETERS TO METERS:
def myfunction():
    conversion_selection = input("Would you like to convert kilometres to metres or metres to kilometres?:")

    if conversion_selection.lower() == 'kilometres to metres':
        number_of_km = input("Enter the number of kilometres you want to convert to metres:" )
        number_of_metres = float(number_of_km) * 1000
        print(number_of_metres)
        return number_of_km
    elif conversion_selection.lower() == 'metres to kilometres':
        number_of_m = input("Enter the number of metres you want to convert to kilometres:")
        number_of_kilometres = float(number_of_m) / 1000
        print(number_of_kilometres)
        return(number_of_m)
myfunction()'''

'''base = '{}'
base.format("Cats")
print(base.format("Cats")*5)'''

'''GCD PROGRAM:
n1 = 4
n2 = 8
i=1
while i<=n1 and i<=n2:
    if n1%i==0 and n2%i==0:
        gcd=i
    i+=1
    print(gcd)
print(f'HCF of {n1} and {n2} = {gcd}')'''

#FUEL VALUE SUM RETURN:
#CODE DELETED

#CODING PROGRAM DAY 1:
'''with open("nice.txt" , 'r') as myfile:
    var = myfile.readlines()
    print(var)
for i in range(len(var)):
    var[i]=int(var[i])  
    if var.count(2020-int(var[i]))==1:
        print((var[i])*(2020-var[i]))
print(var)'''
'''with open("nice.txt" , 'r') as myfile:
    var = myfile.readlines()
for i in range(0 , len(var)-2):
    for j in range(i+1,len(var)-1):
        for k in range(j+1,len(var)):
            if int(var[i]) + int(var[j]) + int(var[k]) == 2020: 
                    print(int(var[i])*int(var[j])*int(var[k])) 
                    print(var[i])
                    print(var[j])
                    print(var[k])'''
                    
'''MULTIPLICATION TABLE FOR NUMBERS:
def multi_table(number): #general
    for i in range(1,11):
        print(f'{i} * {number} = ' + str(i*number))
multi_table(5)'''
'''def multi_table(number): #for codewars form with newline character only
    var = [f'{i} * {number} = ' + f'{i*number}\n' for i in range(1,11)]
    return(''.join(var)[:-1])
multi_table(5)'''

'''NOT PERFECT Advent Of Code DAY 2 CODE:
with open('nice.txt' , 'r') as myfile:
    count=0
    var = myfile.readlines()
    var = [var[i].replace('\n','') for i in range(len(var))]
    newvar = [var[i].replace('\n','')[:3].split('-') for i in range(len(var))]
    newnew = [list(var[i][7:]) for i in range(len(var))]
    newphile = [var[i][4] for i in range(len(var))]
    for j in range(len(var)):
        if newnew[j][int(newvar[j][0])-1]==newphile[j] and newnew[j][int(newvar[j][1])-1]==newphile[j]:
            count+=0
        if newnew[j][int(newvar[j][0])-1]!=newphile[j] and newnew[j][int(newvar[j][1])-1]==newphile[j]:
            count+=1
        if newnew[j][int(newvar[j][0])-1]==newphile[j] and newnew[j][int(newvar[j][1])-1]!=newphile[j]:
            count+=1
        
    print(count)'''

#Advent Of Code DAY 2:
'''with open('aoc.txt' , 'r') as myfile:
    count=0
    var = myfile.readlines()
    var = [var[i].replace('\n','') for i in range(len(var))]
    newnew = [var[i].replace(':' , '').replace('-',' ').split() for i in range(len(var))]
    for i in range(len(newnew)):
        if newnew[i][3].count(newnew[i][2]) >= int(newnew[i][0]) and newnew[i][3].count(newnew[i][2]) <= int(newnew[i][1]):
            count+=1
        else:
            count+=0
    print(count)
    print(var)
    print(newnew)'''

'''with open('aoc.txt' , 'r') as myfile:
    count=0
    var = myfile.readlines()
    var = [var[i].replace('\n','') for i in range(len(var))]
    newnew = [var[i].replace(':' , '').replace('-',' ').split() for i in range(len(var))]
    for i in range(len(newnew)):
        if newnew[i][3][int(newnew[i][0])-1]==newnew[i][2] and newnew[i][3][int(newnew[i][1])-1]==newnew[i][2]:
            count+=0
        if newnew[i][3][int(newnew[i][0])-1]==newnew[i][2] and newnew[i][3][int(newnew[i][1])-1]!=newnew[i][2]:
            count+=1
        if newnew[i][3][int(newnew[i][0])-1]!=newnew[i][2] and newnew[i][3][int(newnew[i][1])-1]==newnew[i][2]:
            count+=1
        if newnew[i][3][int(newnew[i][0])-1]!=newnew[i][2] and newnew[i][3][int(newnew[i][1])-1]!=newnew[i][2]:
            count+=0    
    print(count)'''

'''PIG LATIN:
def pig_it(text):
    variable = text.split()
    for i in range(len(text.split())):
        if variable[i].isalpha() == True and len(variable[i])!=1:
            variable[i]=str(variable[i][-len(variable[i])+1:])+str(variable[i][0])+'ay'
        elif len(variable[i])==1 and i!=len(variable)-1:
            variable[i]=str(variable[i][-len(variable[i])+1:])+'ay'
    return(' '.join(variable))'''

'''with open('aoc.txt','r') as myfile:
    grid = myfile.readlines()
    grid = [grid[i].replace('\n','') for i in range(len(grid))]
    x=0
    y=0
    count=0
    while True:
        try:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    i+=1
                    j+=3
                    if grid[i+1][j+3]=='#':
                        count+=1

        except IndexError as e:
            print(i , j)
        break

    print(count)
    print(grid)'''
#DAY 3 Advent Of Code PART 1 AND 2:
'''distance_moved_in_x = int(input("Enter Value 1"))
distance_moved_in_y = int(input("Enter Value 2"))
with open('aoc.txt') as myfile:
    var = [x for x in myfile.read().split('\n')[::distance_moved_in_y]]
number_of_trees_hit = 0
x=0
for y in var:
    number_of_trees_hit += (y[x%len(var[0])]=='#')
    x+=distance_moved_in_x
print(str(number_of_trees_hit)) '''

