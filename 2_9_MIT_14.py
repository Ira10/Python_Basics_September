# #######################################
# ## EXAMPLE: getting grades using lists, do NOT do it this way...
# #######################################
# def get_grade_list(student, name_list, grade_list):
#     """ student is a str
#         name_list and grade_list are lists """
#     i = name_list.index(student)  ## find location in list for person
#     print(i)
#     grade = grade_list[i] # use location index to acess other info
#     return (student, grade)

# names = ['Ana', 'John', 'Denise', 'Katy']
# grade = ['B', 'A-', 'A', 'B']
# # can add more lists for course number, etc.
# print(get_grade_list('John', names, grade))

# # 1
# # ('John', 'A-')



# #######################################
# ## EXAMPLE: getting grades using list of lists, do NOT do it this way...
# #######################################
# def get_grades(who, what, data):
#     """ who and what are strings
#         data is a list containing lists of student info """
#     for stud in data:
#         if stud[0] == who:
#             for info in stud[1:]:
#                 if info[0] == what:
#                     return who, info
  
# eric = ['eric', ['ps', [8, 4, 5]], ['mq', [6, 7]]]
# ana = ['ana', ['ps', [10, 10, 10]], ['mq', [9, 10]]]
# john = ['john', ['ps', [7, 6, 5]], ['mq', [8, 5]]]

# grades = [eric, ana, john]

# print(get_grades('eric', 'mq', grades))  # ('eric', ['mq', [6, 7]])
# print(get_grades('ana', 'ps', grades))



#####################
## DICTIONARY OPERATIONS 
######################
# create dicts
# my_dict = {}
# d = {4:16}
# grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}

# print(d(4)) # TypeError: 'dict' object is not callable

# print(d[4]) # 16
# -------------------------------

# # get dict entries
# grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}
# print(grades['John']) # B
# print(grades['Grace']) # this gives an error since 'Grace' is not in dict -  KeyError: 'Grace'
# print(grades[1]) # KeyError: 1


# # add, edit, remove entries
# grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}
# grades['Grace'] = 'A' 
# print(grades) # {'Ana': 'B', 'Matt': 'A', 'John': 'B', 'Katy': 'A', 'Grace': 'A'}

# grades['Grace'] = 'C' 
# print(grades) # {'Ana': 'B', 'Matt': 'A', 'John': 'B', 'Katy': 'A', 'Grace': 'C'}

# del(grades['Ana'])
# print(grades)  # {'Matt': 'A', 'John': 'B', 'Katy': 'A', 'Grace': 'C'}

# test if keys are in dict
# grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}
# print('John' in grades) # True
# print('Daniel' in grades)  # False
# print('B' in grades)  # False

# ------------------------------------------------------
# iterate over keys and values
grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}
# print(grades.keys())  # dict_keys(['Ana', 'Matt', 'John', 'Katy'])
# print('\n')
# print(list(grades.keys()))  # ['Ana', 'Matt', 'John', 'Katy']
# print('\n')

# print(grades.values())
# print('\n')

# print(list(grades.values()))

# iterate over keys and values at the same time
# grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}
# print(grades.items() )
# print(list(grades.items()))

# for k,v in grades.items():
#     print(f"key {k} has value {v}")




# ################## YOU TRY IT #########################    my solution hihihihihihihi
# def find_grades(grades, students):
#     """ grades is a dict mapping student names (str) to grades (str)
#         students is a list of student names 
#     Returns a list containing the grades for students (in the same order) """
#     # your code here
#     L = []
#     for student in students:
#     # student is Matt, Katy -> the keys in the dictionary
#         L.append(grades[student])
    
#     return L       

# d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
# print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']
# print(find_grades(d, ['Ana', 'Katy', 'John', 'Matt'])) # returns ['B', 'A', 'B', 'C']


# ################## YOU TRY IT #########################   couldn't solve it, then I DID!! supremacy
# def find_in_L(Ld, k):
#     """ L is a list of dicts
#         k is an int
#     Returns True if k is a key in any dicts of L and False otherwise """
#     # your code here
#     for dict in Ld:
#         if k in dict:
#             return True
#     return False

  
# d1 = {1:2, 3:4, 5:6}
# d2 = {2:4, 4:6}
# d3 = {1:1, 3:9, 4:16, 5:25}

# print(find_in_L([d1, d2, d3], 2))  # returns True
# print(find_in_L([d1, d2, d3], 25))  # returns False

# ########################################################
