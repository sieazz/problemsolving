import time


start = time.time()


year = 1900
day = 1
sunday_num = 0

def check_sunday():
    global year
    global sunday_num
    if year < 1901:
        return
    if day % 7 == 0:
        sunday_num += 1

while year < 2001:
    check_sunday()
    day += 31

    check_sunday()  
    if year % 4 == 0:
        if year % 100 == 0 and not (year % 400 == 0):
            day += 28
        else:
            day += 29
    else: day += 28

    check_sunday()
    day += 31

    check_sunday()
    day += 30

    check_sunday()
    day += 31

    check_sunday()
    day += 30

    check_sunday()
    day += 31

    check_sunday()
    day += 31

    check_sunday()  
    day += 30

    check_sunday()
    day += 31

    check_sunday()
    day += 30

    check_sunday()
    day += 31

    year += 1

print(sunday_num)
            
        
    


    




end = time.time()
print('time spent: {:.3f}'.format(end-start))
