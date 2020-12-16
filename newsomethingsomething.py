#GITHUB REPOSITORY UPDATE:

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

'''CHECK THE EXAM:
def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr1[i]==arr2[i]:
            score+=4
        elif arr1[i]!=arr2[i] and arr2[i]!='':
            score-=1
        elif arr2[i]=='':
            score+=0
    if score<0:
        score=0
    return(score)'''

'''def myfunction():
    with open('nice.txt','r') as myfile:
        filelineread = myfile.readlines()
        for i in range(len(filelineread)):
            filelineread[i]=filelineread[i].replace('\n','')
        print(filelineread)
myfunction()'''

#AOC DAY 4:
#PART 1:
'''with open('aoc.txt','r') as myfile:
        lines = myfile.read().split('\n\n')
        for i in range(len(lines)):
            lines[i]=lines[i].replace('\n',' ')
count=0
#required_fields = ['byr', 'iyr' ,'eyr', 'hgt' ,'hcl' ,'ecl' ,'pid', 'cid']
number = 0
print(lines)
while True and number<len(lines)-1:
    #for i in range(len(required_fields)):
    if lines[number].count('byr')==1 and lines[number].count('iyr')==1 and lines[number].count('eyr')==1 and lines[number].count('hgt')==1 and lines[number].count('hcl')==1 and lines[number].count('ecl')==1 and lines[number].count('pid')==1 and lines[number].count('cid')==1:
        count+=1
        number+=1
    if lines[number].count('byr')==1 and lines[number].count('iyr')==1 and lines[number].count('eyr')==1 and lines[number].count('hgt')==1 and lines[number].count('hcl')==1 and lines[number].count('ecl')==1 and lines[number].count('pid')==1:
        count+=1
        number+=1
    else:
        count+=0
        number+=1
print(count)'''
#PART 2:
'''count=0
filelines = open('aoc.txt').read().split('\n\n')

def hclconditions(var):
  return(ord('0') <= ord(var) <= ord('9') or ord('a') <= ord(var) <= ord('f'))

def passportvalidator(key,value):
  if key == 'byr':
    return(value.isnumeric() and 1920 <= int(value)  <= 2002)
  if key == 'iyr':
    return(value.isnumeric() and 2010 <= int(value)  <= 2020)
  if key == 'eyr':
    return(value.isnumeric() and 2020 <= int(value)  <= 2030)
  if key == 'hgt':
    if value[-2:] == 'cm':
      return(value[:-2].isnumeric() and 150 <= int(value[:-2])  <= 193)
    if value[-2:] == 'in':
      return(value[:-2].isnumeric() and 59 <= int(value[:-2])  <= 76)
  if key == 'hcl':
    return(value[0] == '#' and all([hclconditions(value[i]) for i in range(1, len(value))]))
  if key == 'ecl':
    return(value in 'amb blu brn gry grn hzl oth'.split())
  if key == 'pid':
    return(len(value) == 9 and value.isnumeric())
  if key == 'cid':
    return True
for variable in filelines:
  d = {}
  for y in variable.split():
    a, b = y.split(':')
    d[a] = b
  #print([(passportvalidator(key, d[key]), key) for key in d])
  if len(d) == 8 and all([passportvalidator(key, d[key]) for key in d]):
    count += 1
  elif len(d) == 7 and 'cid' not in d and all([passportvalidator(key, d[key]) for key in d]):
    count += 1

print(count)'''

#REPLACE ALL INSTANCES OF FIND WITH REPLACE:
'''def replace_all(obj, find, replace):
    for i in range(len(obj)):
        if obj[i]==find and type(obj[i])==int:
            obj[i]=replace
        elif type(obj)==str:
            obj = obj.replace(find,replace)
    return(obj)'''

'''SORT MEN FROM BOYS:
def men_from_boys(arr):
    arr1=[]
    arr2=[]
    returnlist = []
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr1.append(arr[i])
        elif arr[i]%2!=0:
            arr2.append(arr[i])
    arr1.sort(reverse=False)
    arr2.sort(reverse=True)
    arrnew = arr1+arr2
    for i in range(len(arrnew)):
        if arrnew[i] not in returnlist:
            returnlist.append(arrnew[i])
    return(returnlist)'''

#RULE OF DIVISIBILITY BY 13:
#ALSO ONE OF THE MOST DISTURBING CODES I'VE COME UP WITH:
'''def thirt(n):
    generalset = [1,10,9,12,3,4]
    n = list(str(n))[::-1]
    for i in range(len(generalset)):
        if len(n)>len(generalset):
            extrageneralset = [int(n) for n in generalset[:len(n)-len(generalset)]]
            generalset.extend(extrageneralset)
    for i in range(len(n)):
            n[i] = int(n[i])*int(generalset[i])
    newsum = sum(n)
    iternew = list(str(newsum))[::-1]
    iternew = [int(iternew[i])*int(generalset[i]) for i in range(len(iternew))]
    new = sum(iternew)
    if new==newsum:
        print(sum(n))
    else:
        n = list(str(new))[::-1]
        n = [int(n[i])*int(generalset[i]) for i in range(len(n))]
        if sum(n)==new:
            print(new)
        elif sum(n)!=new:
            print(sum(n))
    print(sum(n))
thirt(101201920192012)'''

#DAY 5 ADVENT OF CODE PART 1 AND 2:
'''import collections

with open("nice.txt") as f:
    a = f.read().strip().split("\n")

highestseat = -1
seats = []
for i in a:
    mylineFB = "FBFBBFF"
    mylineFB = i[0:7]
    mylineFB = mylineFB.replace("F", "0")
    mylineFB = mylineFB.replace("B", "1")
    #print(mylineFB)
    mylineFB = "0b" + mylineFB
    mylineRL = i[7:]
    mylineRL = mylineRL.replace("R", "1")
    mylineRL = mylineRL.replace("L", "0")
    seats.append((int(mylineFB, 2), int(mylineRL, 2)))
b = (max(seats, key = lambda x: x[0]))

print("part 1", b[0] * 8 + b[1])
seats.sort()
char = []
for i in seats:
    char.append((i[0] * 8 + i[1]))
    #print(i)
x = char[0]
for i in range(1, len(char)):
    if char[i] - 1 != x:
        print("part 2", char[i] - 1)
        break
    x = char[i]'''

#(OR)


'''with open('nice.txt', 'r') as f:
    boarding_passes = f.read().splitlines()

def parse_seat_pos(board_pass: str) -> int:
    limit = (0, 2 ** len(board_pass) - 1)
    for step in board_pass:
        split = sum(limit) // 2
        lower, upper = limit
        if step in 'FL':
            limit = (lower, split)
        else:
            limit = (split+1, upper)
    return limit[0]

def seat_pos(board_pass: str) -> tuple[int, int]:
    bp_row, bp_col = board_pass[:7], board_pass[7:]
    row, col = parse_seat_pos(bp_row), parse_seat_pos(bp_col)
    return row, col

def seat_id(board_pass: str) -> int:
    row, col = seat_pos(board_pass)
    return row * 8 + col

def find_missing(lst: list) -> int:
    return next((x for x in range(lst[0], lst[-1]+1) if x not in lst))

if __name__ == '__main__':
    taken_seat_ids = [seat_id(board_pass) for board_pass in boarding_passes]

    print('Q1:', 'What is the highest seat ID on a boarding pass?')
    print('A1:', max(taken_seat_ids))

    print('Q2:', 'What is the ID of your seat?')
    print('A2:', find_missing(sorted(taken_seat_ids)))'''

'''INTRO TO LAMBDA'S THROUGH CALCULATING THROUGH FUNCTIONS ON CODEWARS:
def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x//y'''

'''PROGRAM FOR VALID SPACING:
def valid_spacing(s):
    if s.strip()==s:
        return(all(s.strip().split(' ' , len(s.split())-1)[i].count(' ')!=1 for i in range(len(s.strip().split(' ' , 1)))))
    else:
        return(False)
valid_spacing('XLiB e H')'''

#(OR)

#PROGRAM FOR VALID SPACING:
'''def valid_spacing(s):
    if s.strip()==s:
        print(all(s.strip().split(' ' , len(s.split())-1)[i].count(' ')!=1 and s.strip().split(' ' , len(s.split())-1)[i].count(' ')!=2 for i in range(len(s.strip().split()))))
    else:
        print(False)
valid_spacing('UKZ DWFP')'''

#AOC DAY 6
'''PART 1:  
with open('nice.txt','r') as myfile:
    myfile = myfile.read().split('\n\n')
    myfile = [myfile[i].replace('\n' , '') for i in range(len(myfile))]
    for i in range(len(myfile)):
        myfile[i]=len(set(myfile[i]))
    print('The sum is : ' + str(sum(myfile)))'''
'''counter1 = 0
counter2 = 0
PART 1 AND PART 2:
for item in open('nice.txt').read().split('\n\n'):
      splitstring = item.split('\n')
      emptylist = {}
      for line in splitstring:
        for char in line:
          if char not in emptylist:
            emptylist[char] = 0
          emptylist[char] += 1
      counter1 += len(emptylist)
      for key in emptylist:
        if emptylist[key] == len(splitstring):
          counter2 += 1

print('Part 1', counter1)
print('Part 2', counter2)'''

#PASCALS TRIANGLE:
'''def pascals_triangle(n):
    flatlist = []
    arr = [[0 for x in range(n)] for y in range(n)] 
    for counter in range (0, n): 
        for i in range (0, counter + 1):
            if i==0 or i==counter:
                arr[counter][i] = 1
            else: 
                arr[counter][i] = (arr[counter - 1][i - 1] + 
                                arr[counter - 1][i])
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            flatlist.append(str(arr[i][j]))
    while '0' in flatlist:
        flatlist.remove('0')
    for i in range(len(flatlist)):
        flatlist[i]=int(flatlist[i])
    print(flatlist)
pascals_triangle(6)'''

''' AOC DAY 7 PART 1 AND 2:

with open('nice.txt' , 'r') as myfile:
    lines = myfile.read().split('\n')
#print(lines)
gold_as_bag = {}
gold_as_sub_bag = {}
emptydict = {}

def counter_value(list_chosen, element_required):
  if element_required in emptydict:
    return(emptydict[element_required])
  counter = 1
  if element_required not in list_chosen:
    list_chosen[element_required] = []
  for number,alphabetical_part in list_chosen[element_required]:
    counter += number * counter_value(list_chosen, alphabetical_part)
  emptydict[element_required] = counter
  return(counter)

for line in lines:
  line = line.replace('.', '')
  #print(line)
  a, b = line.split(' bags contain ')
  #print(a)
  #print(b)
  parts = b.split(',')
  #print(parts)
  for part in parts:
    part = part.strip()
    if part == 'no other bags':
      continue
    c, d = part.split(' ', 1)
    c = int(c)
    d = d.replace('bags', '').replace('bag', '').strip()
    #print(c, d)
    if a not in gold_as_bag:
      gold_as_bag[a] = []
    gold_as_bag[a].append((c, d))
    #print(gold_as_bag)
    if d not in gold_as_sub_bag:
      gold_as_sub_bag[d] =[]
    gold_as_sub_bag[d].append((c, a))
    #print(gold_as_sub_bag)

counter_value(gold_as_sub_bag, 'shiny gold')
#print(emptydict)
print(len(emptydict) - 1)
emptydict = {} #reset emptydict to be a empty dictionary
print(counter_value(gold_as_bag, 'shiny gold') - 1)
#counter_value(gold_as_bag , 'shiny gold')
#print(emptydict)'''

#AOC DAY 8 PART 2:
'''with open('nice.txt' , 'r') as myfile:
    lines = myfile.read().split('\n')
print(lines)

def myfunction(which):
  counter = 0
  acc = 0
  emptyset = set([])
  while counter >= 0 and counter < len(lines):
    (a, b) = lines[counter].split()
    if counter == which and a == 'nop':
      a = 'jmp'
    if counter == which and a == 'jmp':
      a = 'nop'
    if counter in emptyset:
      return None
    emptyset.add(counter)
    if a == 'acc':
      acc += int(b)
      counter += 1
    elif a == 'jmp':
      counter += int(b)
    elif a == 'nop':
      counter += 1
  return acc

for i in range(len(lines)):
  ret = myfunction(i)
  if ret is not None:
    print(ret)'''

#AOC DAY 8 PART 1
'''with open('nice.txt' , 'r') as myfile:
    lines = myfile.read().split('\n')
print(lines)
counter = 0
acc = 0
emptyset = set([])
while counter >= 0 and counter < len(lines):
  (a, b) = lines[counter].split()
  if counter in emptyset:
    print(acc)
    exit(0)
  emptyset.add(counter)
  if a == 'acc':
    acc += int(b)
    counter += 1
  elif a == 'jmp':
    counter += int(b)
  elif a == 'nop':
    counter += 1'''

#AOC DAY 9 PART 1:
'''with open('nice.txt' , 'r') as myfile:
    lines = myfile.read().split('\n')
i=26
mylist = []
while True:
    for z in range(i-25,i):
        mylist.append(lines[z])
    for x in range(len(mylist)):
        for y in range(len(mylist)):
            if int(lines[i])==int(mylist[x])+int(mylist[y]):
                i+=1
            else:
                print(lines[i])
    mylist = []'''
#AOC DAY 9 PART 2:
'''with open('nice.txt' , 'r') as myfile:
    lines = myfile.read().split('\n')
    lines = [int(lines[i]) for i in range(len(lines))]
#print(lines)
def sum_min_max_function():
    a = 0
    b = 1
    s = lines[a]

    while True:
        if s == 257342611:
            return min(lines[a:b]) + max(lines[a:b])
        if s < 257342611:
            s += lines[b]
            b += 1
        if s > 257342611:
            s -= lines[a]
            a += 1

print('Part 2' , sum_min_max_function())'''


#AOC DAY 10 PART 1 , 2: 
'''with open('nice.txt' , 'r') as inputfile:
    lines = inputfile.read().split('\n')
#print(lines)
lines = [int(x) for x in lines]
lines.append(0)
sortedlines = sorted(lines)
sortedlines.append(max(sortedlines)+3)
counter1 = 0
counter2 = 0
for i in range(len(sortedlines)-1):
    difference = sortedlines[i+1] - sortedlines[i]
    if difference==3:
        counter2+=1
    elif difference==1:
        counter1+=1
print('Part 1: ' + str(counter2*counter1))
diff_combinations = {}
def diffwaystosort(i):
    if i==len(sortedlines)-1:
        return(1)
    if i in diff_combinations:
        return(diff_combinations[i])
    counter = 0
    for j in range(i+1 , len(sortedlines)):
        if sortedlines[j]-sortedlines[i]<=3:
            counter += diffwaystosort(j)
    diff_combinations[i] = counter
    return(counter)
print('Part 2: ' + str(diffwaystosort(0)))'''

#AOC DAY 11 PART 2:
'''with open('nice.txt') as file:
    lines = file.read().split('\n')
    #print(lines)
def HowManyAdjacentOccupied(v,i,j):
    counter = 0
    coordinates = [ [-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1] ]
    for x in coordinates:
        dx = i+x[0]
        dy = j+x[1]
        while dx>=0 and dx<len(v) and dy>=0 and dy<92 and v[dx][dy]=='.':
            dx+=x[0]
            dy+=x[1]
        #print(dx)
        #print(dy)
        if dx>=0 and dx<len(v) and dy>=0 and dy<92:
            counter += (v[dx][dy] =='#')
    return(counter)
def TotalOccupants(v):
    counter=0
    for x in v:
        counter+=x.count('#')
    return(counter)
for iterations in range(500):
    nextiteration = []
    for i in range(len(lines)):
        string = ''
        for j in range(len(lines[i])):
            #print(lines[i])
            character = lines[i][j]
            if character !='.':
                arrived_occupants = HowManyAdjacentOccupied(lines,i,j)
                if character == 'L' and arrived_occupants ==0:
                    character = '#'
                elif character == '#' and arrived_occupants>=5:
                    character = 'L'
            string+=character
        nextiteration.append(string)
    lines = nextiteration
    print('Part 2: ' + str(TotalOccupants(lines)))'''

#AOC DAY 11 PART 1:
'''with open('nice.txt') as file:
    lines = file.read().split('\n')
    #print(lines)
def HowManyAdjacentOccupied(a,i,j):
    counter = 0
    coordinates = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for x in coordinates:
        dx = i+x[0]
        dy = j+x[1]
        #print(dx)
        #print(dy)
        if dx>=0 and dx<len(a) and dy>=0 and dy<92:
            counter += (a[dx][dy] =='#')
    return(counter)
def TotalOccupants(a):
    counter=0
    for x in a:
        counter+=x.count('#')
    return(counter)
for iterations in range(500):
    nextiteration = []
    for i in range(len(lines)):
        string = ''
        for j in range(len(lines[i])):
            #print(lines[i])
            character = lines[i][j]
            if character !='.':
                arrived_occupants = HowManyAdjacentOccupied(lines,i,j)
                if character == 'L' and arrived_occupants ==0:
                    character = '#'
                elif character == '#' and arrived_occupants>=4:
                    character = 'L'
            string+=character
        nextiteration.append(string)
    lines = nextiteration
    print('Part 1: ' + str(TotalOccupants(lines)))'''

#AOC DAY 12 PART 1 , 2:
'''import math
coordinates = [[1,0] , [0,-1] , [-1,0] , [0,1]]
initial_position = [0,0]
direction = 0
with open('aoc.txt' , 'r') as myfile:
    data = myfile.read().split('\n')
for line in data:
    command = line[0]
    value = int(line[1:])
    if command == 'N':
        initial_position[1]+=value
    elif command=='S':
        initial_position[1]-= value
    elif command == 'E':
        initial_position[0]+=value
    elif command=='W':
        initial_position[0]-=value
    elif command=='F':
        initial_position[0]+=(value*coordinates[direction][0])
        initial_position[1]+=(value*coordinates[direction][1])
    else:
        if command=="R":
            direction+=(value//90)
        else:
            direction-=(value//90)
        direction = direction % 4
print('Part 1: ' + str(abs(initial_position[0])+abs(initial_position[1])))
with open('aoc.txt' , 'r') as myfile:
    data = myfile.read().split('\n')
ship_position = [0,0]
endpoint_position = [10,1]
endpoint_direction = 0
for line in data:
    command = line[0]
    value = int(line[1:])
    if command == 'N':
        endpoint_position[1]+=value
    elif command=='S':
        endpoint_position[1]-=value
    elif command=='E':
        endpoint_position[0]+=value
    elif command=='W':
        endpoint_position[0]-=value
    elif command=='F':
        ship_position[0]+=(value*endpoint_position[0])
        ship_position[1]+=(value*endpoint_position[1])
    else:
        if command=="R":
            value = 360-value
        endpoint_direction+=value
        endpoint_direction%=360
        radians = math.radians(value)
        endpoint_position = [round((endpoint_position[0] * math.cos(radians)) - (endpoint_position[1] * math.sin(radians))) , round((endpoint_position[0]*math.sin(radians)) + (endpoint_position[1]*math.cos(radians)))]
print('Part 2: ' + str(abs(ship_position[0])+abs(ship_position[1])))'''

#AOC DAY 13 PART 1,2:
'''from math import prod
def parse_input(file):
    with open(file, "r") as myfile:
        lines = myfile.read().splitlines()
        return int(lines[0]), lines[1].split(",")

def calculate_distance(earliest_timestamp,i):
    if earliest_timestamp%i == 0:
        return(0)
    else:
        return(i*(earliest_timestamp//i+1)-earliest_timestamp)

def part1(earliest_timestamp,ids):
    idlist = list(map(int,filter(lambda x:x!="x",ids)))
    closest_timestamp = [ids[0], calculate_distance(earliest_timestamp, idlist[0])]
    for i in idlist[1:]:
        current_distance = calculate_distance(earliest_timestamp, i)
        if current_distance < closest_timestamp[1]:
            closest_timestamp = [i, current_distance]
    return(closest_timestamp[0]*closest_timestamp[1])

#earliest_timestamp,ids = parse_input('nice.txt')
#print("Part 1:" + str(part1(earliest_timestamp,ids)))

def chinise_remainder_theorem(n, a):
    sum=0
    product=prod(n)
    for i,j in zip(n, a):
        p=product//i
        sum += (j*mod_inverse_function(p, i)*p)
    return(sum % product)

def mod_inverse_function(a, b):
    b0=b
    (x0,x1) = (0,1)
    if b==1:
        return 1
    while a>1:
        q = a//b
        (a,b) = ((b),(a % b))
        (x0,x1) = ((x1-q*x0) , (x0))
    if x1<0:
        x1+=b0
    return(x1)

def part2(ids):
    n = []
    a = []
    for (i,t) in enumerate(ids):
        if t!="x":
            n.append(int(t))
            a.append(int(t)-i)
    return(chinise_remainder_theorem(n, a))

def main_function():
    earliest_timestamp,ids = parse_input('nice.txt')
    print(f"Part 1: {part1(earliest_timestamp, ids)} \nPart 2: {part2(ids)}")

main_function()'''

#AOC DAY 14 PART 1:
'''with open('nice.txt' , 'r') as myfile:
    lines = myfile.read().split('\n')
#print(lines)
mem = {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
    else:
        index,miscellaneous,value = line.split()
        index = int(index.split('[')[-1][:-1])
        value = int(value) #parsing_completed
        new_value = 0 
        for i,bit in enumerate(reversed(mask)):
            value_of_bit = value&(2**i) #bitwise operator '&' (https://www.tutorialspoint.com/python/python_basic_operators.htm)
            if bit=='X':
                new_value+=value_of_bit
            elif bit=='1':
                new_value+=2**i
            elif bit=='0':
                pass
            else:
                pass
            #print(value,bit)
        mem[index]=new_value
        #print(index,new_value)
ans=0
for value in mem.values():
    ans+=value
print(ans)
#ans = 6559449933360'''

#AOC DAY 14 PART 2:
'''def indices(new_index,floating_values):
    if len(floating_values)==0:
        return([new_index])
    else:
        i=floating_values.pop(0)
        ans = indices(new_index,list(floating_values)) + indices(new_index+2**i , list(floating_values))
        return(ans)

with open('nice.txt' , 'r') as myfile:
    lines = myfile.read().split('\n')
#print(lines)
mem = {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split()[-1]
    else:
        if len(mask)==36:
            index,miscellaneous,value = line.split()
            index = int(index.split('[')[-1][:-1])
            value = int(value)
            new_index = 0
            floating_values = []
            for i,bit in enumerate(reversed(mask)):
                index_bit = index&(2**i)
                if bit=='X':
                    floating_values.append(i)
                elif bit=='1':
                    new_index+=2**i
                elif bit=='0':
                    new_index+=index_bit
                    pass
                else:
                    pass
        for index2 in indices(new_index , list(floating_values)):
            mem[index2] = value
        #print(index2,new_index)
ans=0
for k,v in mem.items():
    ans+=v
print('Part 2: ' + str(ans))
#ans = 3369767240513'''

#AOC DAY 15 PART 1,2:
'''def get_index_positions(list_of_elems, element):
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = list_of_elems.index(element, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return(index_pos_list)

starting_numbers = [6,13,1,15,2,0]

def get_closest_index(myArr , myNumber):
    return(min([ i for i in myArr if i < myNumber], key=lambda x:abs(x-myNumber)))

new_number_index = len(starting_numbers)
while len(starting_numbers)<=30000001:
    if starting_numbers.count(starting_numbers[new_number_index-1])==1:
        next = 0
    else:
        next = (new_number_index-1)-int(get_closest_index(get_index_positions(starting_numbers , starting_numbers[new_number_index-1]) , new_number_index-1))
    #print(starting_numbers)
    starting_numbers.append(next)
    new_number_index+=1
print(starting_numbers[29,999,999])'''

#OPTIMIZED CODE AOC DAY 15:
#PART 1,2
'''list1 = [6,13,1,15,2,0]
last_index = {}

for counter,number in enumerate(list1):
    if counter!=len(list1)-1:
        last_index[number] = counter

while len(list1) < 30000000:
    previous_num = S[-1]
    prev_prev = last_index.get(previous_num, -1)
    last_index[previous_num] = len(list1)-1
    if prev_prev == -1:
        next = 0
    else:
        next=len(list1)-1-prev_prev
    list1.append(next)
    #if len(S) == 2020:
        #print(next)
print(list1[-1])'''

#AOC DAY 16 PART 1,2:
#OPTIMIZED CODE:
'''import re
with open('nice.txt' , 'r') as myfile:
    L = myfile.read().split('\n')
#L = list(l.strip() for l in fileinput.input(files = 'nice.txt'))
limits = []
my_ticket = None
other_tickets = []
for l in L:
    integers = [int(x) for x in re.findall('\d+', l)]
    if len(integers) == 4:
        limits.append(integers)
    elif len(integers)>4:
        if my_ticket is None:
            my_ticket = integers
        else:
            other_tickets.append(integers)
n = len(limits)
n == 20
part1 = 0
ok_ = [[True for i in range(n)] for i in range(n)]
for values in other_tickets:
    assert len(values) == len(limits)
    ticket_valid = True
    for v in values:
        valid = False
        for a,b,c,d in limits:
            if a<=v<=b or c<=v<=d:
                valid = True
        if not valid:
            part1 += v
            ticket_valid = False

    if ticket_valid:
        for i,v in enumerate(values):
            for j,(a,b,c,d) in enumerate(limits):
                if not (a<=v<=b or c<=v<=d):
                    ok_[i][j] = False
print(part1)
map_ = [None for i in range(20)]
used = [False for i in range(20)]
found = 0
while True:
    for i in range(20):
        valid_j = [j for j in range(20) if ok_[i][j] and not used[j]]
        if len(valid_j) == 1:
            map_[i] = valid_j[0]
            used[valid_j[0]] = True
            found += 1
    if found == 20:
        break
#print(map_)
part2 = 1
for i,j in enumerate(map_):
    if j<6:
        part2 = part2*my_ticket[i]
print(part2)'''
