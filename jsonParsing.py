import json

courses = '{"name": "JCPayos", "languages": [ "Java", "Python"]}'

# Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

# get first language taught by trainer
# list_languages = dict_courses['languages']
# print(type(list_languages))
# print(list_languages[0])

print(dict_courses['languages'][0])

# ******************* Parse content present in Json file
with open('//Users//jpayos//Desktop//course.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(type(data['dashboard']))

# price of course 'RPA'
    print(type(data['courses']))
    for course in data['courses']:
        # print(course)
        if course['title'] == "RPA":
            print("The price for RPA is: ", course['price'])
            assert course['price'] == 45

with open('//Users//jpayos//Desktop//course1.json') as fi:
    data2 = json.load(fi)

    for courses in data['courses']:
        if courses["title"] == "RPA":
            for courses1 in data2['courses']:
                if courses1['title'] == "RPA":
                    # print(courses['title'], "is equal to", courses1['title'])
                    if courses['price'] == courses1['price']:
                        print("Price is equal for 2 different JSON file")
                    else:
                        print("Price is not equal for 2 different JSON file")

exampleJSON = '{"test1":[{"lang1": "Java", "lang2": "Python", "other":["fortran", "go", "C"]}]}'

data3 = json.loads(exampleJSON)
print(type(data3))

