from bs4 import BeautifulSoup
import csv

with open("dfxml.xml") as fp:
    soup = BeautifulSoup(fp)

fileobjects = soup.find_all('fileobject')
with open ('dfxml-dates.csv', 'w', newline='') as csvfile:
    for fileobject in fileobjects:
        writer = csv.writer(csvfile)
        writer.writerow([fileobject.filename.text,fileobject.ctime.text])