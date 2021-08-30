# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15 # 1.Change the value 10 in x to 15.
print(x)

students[0]['last_name'] = 'Bryant' # 2.Change the last_name of the first student from 'Jordan' to 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres' # 3.In the sports_directory, change 'Messi' to 'Andres'
print(sports_directory)

z[0]['y'] = 30 # 4.Change the value 20 in z to 30
print(z)

#Iterate Through a List of Dictionaries

denverBroncos = [
        {'first_name': 'John', 'last_name': 'Elway'},
        {'first_name': 'Peyton', 'last_name': 'Manning'},
        {'first_name': 'Karl', 'last_name': 'Meklenburg'},
        {'first_name': 'Shannon', 'last_name': 'Sharpe'},
    ]

def interateDictionary(a):
    for key in range (0, len(a)):
        print(str(denverBroncos[key]).replace("{","").replace("'","").replace("}",""))
interateDictionary(denverBroncos)

#Get Values From a List of Dictionaries

denverBroncos2 = [
        {'first_name': 'John', 'last_name': 'Elway'},
        {'first_name': 'Peyton', 'last_name': 'Manning'},
        {'first_name': 'Karl', 'last_name': 'Meklenburg'},
        {'first_name': 'Shannon', 'last_name': 'Sharpe'},
    ]

def iterateDictionary2(key_name, some_list):
    for person in some_list:
        print(person[key_name])

iterateDictionary2('first_name', denverBroncos2)
iterateDictionary2('last_name', denverBroncos2)


#Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key_name in some_dict:
        print(len(some_dict[key_name]))
        for list in some_dict[key_name]:
            print(list)

printInfo(dojo)