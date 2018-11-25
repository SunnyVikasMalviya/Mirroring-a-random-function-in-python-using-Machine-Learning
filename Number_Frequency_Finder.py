def num_frequency_count() :
    for i in range(1,6) :
        sorted_file = open(str("sorted_dataset_to_count"+str(i)+".txt"), "r")
        #Creating new files that will store the frequency of all the numbers.
        frequency_file = open(str("frequency_of_numbers_per_line"+str(i)+".txt"), "w")
        for j in range(100) :
            line = sorted_file.readline(1000)
            #Since string is immutable in python,here line, we have to create a new \
            #variable line1
            line1 = list(line)
            line1 = list(map(int, line1))
            #lists are mutable  in python
            frequency_file.write(str("Line"+str(j)+" : "))
            for k in range(10) :
                freq = line1.count(k)   #Counting the numbers from the file.
                #Now we write it to the file.
                frequency_file.write(str('('+str(k)+','+str(freq)+')'))
            frequency_file.write('\n')
            sorted_file.readline(1)
            #The above line was included because a newline character is added\
            #at the end of each line of the sorted_file. If we try to read 1000\
            #characters without the above line, it will show an error.
        sorted_file.close()
        frequency_file.close()
    print("Done!!!")         #For Debugging

num_frequency_count()
