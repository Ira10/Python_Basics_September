iterate over keys and values at the same time
grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}

print('\n')
print(grades.keys() ) # dict_keys(['Ana', 'Matt', 'John', 'Katy'])
print('\n')

print(list(grades.keys())) # ['Ana', 'Matt', 'John', 'Katy']
print('\n')

print(sorted(list(grades.keys()))) # ['Ana', 'John', 'Katy', 'Matt']
print('\n')

print('\n')
print(grades.values() ) # dict_values(['B', 'A', 'B', 'A'])
print('\n')

print(list(grades.values())) # ['B', 'A', 'B', 'A']
print('\n')

print('\n')
print(grades.items() ) # dict_items([('Ana', 'B'), ('Matt', 'A'), ('John', 'B'), ('Katy', 'A')])
print('\n')

print(list(grades.items())) # [('Ana', 'B'), ('Matt', 'A'), ('John', 'B'), ('Katy', 'A')]
print('\n')


for k,v in grades.items():
    print(f"key {k} has value {v}")

#     key Ana has value B
# key Matt has value A
# key John has value B
# key Katy has value A

# ####################### YOU TRY IT ######### solved it by myself
def count_matches(d):
    """ d is a dict
    Returns how many entries in d have the key equal to its value """
    # your code here
    count = 0
    for k,v in d.items():
        # print(k,v)
        if k == v:
            count += 1
    return count###


d = {1:2, 3:4, 5:6}
print(count_matches(d))   # prints 0

d = {1:2, 'a':'a', 5:5}
print(count_matches(d))   # prints 2

############################################################## extra sol 

def count_matches(d):
    """ d is a dict
    Returns how many entries in d have the key equal to its value """
    # your code here
    count = 0
    for x in d.keys():
        # print(k,v)
        if d[x] == x:  # value == key
            count += 1
    return count


d = {1:2, 3:4, 5:6}
print(count_matches(d))   # prints 0

d = {1:2, 'a':'a', 5:5}
print(count_matches(d))   # prints 2


grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A', 'Katy':'C','John':'D'}

print(grades.keys()) # dict_keys(['Ana', 'Matt', 'John', 'Katy'])
