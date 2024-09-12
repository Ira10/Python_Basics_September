my_d ={'Ana':{'mq':[10], 'ps':[10,10]}, 
       'Fredo':{'ps':[7,8], 'mq':[8]},
       'Eric':{'mq':[3], 'ps':[0]}      }

# print(my_d['Ana'[0]]) ## error

# print(my_d['Ana']['mq'][2])  # 5

# print(my_d['Ana']['mq'])  # [10, 0, 5, 7]

############# YOU TRY IT ###################

def get_average(data, what):
    """ data is a dict like my_d above
        what is 'ps' or 'mq'
        Returns the average of all elements in data that match 'what' """
    all_data = []
    for stud in data.keys():
        pass
        # Which one of the below is correct? 
        # A) 
        all_data = all_data + data[stud][what] ###  '+' is for concat
        # B) all_data.append(data[stud][what]) ## this will append a list in a list
        # C) all_data = all_data + data[stud[what]]
        # D) all_data.append(data[stud[what]]) 

    return sum(all_data)/len(all_data)

print(get_average(my_d, 'mq') )   # prints 7.0

###########################################################

