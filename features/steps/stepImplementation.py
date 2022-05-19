from behave import *
import requests
from payLoad import *
from utilities.resources import *
from utilities.configurations import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    #
    context.urlAddBook = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headersAddBook = {"Content-Type": "application/json"}
    context.payLoad = addBookPayLoad("asfarergh")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.addBook_response = requests.post(context.urlAddBook, json=context.payLoad,
                                             headers=context.headersAddBook, )


@then('book is successfully added')
def step_impl(context):
    print(context.addBook_response.json())
    response_json = context.addBook_response.json()
    assert context.addBook_response.status_code == 200
    assert context.addBook_response.headers['Content-Type'] == 'application/json;charset=UTF-8'
    print(type(response_json))
    bookID = response_json['ID']
    print(bookID)
