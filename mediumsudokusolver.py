import pandas as pd
from csv import writer

def square_list(start,puzzle_list):
    list1 = []
    list1 += puzzle_list[start:start+3] + puzzle_list[start+9:start+12] + puzzle_list[start+18:start+21]
    return list1

def check_last_number(puzzle_list):
    numbers_in_list = 0
    column1 = puzzle_list[0:9]
    column2 = puzzle_list[9:18]
    column3 = puzzle_list[18:27]
    column4 = puzzle_list[27:36]
    column5 = puzzle_list[36:45]
    column6 = puzzle_list[45:54]
    column7 = puzzle_list[54:63]
    column8 = puzzle_list[63:72]
    column9 = puzzle_list[72:81]
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    index = 0
    for i in puzzle_list:
        if index % 9 == 0:
            row1 += [i]
        elif index % 9 == 1:
            row2 += [i]
        elif index % 9 == 2:
            row3 += [i]
        elif index % 9 == 3:
            row4 += [i]
        elif index % 9 == 4:
            row5 += [i]
        elif index % 9 == 5:
            row6 += [i]
        elif index % 9 == 6:
            row7 += [i]
        elif index % 9 == 7:
            row8 += [i]
        elif index % 9 == 8:
            row9 += [i]
        index += 1
        square1 = puzzle_list[0:3] + puzzle_list[9:12] + puzzle_list[18:21]
        square2 = puzzle_list[3:6] + puzzle_list[12:15] + puzzle_list[21:24]
        square3 = puzzle_list[6:9] + puzzle_list[15:18] + puzzle_list[24:27]
        square4 = puzzle_list[27:30] + puzzle_list[36:39] + puzzle_list[45:48]
        square5 = puzzle_list[30:33] + puzzle_list[39:42] + puzzle_list[48:51]
        square6 = puzzle_list[33:36] + puzzle_list[42:45] + puzzle_list[51:54]
        square7 = puzzle_list[54:57] + puzzle_list[63:66] + puzzle_list[72:75]
        square8 = puzzle_list[57:60] + puzzle_list[66:69] + puzzle_list[75:78]
        square9 = puzzle_list[60:63] + puzzle_list[69:72] + puzzle_list[78:81]

    
    row_list= [row1,row2,row3,row4,row5,row6,row7,row8,row9]
    column_list = [column1,column2,column3,column4,column5,column6,column7,column8,column9]
    square_list = [square1,square2,square3,square4,square5,square6,square7,square8,square9]
    for i in row_list:
        numbers_in_list = 0
        for j in i:
            if type(j) == int:
                numbers_in_list += 1
        if numbers_in_list == 8:
            for k in range(1,10):
                if i.count(k) == 0:
                    for z in range (0,9):
                        if type(z)!= int:
                            i[z] = k
                            puzzle_list_index = row_list.index(i) + i.index(k)*9
                            puzzle_list[puzzle_list_index] = k

                
    for i in column_list:
        numbers_in_list = 0
        for j in i:
            if type(j) == int:
                numbers_in_list += 1
        if numbers_in_list == 8:
            for k in range(1,10):
                if i.count(k) == 0:
                    for z in range (0,9):
                        if type(z) != int:
                            i[z] = k
                            puzzle_list_index = column_list.index(i)*9 + i.index(k)
                            puzzle_list[puzzle_list_index] = k

                

    square_add_list = [0,1,2,9,10,11,18,19,20]    
    square_start_list = [0,3,6,27,30,33,54,57,60]            
    for i in square_list:
        numbers_in_list = 0
        for j in i:
            if type(j) == int:
                numbers_in_list += 1
        if numbers_in_list == 8:
            for k in range(1,10):
                if i.count(k) == 0:
                    for z in range (0,9):
                        if type(z) != int:
                            i[z] = k
                            puzzle_list_index = square_start_list[square_list.index(i)] + square_add_list[i.index(k)]
                            puzzle_list[puzzle_list_index] = k
    return puzzle_list


def create_possibilities_list(puzzle_list):
    possibilities = []
    total = [1,2,3,4,5,6,7,8,9]
    for i in range (0,81):
        if puzzle_list[i] == '':
            possibilities.append(total)
        else:
            possibilities.append(puzzle_list[i])
            
    return possibilities


def check_possibilities(possibilities):
    index = 0
    templist = []
    for i in possibilities:
        row_list = []
        column_list = []
        square_list = []
        if type(i) == list:
            row_index = int((index - ((index//9)*9)))
            column_index = int(index // 9)
            if column_index < 3:
                square_index = row_index // 3
            elif column_index < 6:
                square_index = 3 + (row_index // 3)
            elif column_index < 9:
                square_index = 6 + (row_index // 3)
            column_list = possibilities[column_index*9:(column_index*9)+9]
            j_index = 0
            for j in possibilities:
                if j_index % 9 == row_index and type(j) == int:
                    row_list += [j]
                j_index += 1
            start = int(((column_index // 3)*27) + ((row_index // 3)*3))
            square_list += possibilities[start:start+3] + possibilities[start+9:start+12] + possibilities[start+18:start+21]
            for iteration in range (1,10):
                for k in square_list:
                    if type(k) == list:
                        square_list.remove(k)
            for iteration in range (1,10):
                for k in column_list:
                    if type(k) == list:
                        column_list.remove(k)
            templist = []
            for x in possibilities[index]:
                templist += [x]
            for a in row_list:
                if templist.count(a) >0:
                    templist.remove(a)
            for a in column_list:
                if templist.count(a) >0:
                    templist.remove(a)
            for a in square_list:
                if templist.count(a) >0:
                    templist.remove(a)
            possibilities.pop(index)
            if len(templist) == 1:
                possibilities.insert(index,templist[0])
            else:
                possibilities.insert(index,templist)
        index += 1
    return possibilities
    


def update_puzzle_list(possibilities,puzzle_list):
    index = 0
    for i in possibilities:
        if type(i) == int and i != puzzle_list[index]:
            puzzle_list[index] = i
        index += 1
    return puzzle_list


def check_for_restrictions(possibilities):
    column1 = possibilities[0:9]
    column2 = possibilities[9:18]
    column3 = possibilities[18:27]
    column4 = possibilities[27:36]
    column5 = possibilities[36:45]
    column6 = possibilities[45:54]
    column7 = possibilities[54:63]
    column8 = possibilities[63:72]
    column9 = possibilities[72:81]
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    index = 0
    for i in possibilities:
        if index % 9 == 0:
            row1 += [i]
        elif index % 9 == 1:
            row2 += [i]
        elif index % 9 == 2:
            row3 += [i]
        elif index % 9 == 3:
            row4 += [i]
        elif index % 9 == 4:
            row5 += [i]
        elif index % 9 == 5:
            row6 += [i]
        elif index % 9 == 6:
            row7 += [i]
        elif index % 9 == 7:
            row8 += [i]
        elif index % 9 == 8:
            row9 += [i]
        index += 1
    square1 = possibilities[0:3] + possibilities[9:12] + possibilities[18:21]
    square2 = possibilities[3:6] + possibilities[12:15] + possibilities[21:24]
    square3 = possibilities[6:9] + possibilities[15:18] + possibilities[24:27]
    square4 = possibilities[27:30] + possibilities[36:39] + possibilities[45:48]
    square5 = possibilities[30:33] + possibilities[39:42] + possibilities[48:51]
    square6 = possibilities[33:36] + possibilities[42:45] + possibilities[51:54]
    square7 = possibilities[54:57] + possibilities[63:66] + possibilities[72:75]
    square8 = possibilities[57:60] + possibilities[66:69] + possibilities[75:78]
    square9 = possibilities[60:63] + possibilities[69:72] + possibilities[78:81]
    
    row_list= [row1,row2,row3,row4,row5,row6,row7,row8,row9]
    column_list = [column1,column2,column3,column4,column5,column6,column7,column8,column9]
    square_list = [square1,square2,square3,square4,square5,square6,square7,square8,square9]
    

    row_list_index = 0
    for row in row_list:
        box_index = 0
        for box in row:
            index_list = []
            index_list.append(box_index)
            for k in range (0,9):
                if k != box_index:
                    if box == row[k]:
                        index_list.append(k)
            if type(box) == list and len(index_list) == len(box):
                other_box_index = 0
                for other_box in row:
                    if index_list.count(other_box_index) == 0 and type(other_box) == list:
                        for possibility in box:
                            if other_box.count(possibility) > 0:
                                possibilities_index = row_list_index + ((other_box_index)*9)
                                templist = []
                                for x in other_box:
                                    templist += [x]
                                possibilities.pop(possibilities_index)
                                templist.remove(possibility)
                                possibilities.insert(possibilities_index,templist)
                                
                    other_box_index += 1
            box_index += 1
        row_list_index += 1

         
    column_list_index = 0
    for column in column_list:
        box_index = 0
        for box in column:
            index_list = []
            index_list.append(box_index)
            for k in range (0,9):
                if k != box_index:
                    if box == column[k]:
                        index_list.append(k)
            if type(box) == list and len(index_list) == len(box):
                other_box_index = 0
                for other_box in column:
                    if index_list.count(other_box_index) == 0 and type(other_box) == list:
                        for possibility in box:
                            if other_box.count(possibility) > 0:
                                possibilities_index = ((column_list_index)*9) + (other_box_index)
                                templist = []
                                for x in other_box:
                                    templist += [x]
                                possibilities.pop(possibilities_index)
                                templist.remove(possibility)
                                possibilities.insert(possibilities_index,templist)
                            
                    other_box_index += 1
            box_index += 1
        column_list_index += 1

                
    square_list_index = 0
    for square in square_list:
        box_index = 0
        for box in square:
            index_list = []
            index_list.append(box_index)
            for k in range (0,9):
                if k != box_index:
                    if box == square[k]:
                        index_list.append(k)
            if type(box) == list and len(index_list) == len(box):
                other_box_index = 0
                for other_box in square:
                    if index_list.count(other_box_index) == 0 and type(other_box) == list:
                        for possibility in box:
                            if other_box.count(possibility) > 0:
                                possibilities_index = ((square_list_index // 3)*27) + ((other_box_index//3)*9) + ((square_list_index %3)*3) + ((other_box_index % 3))
                                templist = []
                                for x in other_box:
                                    templist += [x]
                                possibilities.pop(possibilities_index)
                                templist.remove(possibility)
                                possibilities.insert(possibilities_index,templist)
                                other_box = templist
                    other_box_index += 1
            box_index += 1
        square_list_index += 1



           
    return possibilities




csv_file = 'mediumpuzzle.csv'
       


puzzle = pd.read_csv(csv_file)
df = pd.DataFrame(list())
df.to_csv(csv_file)



puzzle_list = []

for column in puzzle:
    if str(column) == '1' or str(column) == '2' or str(column) == '3' or str(column) == '4' or str(column) == '5' or str(column) == '6' or str(column) == '7' or str(column) == '8' or str(column) == '9':
        puzzle_list += [int(column)]
    else:
        puzzle_list += ['']
    for i in range (0,8):
        if puzzle[column][i] == 1 or puzzle[column][i] == 2 or puzzle[column][i] == 3 or puzzle[column][i] == 4 or puzzle[column][i] == 5 or puzzle[column][i] == 6 or puzzle[column][i] == 7 or puzzle[column][i] == 8 or puzzle[column][i] == 9:
            puzzle_list += [int(puzzle[column][i])]
        else:
            puzzle_list += ['']


    







puzzle_complete = False
attempts = 0

possibilities = create_possibilities_list(puzzle_list)

while puzzle_complete == False:
    puzzle_list = check_last_number(puzzle_list)
    possibilities = check_possibilities(possibilities)
    puzzle_list = update_puzzle_list(possibilities,puzzle_list)
    possibilities = check_for_restrictions(possibilities)
    attempts += 1

    
    unsolved_boxes = 0
    for i in puzzle_list:
        if type(i) != int:
            unsolved_boxes += 1                                  
    if attempts == 1000 or unsolved_boxes == 0:
        puzzle_complete = True
                    
    




row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []
row7 = []
row8 = []
row9 = []
index = 0
for i in puzzle_list:
    if index % 9 == 0:
        row1 += [i]
    elif index % 9 == 1:
        row2 += [i]
    elif index % 9 == 2:
        row3 += [i]
    elif index % 9 == 3:
        row4 += [i]
    elif index % 9 == 4:
        row5 += [i]
    elif index % 9 == 5:
        row6 += [i]
    elif index % 9 == 6:
        row7 += [i]
    elif index % 9 == 7:
        row8 += [i]
    elif index % 9 == 8:
        row9 += [i]
    index += 1

    
    
row_list= [row1,row2,row3,row4,row5,row6,row7,row8,row9]
for i in row_list: 
    with open(csv_file, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(i)   
    
    
    
    
    
    
    
    
    
    
        
