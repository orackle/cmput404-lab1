import requests

# question 2
print(requests.__version__ + "\n")


# question 5
# from 'https://www.w3schools.com/python/ref_requests_get.asp'
print(requests.get('http://www.google.com').status_code)


# question 10
print(requests.get('https://raw.githubusercontent.com/orackle/cmput404-lab1/main/script.py').text)
