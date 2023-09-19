file_path = "graph/UnionFind.py"
content = []
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.readlines()
with open('./tools/format.txt', 'w', encoding='utf-8') as file:
    for item in content:
        item = item.replace("\"", "\'")
        item = item.replace("\n", "")
        file.write("\"{}\",\n".format(item))
