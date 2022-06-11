#
# This_list=["jahid","hasan","joy","ratul"]   # just list show
# print(This_list)                            # output

# This_list=['jahdi','hasan','joy','ratul','joy','jahid','hasan']  # same output  esy data same data show
# print(This_list)                                                 # output

# open_list=["small","beg","title","solder"]  # list function
# print(len(open_list))                       # len use list item number forth chek


# list1 = ["apple", "banana", "cherry"]      # item list use
# list2 = [1, 5, 7, 9, 3]                    # item list use
# list3 = [True, False, False]               # item list use
#
# print(list1)                               # output
# print(list2)                               # output
# print(list3)                               # output


# list1=["home","nathing",77,True,7.88]     # any item add list
# print(list1)                              # output
# print(type(list1))                        # what is the type of calls in the list ? solve the type function just


# item1=list(("data1","data2","data3"))  # direct use list function must use first Bracket
# print(item1)                           # output

# list1=["Item1",88,"Item2",88.999,"Item3",False] # Access Items
# print((list1[1]))                               # item number 6 but start 0 first item and list last item 5

# item3=[66,99,77,44,88]   # Negative Indexing
# print(item3[-1])         # Negative Indexing start list site


# item=["jahid","hasan","jesan","emon","akas","sorif","elias"]  # item number= 7
# print(item[1:7])# need =hasan to elias.print- index1 =hasan and index7= elias  index start=0 and end=item
# print(item[5:7])

# thislist = ["apple", "banana", "cherry"]  # list use the item
# thislist[1]="Black"                       # Change Item Value
# print(thislist[1])                        # print the output


"""Change Item Value"""

# item0=["world","Bangladesh","India","Japan","China","Usa","kolkata","word","Time","Home"]  # list
# item0[0]= "hecker"  # change item
# item0[7]="hecker"   # change item
# item0[8]="hecker"   # change item
# item0[9]="hecker"   # change item
# print(item0[0])     # output
# print(item0[7])     # output
# print(item0[8])     # output
# print(item0[9])     # output

"""Change a Range of Item Values"""
# homeline=[11,99,88,77,66,55,44,33,00]   # list item
# homeline[0:9]=[00,11]                   # change list item
# print(homeline)                         # output


""" Question-01 """
# Change the second and third value by replacing it with one value: third value=orange_2nd value=Mango
# ["apple", "banana", "cherry"]
#
# dallyitem=["apple", "banana", "cherry"]   # item list
# dallyitem[1:3]=["Mango","Orange"]         # change item
# print(dallyitem)                          # output

"""insert item of python"""
# this_item=["apple","eig","hen","tiger","royal"] # just insert data no move any data
# this_item.insert(1,"time")                      # just insert of ( count . change name ) insert method
# print(this_item)                                # output


"""Python - Add List Items  append() method use"""
# this_list=[77,99,00,66,33]
# this_list.append(34)        # use method =append()
# print(this_list)            # output

""" method extend() two list add one line """
# this_list=["home","some","time","nothing","country"]    # str type data but list use
# list_of=[88,99,00,77,66,55]                             # list  type data
# this_list.extend(list_of)                               # method=extend()_ two list data show just method use
# print(this_list)                                        # output

"""Python - Remove List Items"""
# this_list=["time","out","win"]      # list of python
# this_list.remove("out")             # method use =  remove()  list item remove
# print(this_list)                    # output

"""Remove Specified Index"""
# code=["time1","time2","time3","time4"] # list of python
# code.pop(3)                            # method use= pop()_data remove just serial number
# print(code)                            # OUTPUT

# """The del keyword also removes the specified index"""
# time_code=[77,99,00,66,55]    # just of python
# del time_code[2]              # del keyword use for python
# print(time_code)              # output

# """The clear keyword also remove the specified all index"""
# list_of=[88,00,99,77,66]   # just of python
# list_of.clear()            # clear keyword use for python
# print(list_of)             # output

"""python loop list"""
# home=["jahid","hasan","akas","imran"]    # just of python
# for x in home:                           # use for and in item is list serial
#     print(x)                             # output


"""Loop Through the Index Numbers"""
# this_list=[77,99,88,66,55,44,33,22]   # list of python
# for i in range(len(this_list)):       # use of keyword for,in,range,len try to keyword
#     print(this_list[i])               # serial kore item
#     print(i)                          # item total number
#     print(this_list)                  # all item serial by serial


"""
Loop Through the Index Numbers:
Use the range() and len() functions to create a suitable iterable.
"""
# this_list=["apple","banana","cherry"]   # list of python
# for i in range(len(this_list)):         # loop use
#     print(this_list[i])                 # OUTPUT
#     print(i)                            # OUTPUT


"""
Using a While Loop :
Use the len() function to determine the length of the list, then start at 0 and loop your way through
the list items by refering to their indexes.
"""
# this_list=["Apple","Banana","cherry"]   # list of python
# i=0                                     # fixed i=0 and three item output now 0 to 2
# while i < len(this_list) :              # use while loop and len method that set
#     print(this_list[i])                 # output
#     i=i+1                               # i value stor and 1 value ++

""" 

use from list of python : 

"""
# letter=["a","b","c","d"]    # list of python letter
# Zero=letter*5               # solve letter data 5th no [] use
# print(Zero)                 # output
# number=[letter]*4           # solve letter data 4th [] use
# print(number)               # output
# zero=[0]*10                 # 0 into 10 then 10 zero output
# print(zero)                 # output

"""
Looping Using List Comprehension

List Comprehension offers the shortest syntax for looping through lists:

"""
# # A short hand for loop that will print all items in a list:
# thislist = ["network", "data", "designer"]
# [print(x) for x in thislist]

"""
Youtube learn python list :

"""
# number=list(range(30))
# print(number)
# word=list("Computer" )
# print(word)
# word_list=["Ssd","Hdd","Ram","Rom","Cpu"]
# print(word_list[2],word_list[0])

