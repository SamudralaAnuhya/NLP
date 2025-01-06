#its the advance lopping mechanism in python which is used for memory managing 

#if we wnat to print list 

my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    print(i)
    
#using iteraors 
my_list = [1,2,3,4,5,6,7,8,9,10]
my_iter = iter(my_list)
while True:
    try:
        print(next(my_iter))
    except StopIteration:
        print('End of the list')
        break
    