import os

os.system("rm -rf thumbs")
os.system("cp -r images thumbs")
os.system("mogrify -scale 30% thumbs/*/*")

