from re import sub


paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

paragraph = paragraph.lower()
striped_paragraph = sub('[^a-z]', ' ', paragraph)

word_list = striped_paragraph.split()


word_dict = {}


for word in word_list:
    if word in banned:
        continue
    else:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
max_key = ''
max_value = 0
for key, value in word_dict.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_key)
