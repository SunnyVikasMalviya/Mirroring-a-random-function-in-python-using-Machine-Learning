from matplotlib import style
from matplotlib import pyplot as plt


def frequency_bubble_plotter() :
    plt.title('Bubble Graph of 0-9')
    plt.xlabel('Number')
    plt.ylabel('Frequency Bubble')
    plt.grid(color = 'k')
    dic = {}
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
##########UPDATED CODE FROM HERE##################
                key = str((k, freq))        #A key value for storing the value
                if key not in dic :         #in dic which shows the frequency of 
                    dic[key] = 1            #frequency of that digit in the file.
                else :                      #..and yes, it has been purposely 
                    dic[key] += 1           #written as 'frequency of frequency of'
                ss = (dic[key]**2) * 1      #because that's what it is.
                plt.scatter(k, freq, s = ss)#ss is the size of the bubble.
###################################################
            sorted_file.readline(1)
                #The above line was included because a newline character is added\
                #at the end of each line of the sorted_file. If we try to read 1000\
                #characters without the above line, it will show an error.
        sorted_file.close()
        #dic.clear()  #Uncomment this line for just combining individual bubble plots
    plt.show()
    print("Done!!!")         #For Debugging

frequency_bubble_plotter()
