from bs4 import BeautifulSoup
import csv

with open("dfxml.xml", encoding="utf8") as fp:
    soup = BeautifulSoup(fp)

fileobjects = soup.find_all('fileobject')
with open ('dfxml-dates.csv', 'w', newline='', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filename", "crtime","ctime", "mtime"])
    for fileobject in fileobjects:
        if fileobject.crtime == None:
            writer.writerow([fileobject.filename.text,'',fileobject.ctime.text,fileobject.mtime.text])
        elif fileobject.ctime == None:
            writer.writerow([fileobject.filename.text,fileobject.crtime.text,'',fileobject.mtime.text])
        else:
            writer.writerow([fileobject.filename.text,fileobject.crtime.text,fileobject.ctime.text,fileobject.mtime.text])
