#imports
from time import gmtime, strftime

#time for clock
min_init = int(strftime("%M", gmtime()))
sec_init = int(strftime("%S", gmtime()))

#values initialization
check_link = 0 #to check whether the line have space or not
clock = 0 #starts when program starts which generate time in seconds

#flags
busy_flag = 0
print('Enter Link :')
link = int(input())
line = 2 * link + 2

#line array list
line_array = []
for i in range(line):
    line_array.append(0)

#to from time table
nextarrival = []

#Process,completed,busy,block
process = 0
completed = 0
busy = 0
block = 0

while True:
    #INPUT NEXT ARRIVAL (from, to, length)
    print('Enter To, From, Length respectfully !!!')
    to = int(input())
    From = int(input())
    length = int(input())

    #saving next arrival in 2d array ;)
    i = 0
    if check_link < link :
        #to check busy status
        for a in nextarrival:
            if to == nextarrival[i][0] or From == nextarrival[i][1] or to == nextarrival[i][1] or From == nextarrival[i][0]:
                busy += 1
                busy_flag = 1
            i += 1

        #adding value to call in progress
        nextarrival.append([to,From,length])

        #input in line_array
        line_array[to - 1] = 1
        line_array[From - 1] = 1

        check_link += 1
        process += 1
    else :
        block += 1

    #clock change huna and check if length is completed or not

    # check_time = (int(strftime("%M", gmtime()))*60 + int(strftime("%S", gmtime()))) - (min_init*60 + sec_init)
    # if check_time >= length:
    #     del nextarrival[0]
    #     check_time = check_time - length
    #     completed += 1
    if busy_flag == 0:
        check_time = (int(strftime("%M", gmtime()))*60 + int(strftime("%S", gmtime()))) - (min_init*60 + sec_init)
        if check_time >= length:
            del nextarrival[0]
            check_time = check_time - length
            completed += 1
    else:
        busy_flag = 0


    print("\nPress 'Y' OR 'N' to Exit or Stay in call")
    i = input()
    if i=='y' or i == 'Y':
        print('You have Successfully exited :)')
        break;


#time ends
min_end = int(strftime("%M", gmtime()))
final_sec = int(strftime("%S", gmtime()))

#total time calculation
to = (min_end*60 + final_sec) - (min_init*60 + sec_init)


# Debugging
print('DEBUGGING')
print(nextarrival)
print('Line ARRAY')
print(line_array)
print(to)
print(sec_init)
print(final_sec)


#main output
print('Total Output :[ Process, Completed, Busy, Block]')
output = [process,completed,busy,block]
print(list(output))
