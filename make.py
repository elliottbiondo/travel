import os

out = ""
with open("header.html", 'r') as f:
    for line in f.readlines():
        out += line

dirs = os.listdir("images")
dirs.remove(".DS_Store")


out +='    <div class="row">\n'
for d in reversed(sorted(dirs)):
    pics = os.listdir("images/{0}".format(d))

    pic_index = 0
    for p in sorted(pics):
        if p == ".DS_Store":
            continue
        name = 'images/{}/{}'.format(d, p)
        out +='        <div class="col-md-3">\n'

        if pic_index == 0:
            out +='            <a class="lightbox" href="{}">\n'.format(name)
        else:
            out +='            <a class="lightbox" href="{}" style="display: none;">\n'.format(name)

        out +='            <img src="{}" alt="">\n'.format(name)
        out +='            </a>\n'
        out +='        </div>\n'
        pic_index += 1

out +="    </div>\n"

with open("footer.html", 'r') as f:
    for line in f.readlines():
        out += line

with open("index.html", 'w') as f:
    f.write(out)


