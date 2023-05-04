if __name__ == "__main__":
    import csv
    f = open('q2.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    mx = 0
    mn = 100
    mxdate = 0
    mndate = 0
    for row in data:
        if row[-2] != '':
            if row[-1] != '':
                diff = float(row[-1])-float(row[-2])
                if diff > mx:
                    mx = diff
                    mxdate = row[0]
                if diff < mn:
                    mn =diff
                    mndate = row[0]
    
    print("*** Annual Temperature Report for Seoul in 2022 ***\n")
    print("Day with the Largest Temperature Variation: {0}\n".format(mxdate))
    print("Maximum Temperature Difference: {0:.1f} Celsius\n".format(mx))
    print("Day with the Smallest Temperature Variation: {0}\n".format(mndate))
    print("Minimum Temperature Difference: {0:.1f} Celsius\n".format(mn))

    f.close()
