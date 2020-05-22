import json
from collections import Counter


def count_description():
    with open('newsafr.json', encoding='utf-8') as file:
        count = 0
        lines = file.readlines()
        for line in lines:
            if "description" in line:
                count += 1
        return count


with open('newsafr.json', encoding='utf-8') as file:
    data = json.load(file)
    string = ""
    temp_list = []
    for i in range(count_description() - 1):
        string += data['rss']['channel']['items'][i]['description']
    words = string.split()
    for letters in words:
        if len(letters) > 6:
            temp_list.append(letters)
    print(Counter(temp_list).most_common(10))