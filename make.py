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
    long_desc = "{}, {}".format(desc, d[:4])
    for p in sorted(pics):
        if p == ".DS_Store":
            continue
        name = 'images/{}/{}'.format(d, p)
        thumb_name = 'thumbs/{}_{}'.format(d, p)

        if pic_index == 0:
            out +='            <a class="lightbox" href="{0}" data-caption="{2}"><img src="{1}" title="{2}"></a>\n'.format(name, thumb_name, long_desc)
        else:
            out +='            <a class="lightbox" href="{0}" data-caption="{1}" style="display: none;"></a>\n'.format(name, long_desc)
        pic_index += 1

    out +='<h3>{}</h3>\n'.format(desc)
    out +='        </div>\n'


with open("footer.html", 'r') as f:
    for line in f.readlines():
        out += line

with open("index.html", 'w') as f:
    f.write(out)
