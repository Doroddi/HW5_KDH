if __name__ == "__main__":
    import csv
    f = open('q1.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    sumA = 0
    sumMN = 0
    sumMX = 0 
    a = 0
    
    for row in data:
        if row[-3] != '':
            if row[-2] != '':
                if row[-1] != '':
                    sumA += float(row[-3])
                    sumMN += float(row[-2])
                    sumMX += float(row[-1])
                    a += 1
    avgA = sumA / a
    avgMN = sumMN / a
    avgMX = sumMX / a
    
    print("*** Annual Temperature Report for Seoul in 2022 ***\n")
    print("Average Temperature: {0:.2f} Celsius\n".format(avgA))
    print("Average Minimum Temperature: {0:.2f} Celsius\n".format(avgMN))
    print("Average Maximum Temperature: {0:.2f} Celsius\n".format(avgMX))

    f.close()
