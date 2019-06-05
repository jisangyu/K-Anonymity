#!/usr/bin/python


with open('pos.condition.count') as pos :
    poslines = pos.readlines()

with open('neg.condition.count') as neg :
   neglines = neg.readlines()


print(poslines[0][5:])
print(int(poslines[0][0:4]))




for posline in poslines:
    for negline in neglines :
        if negline[5:] == posline[5:] :
            #print (negline )
            #print (posline)
            pos=int(posline[0:4])
            neg=int(negline[0:4])
            print (str(float(pos/neg))+"|"+str(pos) +"/"+str(neg) +" |"+negline[5:-1])

            break











