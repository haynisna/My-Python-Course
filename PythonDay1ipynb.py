#!/usr/bin/env python
# coding: utf-8

# # Python Programming: Essentials 1
# 
# #### Variables are used to store values. 
# 
# #### A string is a series of characters, surrounded by single or double quotes. 

# Hello world

# In[3]:


print("Hello World!") #print() is your first function


# Hello world via a variable

# In[5]:


message = "Hello Pairview!" #assigning a string to a variable
print(message) # message is a variable


# 
# 
# Concatenation (combining strings) 

# In[9]:


first_name = 'Fabien' 
last_name = 'GUERET' 
full_name = first_name + ' ' + last_name 
print(full_name)

# little funny one: multiply words! 
print(full_name * 5)  


# In[7]:


print(first_name , last_name ) # the comma adds a space automatically 


# 
# 
# ## List
# 
# A list stores a series of items in a particular order. 
# 
# You access items using an index, or within a loop. 
# Make a list 

# In[10]:


bicycles = ['mountain', 'road', 'race', 'penny-farthing']

print(bicycles)


# In[11]:


addon = ['raleigh','brompton']
bicycles = bicycles + addon # add a list to a list
print(bicycles)


# Get the first item in the list

# In[12]:


first_bike = bicycles[0] 
print (first_bike)


# Get the last item in the list

# In[ ]:


last_bike = bicycles[-1]
print(last_bike)


# In[16]:


# write code to print the penultimate (i.e. one before last) bike
one_before_last_bike = bicycles[-2]
print(one_before_last_bike)  # what i did 


# In[17]:


second_last = bicycles[4] # counts from 0 - 1st one
print(second_last)


# In[18]:


one_b4_last = bicycles[-2] # counts backwards from -1 - last one
print(one_b4_last)


# # Working with Strings
# 
# ## split() function

# In[26]:


# the function split() cuts a string at specified character position then store the result in a list

sentence = 'UK house prices grew two per cent year on year for September.'

words = sentence.split(' ') # split is function, sentence is variable - shown above
words2 = sentence. split ('e') # can put any character here 

print(words)
print(words2)

url = 'https://www.netflix.com/gb/'

elements = url.split ('/')
print (elements)

url = 'https://www.theguardian.com/society/2018/oct/11/john-major-universal-credit-could-result-in-backlash-like-poll-tax'

elements = url.split ('/') # able to find date with url.split etc. 
print (elements)


# In[34]:


# adapt to get the first and second part from an email address
email = "trainingsupport@pairview.co.uk"

########## your code below#############

parts = email.split ('@')
print(parts)

individual = parts [0] # first part
company = parts [-1 # second part 
print(individual, company) #prints both 


# In[40]:


# write code to get the first name and the last name from the full name that can include 1 or many middle names

################your code################
myname = "Elizabeth Alexandra Mary Windsor"

names = myname.split(' ')
print(names)

first_name = names [0]
last_name = names[-1]
print(first_name, last_name)



# ## join() function

# In[45]:


# the function join() take a list of strings and concatenate its elements separated by the character passed to it
separator =' ' # define separator 
sentence = separator.join(words) 

print(sentence)


# ## strip() function

# In[56]:


# the function strip() removes unwanted characters (spaces usually) 
# at the beginning and ending of a string
stri = "0000000@@this is a polluted string example@@0000000"
stri2 = "0000000@@this is a polluted # string example@@0000000"
clean = stri.strip ('0').strip('@')
print(stri.strip( '0' ).strip('@)')) # only touches the first and last- removes beginning and then end- always start with beginning
print(clean)
print (stri2.strip( '0' ).strip('@)'))


# ## replace(old_word,new_word) function

# In[57]:


# and now I present you the function replace
print(stri. strip('0').strip('@').replace( 'polluted ' , 'cleaned ' ))
print(stri2. strip('0').strip('@').replace( '# ' , '' ))


# # for in statement
# ### Looping through a list 

# In[58]:


bicycles = ['mountain', 'road', 'race', 'penny-farthing'] # fixed order 0,1,2,3

# for in:  statement
# for i: 1 to 4 step 2 do 
#     print (elements[i-1])
# end for 

for element in bicycles: # colon part of statement, element can be named anything 
    print(element) # indentation 

    
print('End')    # prints with list without indentation 


# ## range () function
#     

# In[62]:


# loop above equivalent to 

for i in range(0,4): #for i = 0 to 4 do in C++
    print(bicycles[i])


# In[ ]:


# range function tester


# In[59]:


for number in range(8): # one only attribute = range(0,8) # counts at 0
    print(number)


# In[60]:


for number in range(2,8): # first is start , second the one before
    print(number)


# In[61]:


for number in range(2,8,2): # first is start , second the one before the last # 3rd the step
    print(number)


# ## Adding items to a list

# In[66]:


# add another string
bicycles.append('peugeot') # if you run again will add again, modifies bicycles 
print(bicycles)
# equivalent to 
bicycles = bicycles + ['peugeot']


# In[65]:


# aside: insert 
bicycles.insert(2,'BMX')
print(bicycles)


# In[71]:


bicycles.remove('peugeot') #removes the first instance in the list 
print(bicycles)


# In[72]:


bicycles.pop() #removes the last item in the list 
print(bicycles)


# In[64]:


# add a number!
bicycles.append(22)
print(bicycles)


# In[73]:


# add a list!!
bicycles.append(['derailleur','shimano']) 
print(bicycles)

#YOU CAN ADD ANYTHING!!!


# In[77]:


# Code for accessing the second item in the list inside the list - in 73, list 
print(bicycles[-1][-1])
print(bicycles[-1])
print('words'[-1]) # list of characters 


# ## Making numerical lists

# In[80]:


# initialisation 
cubes = [] # if you remove initialisation will run again and again 

for number in range(1, 7): 
    cubes.append(number**3) #to the power=** 3 in the range 1 to 7, shows 6, always - 1 the end 
print(cubes)

# ** operator is power


# In[96]:


# write code to calculate the average of numbers from 5 to 15
# the average is the sum divided by the number of elements

# series = [5,6,7,8,9...15]
# hint range 

series = [5,6,7,8,9,10,11,12,13,14,15]
#range[5,16]


# calculate the sum 
# element1 + element2 ...element15 
# initialisation 
Sum = 0 
#count = 0 
for number in series: 
    Sum = Sum + number 
    #count = count + 1 
    
print(Sum)
count= len(series)
average = Sum / count
print (average)
# calculate number of items 
# hint len function 





# In[99]:


Sum = 0 
count = 0 
for number in range(5,16):
    Sum = Sum + number 
    count = count + 1

average = Sum / count
print (average)
    


# len() function 

# In[79]:


# the amazing Len function - aka the length of everything
#len()    
   
l = len (range(5,16))
print(l)

print( len (bicycles)) #check above bicycles 

print(len('guardian'))
    


# # List comprehensions : Advanced
# 

# In[103]:


cubes = [x**3 for x in range(1, 7)] 
print(cubes)

# equivalent to 


# In[104]:


cubes = [] 
for x in range(1, 7): 
    cubes.append(x**3) 
print(cubes)


# ## List comprehension exercise 
# 
# Write one line of Python that takes this list and makes a new list that has only the even elements of this list in it.

# In[120]:


list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list)


# ## Slicing a list 

# In[105]:


finishers = ['Sue','Elliot', 'Kumiko','Damien'] 
first_two = finishers[:2] # all up to 2 but not 2, to the left 
print(first_two)


# In[107]:


last_two = finishers[2:] # from 2 (included) up to end, to the right 
print(last_two)


# In[108]:


f = finishers[:2] + finishers[2:]
print(f)


# In[109]:


last_two = finishers[-2:] #last two 
print(last_two)


# ## index() function
# index function returns the first occurence in the list

# In[110]:


# want a table with the position next to the element
finishers = ['Sue','Elliot', 'Kumiko','Damien','Elliot'] 
print('Index | Finisher')
for f in finishers:
    print(finishers.index(f), ' | ',f)
# index function returns the first occurence in the list
# a.k.a. vlookup in Excel 


# In[113]:


finishers = ['Sue','Elliot', 'Kumiko','Damien','Elliot'] 
L =len(finishers)
print('Index | Finisher')
for number in range(0,L):
    print(number  , ' | ', finishers[number])
        


# Copying a list

# In[114]:


copy_of_bicycles = bicycles[:] 
print(copy_of_bicycles)


# ### Tuples
# 
# Tuples are similar to lists, but the items in a tuple can't be modified. 

# Making a tuple 

# In[115]:


# tuple of numbers
dimensions = (1920, 1080)

# tuples of tuples
pushbikes= ('mountain', 'road', 'race', 'penny-farthing')

#tuple of different types of variables
hold_all = (35, 'Data Science', [1,2,3,4,5], (1,7))

print(hold_all)

# lists can be modified 
bicycles[0]='raleigh'
print(bicycles)


# In[ ]:


#hold_all[0]= 34

print(hold_all[0])


# ### If statements are used to test for particular conditions and respond appropriately.
# 
# # if (condition) : action

# In[116]:


# If statement
age = 25
commonwealth = True
if age >= 18: 
    print("You may be able to vote")


# In[117]:


if (age >= 18 and commonwealth == True): #conditional operator equal, see below conditions
    print("You can vote!") 
    


# In[119]:


#If-elif-else statements 
if age < 4: 
    price = 0 
elif age < 18:
    price = 10 
elif age > 65: 
    price = 12 
else: price = 15

print(price)


# Conditions
# 
# tests equals
# x == 42 
# 
# not equal 
# x != 42  
# 
# greater than 
# x > 42 
# 
# greater than or equal to
# x >= 42 
# 
# less than
# x < 42 
# 
# less than or equal to
# x <= 42

# In[121]:


x = 57 # i assign 57 to x
# (x<42) is  a test with a value of True of False
print('is x smaller than 42?', x < 42)

X =(x > 42 )
print('is x bigger than 42?', X)

if X : 
    print(X)


# In[122]:


test = 50
x = (test!= 55)

if x :
    print(x)


# ## Conditional test with lists 
# ## IN
# ## NOT IN

# In[123]:


print('downhill' in bicycles)


# In[124]:


print('downhill' not in bicycles)


# Assigning boolean values

# In[ ]:


game_active = True 
can_edit = False

if game_active or can_edit:
    print('yay')


# # Exercise
# 
# Take a list of numbers
# and write a program that prints out all the elements of the list that are less than 5.

# In[127]:


# set list

List = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# your code below
L = len(List)
for number in range (0,L): 
    if List[number] < 5: print(List[number])

    


# In[128]:


for item in List: 
    if item < 5 : print(item)
        
for x in List: 
    if x < 5 : print(x)


# In[132]:


Result = [number for number in List if number < 5] 
print(Result)
print(len(Result))


# In[134]:


# initialisation 
count = 0 

for x in List: 
    if x < 5 : 
        print(x)
        count = count + 1
print('numbers under 5 :', count)


# In[129]:


# extra: create a list of random number using the
# random generator below

import random
for x in range(10):
  print(random.randint(1,101))


# # Dictionaries 
# they store connections between pieces of information
# 
# Each item in a dictionary is a key-value pair

# Simple dictionaries {}

# In[137]:


word_frequency = {'Data' : 14, 'Science': 10, 'Machine': 5, 'Learning' : 8} 
# dictionary-list of pairs tuple - a primary key with a value attached to it 

real_dictionary = {'a': 'string that defines a', 'abc': 'definition of abc'} 


# with different value types
car = {'make' : 'Mazda', 'model' : '3 sport', 'engine_size_cc': 2259,
       'colour': 'laser blue', 'dimensions_mm' : {'w':1795 , 'l':4465 , 'h':1465}}
#dictionary inside a dictionary dimensions w,l,h 


# Accessing a value

# In[138]:


print("The car colour is " + car['colour'])
#dictionary[key] accesses the value in the key, value pair 


# In[139]:


#write code to retrieve the dictionary inside the dictionary

dictionary = car['dimensions_mm']
print(dictionary)


# In[141]:


# retrieve the value in the dictionary inside the dictionary

print('car length is', car['dimensions_mm']['l'], 'mm')


# In[ ]:


Adding a new key-value pair
car = {'make' : 'Mazda', 'model' : '3 sport', 'engine_size_cc': 2259,
       'colour': 'laser blue', 'dimensions_mm' : {'w':1795 , 'l':4465 , 'h':1465}} # just reminder, already run 


# In[142]:


car['transmission_type'] = 'automatic' # adding transmission type to dictionary 
#dic[key] = v 
print(car)


# Values, Keys and Items

# In[143]:


print('list of tuples in the dictionary','\n',car.items(),'\n') 
#\n...\n is new line, tuples is car.items - dict_items() with value


# In[144]:


print('list of keys','\n',car.keys(),'\n') # .keys 


# In[145]:


print('list of values','\n',car.values(),'\n') #.values


# Looping through all keys

# In[146]:


# for keys in dictionary:
# for i = 0 to 6: k=keys[i]
for k in car.keys(): 
    print(k + ' is a car characteristic') 


# Looping through all the values

# In[147]:


#write code to loop through all the values

for v in car.values(): 
    print(v , ' is a car characteristic')


# Looping through all key-value pairs

# In[148]:


# python difference or characteristic
print(str(car['dimensions_mm']['l']))

for k,v in car.items():
    print(k ,' is ' , v)
    print(k + ' is '+ str(v)) #str is string, use string because plus is an operator 


# In[149]:


Tuples_List = [(1,2,3) , (4,5,6) , (7,8,9)]

for a , b , c in Tuples_List: 
    print(a*b/c)


# In[151]:


#Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

#Sample Dictionary : 
dic1={1:'Royal Dutch Shell', 2:'BP'} 
dic2={3:'Total', 4:'Volkswagen'} 
dic3={5:'Glencore Xstrata',6:'Gazprom'}

#initialisation 
final_dic = dic1 

c
for k,v in dic3.items():
    final_dic[k] = v    
    
print(final_dic)
    
    
#for k,v in car.items():
#car['transmission_type'] = 'automatic'



# In[158]:


# Write a Python script to check if a given key already exists in a dictionary.

test_number = 7
key_in_dictionary = False #Assigning boolean values

for k in final_dic.keys():
    if k == test_number : key_in_dictionary = True 

if key_in_dictionary : print(test_number, ' is a key already in the dictionary')
else: print(test_number, ' is not a key already in the dictionary')
    
    
### your code ####


# In[ ]:


key_in_dictionary = test_number in final_dic.keys() #same as the above for...if...etc


if key_in_dictionary : print(test_number, ' is a key already in the dictionary')
else: print(test_number, ' is a key already in the dictionary')


# ### Programs can prompt the user for input. 
# All input is stored as a string. 
# 
# Prompting for a value

# In[159]:


# prompting for a value
name = input("What's your name? ") 
print("Hello, " + name + "!") 


# In[160]:


# prompting for a number

age = input("How old are you? ") #return a string
age = int(age) #convert
print(age)


# In[161]:


pi = input("What's the value of pi? ") 
print(pi)
pi = float(pi)


# # Exercise
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# In[167]:


#initialisaion
current_year = 2018


name = input ("What is your name? ")

age = input("How old are you? ") #return a string
age = int(age) #convert
wait = 100 - age 
year = current_year + wait 
print("Hello,",name, 'you will turn 100 years old in', year) 


# In[168]:


import random

for x in range(10):
  print(random.randint(1,101))

