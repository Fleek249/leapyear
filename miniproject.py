#we import date module 
from datetime import date

date1=input('Enter starting date: ').split('-')#then we take a input seperated by '-' 
year1 , month1 ,day1=[int(i) for i in date1]# then we use lisst comprehension to convert the string input into integer
d1=date(year1,month1,day1)#then by using date module we convert the integer input into date

#we do the same for ending date
date2=input('Enter ending date: ').split('-')
year2 , month2 ,day2=[int(i) for i in date2]
d2=date(year2,month2,day2)


def leapyear(year1,year2):
    for i in range (year1,year2+1):
        if(i%4==0)and(i%100!=0):
            print(i,'is a leap year')
        elif i%400==0:
            print(i,"is a leap year")
def noleap(year1,year2):
    for i in range (year1,year2+1):
        if(i%4==0)and(i%100!=0):
            continue
        elif i%400==0:
            continue
        else:
            print(i,"is not a leap year")

leapyear(year1,year2)
noleap(year1,year2)