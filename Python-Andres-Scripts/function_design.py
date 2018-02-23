import requests
import sys
from urllib.parse import urlencode

print(sys.executable)
print(sys.version)


# Method 1
def find_definition(word):
    q = 'define ' + word
    url = 'http://api.duckduckgo.com/'
    url += urlencode({'q': q, 'format': 'json'})
    response = requests.get(url)
    data = response.json()
    definition = data[u'Definition']
    print(definition)
    if definition == u'':
        raise ValueError('that is not a word')
    return definition


# Method 2
def find_definition_fix(word):
    q = 'define ' + word
    url = 'http://api.duckduckgo.com/'
    url += urlencode({'q': q, 'format': 'json'})
    data = call_json_api(url)
    definition = data[u'Definition']
    if definition == u'':
        raise ValueError('that is not a word')
    return definition


def call_json_api(url):
    response = requests.get(url)
    data = response.json()
    return data


# Method 3
def find_definition_fix_2(word):
    url = build_url(word)
    data = requests.get(url).json()
    return pluck_definition(data)


def build_url(word):
    q = 'define ' + word
    url = 'http://api.duckduckgo.com/'
    url += urlencode({'q': q, 'format': 'json'})
    return url


def pluck_definition(data):
    definition = data[u'Definition']
    if definition == u'':
        raise ValueError('that is not a word')
    return definition


# Check speeds of each function by commenting
print(find_definition('hi'))
print(find_definition_fix('hi'))
print(find_definition_fix_2('hi'))
