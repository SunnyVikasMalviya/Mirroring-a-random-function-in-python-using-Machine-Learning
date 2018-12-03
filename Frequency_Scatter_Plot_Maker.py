from matplotlib import style
from matplotlib import pyplot as plt


def frequency_plotter() :
    plt.title('Frequency Graph of 0-9')
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.grid(color = 'k') 
    for i in range(1,6) :
        sorted_file = open(str("sorted_dataset_to_count"+str(i)+".txt"), "r")
        #style.use('ggplot')
        for j in range(100) :
            line = sorted_file.readline(1000)
                #Since string is immutable in python,here line, we have to create a new \
                #variable line1
            line1 = list(line)
            line1 = list(map(int, line1))
                #lists are mutable  in python
            for k in range(10) :
                freq = line1.count(k)   #Counting the numbers from the file.
                plt.scatter(k, freq)
            sorted_file.readline(1)
                #The above line was included because a newline character is added\
                #at the end of each line of the sorted_file. If we try to read 1000\
                #characters without the above line, it will show an error.
        sorted_file.close()
    plt.show()
    print("Done!!!")         #For Debugging

frequency_plotter()
