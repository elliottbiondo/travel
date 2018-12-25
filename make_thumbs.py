import os

os.system("rm -rf thumbs")
os.system("mkdir thumbs")

dirs = os.listdir("images")
if ".DS_Store" in dirs:
    dirs.remove(".DS_Store")

for d in reversed(sorted(dirs)):
    all_thumbs = os.listdir("images/{0}".format(d))
    if ".DS_Store" in all_thumbs:
        all_thumbs.remove(".DS_Store")
    thumb = sorted(all_thumbs)[0]

    name = 'images/{}/{}'.format(d, thumb)
    thumb_name = 'thumbs/{}_{}'.format(d, thumb)
    os.system("cp {} {}".format(name, thumb_name))

os.system("mogrify -scale 30% thumbs/*")

