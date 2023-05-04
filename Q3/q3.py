if __name__ == "__main__":
    import csv
    f = open('q3.csv', 'r', encoding='ANSI')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    
    a=[0,0,0,0,0,0,0,0,0]
    for row in data:
            if row[-3] != '':
                if row[-2] != '':
                    for i in range(1, 10):
                        if row[1] == "{0}호선".format(i):
                            a[i-1] += int(row[-2])+int(row[-3])
    
    print("*** Subway Report for Seoul on March 2023 ***\n")
    
    mx = a.index(max(a))
    
    print("1st Busiest Line: Line {0}({1})\n".format(mx+1,a[mx]))
    
    temp = a[a.index(max(a))]
    a[a.index(max(a))] = -1
    mx = a.index(max(a))
    
    print("2st Busiest Line: Line {0}({1})\n".format(mx+1, a[mx]))

    a[a.index(-1)] = temp
    mn = a.index(min(a))
    
    print("1st Least Line: Line {0}({1})\n".format(mn+1, a[mn]))

    temp = a[a.index(min(a))]
    a[a.index(min(a))] = max(a)
    mn = a.index(min(a))

    print("2st Least Line: Line {0}({1})\n".format(mn+1, a[mn]))

    f.close()
