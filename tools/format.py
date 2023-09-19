file_path = "./tools/format.in"
content = []
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.readlines()
with open('./tools/format.out', 'w', encoding='utf-8') as file:
    for item in content:
        item = item.replace("\"", "\'")
        item = item.replace("\n", "")
        file.write("\"{}\",\n".format(item))
