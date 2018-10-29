def sort_files() :
    for i in range(1,6) :
        to_file = open(str("sorted_dataset_to_count"+str(i)+".txt"), "w")
        from_file = open(str("dataset"+str(i)+".txt"), "r")
        #lines = from_file.readlines()
        #for line in lines :            
        for x in range(100) :
            line = from_file.readline(1000)
            line1 = list(line)
            line1 = list(map(int, line1))
            sorted_list = sorted(line1)
            sorted_str = ''.join(str(e) for e in sorted_list)
            to_file.write(sorted_str)
            to_file.write("\n")
            #del(line)
            #del(line1)
        to_file.close()
        from_file.close()
    print("Done!!!")          #For Debugging    

sort_files()


