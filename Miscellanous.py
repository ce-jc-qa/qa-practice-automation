import requests

# http://rahulshettyacademy.com
# 'visit-month'

cookie = {'visit-month': 'May'}
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False, cookies=cookie, timeout=1)
print(response.history)
print(response.status_code)


se = requests.session()
se.cookies.update({'visit-month': 'May'})

res = se.get("https://httpbin.org/cookies", cookies={'visit-year': '2022'})
print(res.text)

# Attachments
url = "https://petstore.swagger.io/pet/9843217/uploadImage"
files = {'file': open('')}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
