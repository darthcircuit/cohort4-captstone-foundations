import csv

with open("countydata.csv", "rt") as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    # headers = ["Geographic Area","2010","2011","2012","2013","2014","2015", "2016","2017","2018","2019"]
    print(
        #    Geographic Area   2010          2011           2012           2013            2014          2015            2016           2017          2018            2019
        f'{headers[0]:22}{headers[1]:15}{headers[10]:15}{"Growth":15}{"Rate"}'
    )
    # f'{headers[0]:22}{headers[1]:15}{headers[2]:15}{headers[3]:15}{headers[4]:15}{headers[5]:15}{headers[6]:15}{headers[7]:15}{headers[8]:15}{headers[9]:15}{headers[10]}')
    print(
        f'{"----------------":22}{"---------":15}{"---------":15}{"-----":15}{"-----"}'
        # f'{"----------------":22}{"---------":15}{"---------":15}{"---------":15}{"-----":15}{"-------":15}{"--------":15}{"--------":15}{"-----":15}{"-----":15}{"-----"}'
    )
    # for row in csv_reader:
    for row in csv_reader:
        row = [str(i) for i in row]
        growth = int(row[1]) - int(row[10])
        rate = (int(row[10]) % int(row[1])) * 100
        print(f"{row[0]:<22}{row[1]:15}{row[10]:15}{growth:5}{rate:15}")
        # print(
        #     f'{row[0]:<22}{row[1]:15}{row[2]:15}{row[3]:15}{row[4]:15}{row[5]:15}{row[6]:15}{row[7]:15}{row[8]:15}{row[9]:15}{row[10]}')
