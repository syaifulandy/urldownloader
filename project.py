import urllib
import os
a = 1
Location = "D:/DATA/Pictures/gambar/"  #GANTI SESUAI FOLDER TEMPAT MAU SIMPAN GAMBAR
with open("Project2.txt", "r") as ins:
    for line in ins:
        Loc = Location+str(a)+".jpg"
        a=a+1
        try:
            urllib.urlretrieve (line,Loc)
        except:
            print "gak ada data"
