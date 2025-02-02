from urllib.parse import quote

url = "GET /users/search?name=peter#foo"
encoded_url = quote(url, safe=":/?=")
print(encoded_url)