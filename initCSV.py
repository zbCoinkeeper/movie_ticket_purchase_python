import csv
 
with open("seat.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    i=0
    res=[]
    while i<80:
        i=i+1
        res.append("0")
    writer.writerows([res])

