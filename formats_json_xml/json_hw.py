import json
from collections import Counter

with open('newsafr.json', encoding='utf-8') as file:
    data = json.load(file)
    string = ""
    length = len(data['rss']['channel']['items'])
    temp_list = []
    for i in range(length):
        string += data['rss']['channel']['items'][i]['description']
    string = string.lower().split()
    for letters in string:
        if len(letters) > 6:
            temp_list.append(letters)
    print(Counter(temp_list).most_common(10))