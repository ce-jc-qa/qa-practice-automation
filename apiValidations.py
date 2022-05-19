import requests
import json

# Get method
response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'Rahul Shetty3'},)
# print(response.text)
# print(type(response.text))
#
# dict_response = json.loads(response.text)
# print(dict_response[11]['isbn'])

json_response = response.json()
# print(type(json_response))
# print(json_response[11]['isbn'])
assert response.status_code == 200
# print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

# Retrieve the book details with ISBN = bcd888effed

for actualBook in json_response:
    if actualBook['isbn'] == 'mnopqr':
        print(actualBook)
        break

expectedBook = {
        "book_name": "Automation Everywhere - Siddhant",
        "isbn": "mnopqr",
        "aisle": "11121"
    }

assert actualBook == expectedBook