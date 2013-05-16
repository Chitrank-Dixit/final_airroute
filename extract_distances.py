'''
from mmap import mmap,ACCESS_READ

from xlrd import open_workbook
print open_workbook('test.xls')
with open('test.xls','rb') as f:
    print open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ))
aString = open('test.xls','rb').read()
print open_workbook(file_contents=aString)
'''

from xlrd import open_workbook

def get_city_distances(workbook):
    wb = open_workbook(workbook) #wb = open_workbook('new.xls')
    nest=[]
    for s in wb.sheets():
        print 'Sheet:',s.name
        for row in range(s.nrows):
            values = []
            for col in range(s.ncols):
                values.append(unicode(s.cell(row,col).value))
            print ','.join(values)
            nest.append(values)
     
    print nest
    first_row=nest[0]
    for i in range(1,len(nest)):
        for j in range(1,len(nest[i])):
            nest[i][j]=float(nest[i][j])
    print nest,first_row[1:]

    # dictionary for excel data
    city_distances={};
    for a in first_row[1:]:
        city_distances[a]={}
        for b in nest[1:]:
            if b[0]==a:
                (city_distances)[a]=b

    print "\n\n",city_distances

    # remove 0.0 distance
    for a in city_distances:
        zeros=0.0
        if zeros in city_distances[a]:
            city_distances[a].remove(zeros)

    print city_distances
        

    city_hash={}
    for a in city_distances:
        print a
        city_hash[a]={};i=1
        for key in first_row[1:]:
            print key
            if a!=key :
                (city_hash[a])[key]=city_distances[a][i]
                print city_distances[a][i]
                i=i+1

    return city_hash

    
