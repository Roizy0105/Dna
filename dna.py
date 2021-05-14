import sys
import csv

if len(sys.argv) != 3:
    print("Input Files")
    
with open(sys.argv[1]) as csv_file:
    
    # create an empty array wich will later be a 2d array
    array = []
    # created a varuble that will keep track of the rows entered into the array
    length = 0
    # created a while loop to itarate throguh the csv file
    while True:
        # on every itaration read one line
        csv_reader = csv_file.readline()
        # if the readline function did not return a line then exit the while loop
        if not csv_reader:
            break
        # remove the \n from the end of the line
        csv_reader = csv_reader.rstrip("\n")
        # set this array to 0 on every itaration so that it has only one line in it at a time
        temp_array = []
        # crate a width varuble to keep track how long the line is
        width = 0
        # loop through every word in the line
        for word in csv_reader.split(","):
            
            # add the word to the 1d array    
            temp_array.append(word)
            # add to the width varuble to keep track of the width
            width += 1
        # add the array of this one line to the 2d array
        array.append(temp_array)
        # keep track of the length of this array
        length += 1
    # itarate through the 2d array and change the number strings to values
    for i in range(1, length):
        for j in range(1, width):
            array[i][j] = int(array[i][j])
    
    # open the text file
    with open(sys.argv[2]) as text_file:
        # take all the text from the file and assighn it to this varuble
        text_reader = text_file.read()
        
        # create a empty dictionarey where we'll store the dna of the person in this text file
        dna = {}
        # itarate through the top row of the array and assighn the dna name to the key of the dictionary
        for i in range(1, width):
            # big will keep track how long the array find is
            big = 0
            # every time we find a match we'll put the index into the array
            find = []
            # element will make sure the array will stop at one point
            element = -1
            while True:
                # read the text and give me the next elment that matches
                element = text_reader.find(array[0][i], element + 1)
                if element == -1:
                    break
                # add the matched intex to the array
                find.append(element)
                # update the length of the array
                big += 1
            # keep track of how many we have found the varuble is set to 1 cause we're storing off compairing 2 valuse and only adding one at a time
            track = 1
            greatest = 0
            
            # if the array is less then 2 don't bother looping
            if big < 2:
                greatest = big
            else: 
                # loop through the array subtrack one from the other to see how far appart they are on the array
                for j in range(big - 1):
                    diff = find[j + 1] - find[j]
                    
                    # if they are as far as the dna pattern then update the track varuble
                    if diff == len(array[0][i]):
                        track += 1
                    # if track is greater then greatest then update greates    
                    if track >= greatest:
                        greatest = track  
                    # if elemnts are far apart then rest track to 1    
                    if diff != len(array[0][i]):
                        track = 1

            # update the value of this key in the dictionary
            dna.update({array[0][i]: greatest})
      
        # created the varuble that will be printed at the end it will be updated if we find a match
        match = "No match"
        # itarte through the array and dictionary to see if we find a math
        for i in range(1, length):
            counter = 0
            for j in range(1, width):
                # if we found one match we still have to make sure the whole row matches
                if array[i][j] == dna[array[0][j]]:
                    # the counter varuble will keep track of how many dna in this row match
                    counter += 1 
             
            # if all the dna a this row matched then updated the match varuble wich will be printed at the end
            if counter == width - 1:
                match = array[i][0]
                
        print(match)    
        