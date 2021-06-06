import requests

url = "https://tools.learningcontainer.com/sample-json-file.json"

try:
    data = requests.get(url)
    print(data.json())
except:
    print("Can't get dataset")

# fetch json url dataset
# https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
