import requests
import json

# response = requests.get('https://reqres.in/api/users?page=2')
#
# json_response = response.json()
# assert response.status_code == 200
#
# actualData = json_response['data']
#
# for actualName in actualData:
#     if actualName['email'] == 'byron.fields@reqres.in':
#         print(actualName)
#         break
#
# assert actualName['first_name'] == 'Byron'
# assert actualName['last_name'] == 'Fields'
# assert actualName['avatar'] != ''

headers = {
    'x-kumu-auth': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjN6YnVBSExaVlBZWGVIaHIifQ.eyJqdGkiOiIzemJ1QUhMWlZQWVhlSGhyIiwiYXVkIjoiaHR0cHM6XC9cL3JlYWN0LWRldi5rdW11LmxpdmUiLCJpYXQiOjE2NTEwNDEwOTIsIm5iZiI6MTY1MTA0MTA5MiwiZXhwIjoxNjUzNjMzMDkyLCJwYXJhbXMiOnsidXNlcl9pZCI6IjN6YnVBSExaVlBZWGVIaHIiLCJ3ZWJ0b2tlbiI6ImI4NWVlMDMyODFhM2E2N2Q4NjdmYzQ3NzcyYjlhZWQxIiwidXVpZCI6IjY3Njc1IiwiaXNzdWVfYXQiOjE2NTEwNDEwOTJ9fQ.xj_EaTDowYaIghZDBsod2gH_ZJxS6NPbOIpUKIEbtCg',
    'device-id': '624d17ebd03c1'
    }
response = requests.post('https://api-kumu-live-dev.kumuapi.com/user/profile', headers=headers)
response_json = response.json()

assert response_json['code'] == '200', "Not 200"
print(response_json)
print(type(response_json['code']))
assert response_json['message'] == 'Request Success', "Wrong Message!"
assert response_json['data'] != None