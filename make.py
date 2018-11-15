import os

out = ""
with open("header.html", 'r') as f:
    for line in f.readlines():
        out += line

dirs = os.listdir("images")
dirs.remove(".DS_Store")


for d in reversed(sorted(dirs)):
    pics = os.listdir("images/{0}".format(d))

    pic_index = 0
    out +='        <div class="col-xs-4 col-sm-4 col-md-4 col-lg-4">\n'
    desc = d[9:].replace("_", " ")
    #out +='<h7>{}</h7>'.format(desc)
    for p in sorted(pics):
        if p == ".DS_Store":
            continue
        name = 'images/{}/{}'.format(d, p)

        if pic_index == 0:
            out +='            <a class="lightbox" href="{0}"><img src="{0}" title="{1}"></a>\n'.format(name, desc)
        else:
            out +='            <a class="lightbox" href="{}" style="display: none;"></a>\n'.format(name)
        pic_index += 1

    out +='        </div>\n'

with open("footer.html", 'r') as f:
    for line in f.readlines():
        out += line

with open("index.html", 'w') as f:
    f.write(out)


