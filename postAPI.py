import requests
import json
import configparser
from payLoad import *
from utilities.resources import *
from utilities.configurations import *

# urlAddBook = getConfig()['API']['endpoint'] + ApiResources.addBook
# headersAddBook = {"Content-Type": "application/json"}
# addBook_response = requests.post(urlAddBook, json=addBookPayLoad("asfarer"), headers=headersAddBook, )
#
#
# print(addBook_response.json())
# response_json = addBook_response.json()
# assert addBook_response.status_code == 200
# assert addBook_response.headers['Content-Type'] == 'application/json;charset=UTF-8'
# print(type(response_json))
#
# bookID = response_json['ID']
# print(bookID)
#
# # Delete a book
# urlDeleteBook = getConfig()['API']['endpoint'] + ApiResources.deleteBook
# headersDeleteBook = {"Content-Type": "application/json"}
# deleteBook_response = requests.post(urlDeleteBook, json={"ID": bookID}, headers=headersDeleteBook, )
#
# assert deleteBook_response.status_code == 200
# res_json = deleteBook_response.json()
# print(res_json["msg"])
# assert res_json["msg"] == "book is successfully deleted"

# Authentication
se = requests.session()
se.auth = auth = ('ce-jc-qa', getPassword())

url = 'https://api.github.com/user'
github_response = requests.get(url, auth=('ce-jc-qa', getPassword()))

print(github_response.status_code)

url2 = "https://api.github.com/user/repos"
response = se.get(url2, auth=('ce-jc-qa', getPassword()))
print(response.status_code)