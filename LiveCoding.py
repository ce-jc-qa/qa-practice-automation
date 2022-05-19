import requests

# Attachments
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('Image/husky.jpeg', 'rb')}
r = requests.post(url, files=files, timeout=120)
print(r.status_code)
print(r.text)



