#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to Extract Unique values dictionary values?

# In[2]:


def extract_unique_values(dictionary):
    unique_values = set()
    for values in dictionary.values():
        unique_values.update(set(values))
    return list(unique_values)

dictionary ={'key1':[1,2,3], "key2":[2,4,5],"key3":[3,4,6]}
unique_values = extract_unique_values(dictionary)
print(unique_values)


# 2.Write a Python program to find the sum of all items in a dictionary?

# In[16]:


def sum_dictionary(dictionary):
    total_sum = 0
    for values in dictionary.values():
        total_sum += sum(values)
    return total_sum

# example 
dictionary = {"key1": [1, 2, 3], "key2": [2, 4, 5], "key3": [3, 4, 6]}
total_sum = sum_dictionary(dictionary)
print(total_sum) 


# 3.Write a Python program to Merging two Dictionaries?

# In[29]:


def merge_dictionaries(dict1, dict2):
    merged_dict  = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 ={'c': 3, 'd': 4}
merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict)


# 4.Write a Python program to convert key-values list to flat dictionary?

# In[31]:


def convert_to_dict(key_values_list):
    flat_dict = {}
    for key_values in key_values_list:
        flat_dict[key_values[0]] = key_values[1]
    return flat_dict

key_values_list = [('a', 1), ('b', 2), ('c', 3)]
flat_dict = convert_to_dict(key_values_list)
print(flat_dict)


# 5.Write a Python program to insertion at the beginning in OrderedDict?

# In[36]:


from collections import OrderedDict
def insert_at_beginning(orderes_dict, key, value):
    ordered_dict[key] = key
    ordered_dict.move_to_end(key, last= False)
    
ordered_dict = OrderedDict([('a',1),('b', 2),('c', 3)])
insert_at_beginning(ordered_dict, 'x',0)
print(ordered_dict)


# 6.Write a Python program to check order of character in string using OrderedDict()?

# In[58]:


from collections import OrderedDict

def check_order(string, pattern):
    order_dict = OrderedDict.fromkeys(pattern)
    last_index = 0
    for char in string:
        if char in order_dict:
            if order_dict[char] == last_index:
                last_index += 1
            else:
                return False
    return True

string = "abcdefghijklmnopqrstuvwxyz"
pattern = "abc"
print(check_order(string, pattern))

string = "rajan"
pattern = "rjn"
print(check_order(string, pattern))

string = "rajan"
pattern = "rjnq"
print(check_order(string, pattern)) 


# 7.Write a Python program to sort Python Dictionaries by Key or Value?

# In[61]:


a = {'apple': 5, 'graps': 4, 'orange': 3, 'banana': 2, 'pear':1 }
sorted_dict_key = dict(sorted(a.items()))
sorted_dict_value = dict(sorted(a.items(), key = lambda item: item[1]))

print(sorted_dict_key)
print(sorted_dict_value)


# In[ ]:




