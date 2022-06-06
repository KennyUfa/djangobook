import csv

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12]
y=0
with open('spells.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for i in range(len(row)):
            print(len(row[i]))
            if x[i] < len(row[i]):
                x[i] = len(row[i])
        y+=1

    print(x,'-----',y)
