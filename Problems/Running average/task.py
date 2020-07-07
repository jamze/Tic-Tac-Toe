start = input()

my_list = [int(x) for x in str(start)]
new_list = []

for i in range(0, len(my_list)-1):
    run_avg = (my_list[i] + my_list[i+1])/2
    #run_avg = (my_list[i])
    #print(run_avg)
    new_list.append(run_avg)


print (new_list)