import csv
from matplotlib import pyplot

csvFile = open("2019-XTern- Work Sample Assessment Data Science-DS.csv", "r")
reader = csv.reader(csvFile)

scooter_id = []
xcoordinate = []
ycoordinate = []
power_level = []

for item in reader:
    if reader.line_num == 1:
        continue
    scooter_id.append(item[0])
    xcoordinate.append(item[1])
    ycoordinate.append(item[2])
    power_level.append(item[3])
csvFile.close()

pyplot.plot(xcoordinate, ycoordinate,)
pyplot.show()