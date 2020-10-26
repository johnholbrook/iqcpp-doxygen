with open("index_content.html", "r") as content_file:
    custom_content = content_file.read()
    content_file.close()

output = ""
with open("./docs/index.html", "r") as index:
    for line in index.readlines():
        output += line
        if line == '<div class="contents">\n':
            output += custom_content
    index.close()

with open("./docs/index.html", "w") as of:
    of.write(output)
    of.close()