Dictionary

- collection which unordered, changeable, and indexed.
- we use key to associate with its value, any value can be identified as long as we know the key.

myDict = {"Miller" : "a person who owns or works in a corn mill", 
          "Programmer" : "a person who writes computer programs"}
myArray = ["Miller", "Programmer", "App Miller"]
Accessing elements:

myArray[0]            ---------------------------> Miller

myDict["Miller"]   ---------------------------> a person who owns or works in a corn mill

- for an array index positions should be integers
- for a dictionary key (index) can be any type


How to create a dictionary?
Dictionary
- a mutable collection of key value pairs where each unique key maps to the value.
- implemented using hash tables which provides fast access to values based on their keys.

# using dict() constructor
myDict = dict()
print(myDict)
 
#using curvy brackets {}
myDict2 = {}
print(myDict2)
Time Complexity: O(1)
Space Complexity: O(1) 
- as the dictionary is empty and the only memory for the initial hash table structure is allocated.

# when using dict() constructor we only need to specify data type of the value
# dict() constructor will automatically konvert key into string data type
eng_sp = dict(one='uno', two='dos', three='tres')
print(eng_sp)
 
# using curvy brackets
# we need to specify data type of key as string here and use : 
eng_sp2 = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng_sp2)
Time Complexity: O(n) 
- because each key and value pair need to be inserted in the dictionary ant it will take some time
Space Complexity: O(n)

# using dict() constructor and list of tuples
eng_sp_list = [('one','uno'), ('two','dos'), ('three','tres')]
eng_sp3 = dict(eng_sp_list)
print(eng_sp3)


Dictionary in Memory

A hash table is a way of doing key-value lookups.
- You store the values in an array, and then use a hash function to find he index of the array cell that corresponds to your key-value pair.
- a Hash function maps a key to hash value and then index of the array. 

Elements of Dictionary: 
- key
- value
- hash fuction - minimizes the number of collusions (when different keys have )



# Dictionary vs List

 --------------------------------------------------------------------------------------------
|                   Dictionary                  |               List                        |
|-------------------------------------------------------------------------------------------|
|                   Unordered                   |               Ordered                     |
|               Access via keys                 |           Access via index                |
|           Collection of key values            |       Collection of elements              |
|   Prefferred when you have unique key values  |   Prefferred when you have ordered data   |
|           No duplicate members                |       Allow duplicate members             |
 --------------------------------------------------------------------------------------------


#################################################
# Time and Space Complexity in Python Dictionary

 ------------------------------------------------------------------------------------
|                Operation           |   Time Complexity    |    Space Complexity    |
| Creating a Dictionary              |    O(len(dict))      |         O(n)           |
| Inserting a Value in a Dictionary  |     O(1)/O(n)        |         O(1)           |
| Traversion a given Dictionary      |        O(n)          |         O(1)           |
| Accessing a given cell             |        O(1)          |         O(1)           |
| Searching a given value*           |        O(n)          |         O(1)           |
| Deleting a given value             |        O(1)          |         O(1)           |
 ------------------------------------------------------------------------------------

* if using in operator - Time Complexity is O(1) since the key is known