if __name__ == "__main__":
    import csv
    f = open('q4.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    
    mx = [0,0,0,0]
    mn = [0,0,0,0]
    stationmx = ["","","",""]
    stationmn = ["","","",""]
    for row in data:
            if row[-3] != '':
                if row[-2] != '':
                    for i in range (1, 5):
                        if mn[i-1] == 0:
                            mn[i-1] = int(row[-2])+int(row[-3])
                        if row[1] == "{0}호선".format(i):
                            if mx[i-1] < int(row[-2])+int(row[-3]):
                                mx[i-1] = int(row[-2])+int(row[-3])
                                stationmx[i-1] = row[3]
                            if int(row[-2])+int(row[-3]) < mn[i-1]:
                                mn[i-1] = int(row[-2])+int(row[-3])
                                stationmn[i-1] = row[3]
                                   
    
    print("*** Subway Report for Seoul on March 2023 ***\n")

    for i in range(1, 5):
        print("Line {0}:\n".format(i))
    
        print("Busiest Station: {0} ({1})\n".format(stationmx[i-1], mx[i-1]))

        print("Least Station: {0} ({1})\n".format(stationmn[i-1], mn[i-1]))
    
    f.close()
