import csv
     
f = open('south goa.csv')
csv_f = csv.reader(f)
     
for data in csv_f:
	print("Name: {0} , Popln: {1}".format(data[9],data[11]))
