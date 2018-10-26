'''
Producing Dataset
'''

import random

def random_number_generator() :
    with open("dataset.txt", "w") as file :
        for j in range(0,100) :
            for i in range(0,1000) :
                random_number_generated = random.randint(0,9)
                #print(random_number_generated)      #For debugging
                file.write(str(random_number_generated))
        print("Done!!!")     #For debugging


random_number_generator()


'''
The function random_number_generator() generates one lakh random numbers between \
zero to nine arranged in 100 rows with each row containing 1000 numbers in a file\
named dataset.txt. 
'''
    
