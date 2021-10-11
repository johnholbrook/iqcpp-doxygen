from datetime import datetime

with open("index_content.html", "r") as content_file:
    custom_content = content_file.read()
    content_file.close()

custom_content = custom_content.replace("<date>", datetime.utcnow().strftime("%-d %B %Y at %-H:%M:%S UTC"))

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