import random 
from statistics import mean
from statistics import stdev as std
import math

def simulation(total,chance1,chance2):
    
    count = 0
    turns_sum = []
    
    while count < total:
        count += 1
        deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
                27,28, 29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,
                50,51,52]
        number = 0

        random.shuffle(deck)


        player1 = []
        player2 = []

        incorrect_guesses = []

        player1.append(deck[0])
        player1.append(deck[1])
        player1.append(deck[2])
        player1.append(deck[3])
        player1.append(deck[4])
        player1.append(deck[5])
        player1.append(deck[6])
        player1.append(deck[7])
        player1.append(deck[8])
        player1.append(deck[9])


        player2.append(deck[10])
        player2.append(deck[11])
        player2.append(deck[12])
        player2.append(deck[13])
        player2.append(deck[14])
        player2.append(deck[15])
        player2.append(deck[16])
        player2.append(deck[17])
        player2.append(deck[18])
        player2.append(deck[19])

        possibilities = deck[0:10] + deck[20:52]

        random.shuffle(possibilities)

        random.shuffle(player1)

        player1_sort = player1[1:10]

        player1_sort.sort()

        a = 0

        c = 19

        e = 0
        
        turns = 0
    
        while a == 0:
            if a == 0:
                turns += 1
                c = c + 1
                if c < 52:
                    player1_sort.append(deck[c])
                number = random.uniform(0,100)
                if number <= chance1:
                    if possibilities[0] == player1[0]:
                        a = 1
                    elif player1_sort.count(possibilities[0]) == 0:
                        incorrect_guesses.append(possibilities[0])
                        possibilities.pop(0)
                        c = c + 1
                        if c < 52:
                            player2.append(deck[c])
                            if possibilities.count(deck[c]) > 0:
                                g = possibilities.index(deck[c])
                                possibilities.pop(g)
                    else: 
                        c = c + 1
                        if c < 52:
                            player2.append(deck[c])
                            if possibilities.count(deck[c]) > 0:
                                g = possibilities.index(deck[c])
                                possibilities.pop(g)
                        player2.append(possibilities[0])
                        possibilities.pop(0)
                elif chance1 < number <= chance2 or incorrect_guesses == []:
                    while e == 0:
                        player2_sort = player2
                        random.shuffle(player2_sort)
                        f = player2_sort[0]
                        if player1_sort.count(f) > 0:
                            e = 0
                        else:
                            e = 1
                            c = c + 1
                            if c < 52:
                                player2.append(deck[c])
                                if possibilities.count(deck[c]) > 0:
                                    g = possibilities.index(deck[c])
                                    possibilities.pop(g)
                else:
                    random.shuffle(incorrect_guesses)
                    if incorrect_guesses[0] == player1[0]:
                        a = 1
                    elif player1_sort.count(incorrect_guesses[0]) == 0:
                        c = c + 1
                        if c < 52:
                           player2.append(deck[c])
                           if possibilities.count(deck[c]) > 0:
                               g = possibilities.index(deck[c])
                               possibilities.pop(g)
                    else:
                        c = c + 1
                        if c < 52:
                            player2.append(deck[c])
                            if possibilities.count(deck[c]) > 0:
                                g = possibilities.index(deck[c])
                                possibilities.pop(g)
                        player2.append(incorrect_guesses[0])
                        incorrect_guesses.pop(0)
        turns_sum += [turns]
    return [sum(turns_sum)/ len(turns_sum), std(turns_sum)]

chance1 = 80
chance2 = 20
    
simulation_data= simulation(10000,chance1,chance2)
print()
print("Average turns for computer to win with these conditions:",simulation_data[0])
# print("Std:",simulation_data[1])
# print("Standard Error:", simulation_data[1]/ math.sqrt(10000))
    

deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
        27,28, 29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,
        50,51,52]


random.shuffle(deck)

round_number = 0

player1 = []
player2 = []

incorrect_guesses = []

player1.append(deck[0])
player1.append(deck[1])
player1.append(deck[2])
player1.append(deck[3])
player1.append(deck[4])
player1.append(deck[5])
player1.append(deck[6])
player1.append(deck[7])
player1.append(deck[8])
player1.append(deck[9])


player2.append(deck[10])
player2.append(deck[11])
player2.append(deck[12])
player2.append(deck[13])
player2.append(deck[14])
player2.append(deck[15])
player2.append(deck[16])
player2.append(deck[17])
player2.append(deck[18])
player2.append(deck[19])

possibilities = deck[0:10] + deck[20:52]

random.shuffle(possibilities)

random.shuffle(player1)

player1_sort = player1[1:10]

player1_sort.sort()

print("\nInstructions: You and your opponent each have a thief. Your goal is to guess your opponents thief. To help you, you each start with 9 witnesses. The witnesses help you guess the thief because you know that they aren\'t your opponent\'s thief. If you guess one of your opponents witnesses, it will be added to your list of witnesses. Each round, regardless of what happens, you and your opponent will both receive one witness from the deck until there are none left in the deck. The numbers that you can guess are 1-52. Enter 0 to end game. Good luck!!\n")


print("Your thief is",player1[0],"and your witnesses are",player1_sort)
print()

a = 0

c = 19

e = 0

turns = 0


#player's turn


while a == 0:
    round_number += 1
    e = 0
    print("Round",round_number)
    b = int(input("Your guess:"))
    if b == player2[0]:
        print("\n You won the game!!")
        a = 1
    elif player2.count(b) > 0 and b != player2[0] and player1_sort.count(b) < 1 and b != player1[0]:
        print("\n You guessed",b,", one of your opponents witnesses!!!")
        player1_sort.append(b)
        c = c + 1
        if c < 52:
            player1_sort.append(deck[c])
            print("\n Your new witness is",deck[c],".")
        player1_sort.sort()
        print("\n Your thief is",player1[0],"and your witnesses are",player1_sort)
    elif player2.count(b) == 0 and player1.count(b) == 0 and deck.count(b) > 0:
        print("\n You guessed",b,"incorrectly.")
        c = c + 1
        if c < 52:
            player1_sort.append(deck[c])
            print("\n Your new witness is",deck[c],".")
        player1_sort.sort()
        print("\n Your thief is",player1[0],"and your witnesses are",player1_sort)
    elif player1_sort.count(b) > 0 or b == player1[0]:
        print("\n You guessed one of your own witnesses.")
        c = c + 1
        if c < 52:
            player1_sort.append(deck[c])
            print("\n Your new witness is",deck[c],".")
        player1_sort.sort()
        print("\n Your thief is",player1[0],"and your witnesses are",player1_sort)  
    elif b == 0:
        a = 1
        print()
        print("Game ended")
    else:
        print("\n You did not guess an integer between 1 and 52.")
        c = c + 1
        if c < 52:
            player1_sort.append(deck[c])
            print("\n Your new witness is",deck[c],".")
        player1_sort.sort()
        print("\n Your thief is",player1[0],"and your witnesses are",player1_sort)  
       
#computer's turn
        
    if a == 0:
        number = random.uniform(0,100)
        if number <= chance1:
            if possibilities[0] == player1[0]:
                print("\n Your opponent guessed your thief. You lose. Your opponent's thief was",player2[0],".")
                a = 1
            elif player1_sort.count(possibilities[0]) == 0:
                print("\n Your opponent guessed",possibilities[0],"incorrectly. \n")
                print()
                incorrect_guesses.append(possibilities[0])
                possibilities.pop(0)
                c = c + 1
                if c < 52:
                    player2.append(deck[c])
                    if possibilities.count(deck[c]) > 0:
                        g = possibilities.index(deck[c])
                        possibilities.pop(g)
            else: 
                print("\n Your opponent guessed",possibilities[0],"correctly. \n")
                print()
                c = c + 1
                if c < 52:
                    player2.append(deck[c])
                    if possibilities.count(deck[c]) > 0:
                        g = possibilities.index(deck[c])
                        possibilities.pop(g)
                player2.append(possibilities[0])
                possibilities.pop(0)
        elif chance1 < number <= chance2 or incorrect_guesses == []:
            while e == 0:
                player2_sort = player2
                random.shuffle(player2_sort)
                f = player2_sort[0]
                if player1_sort.count(f) > 0:
                    e = 0
                else:
                    e = 1
                    c = c + 1
                    if c < 52:
                        player2.append(deck[c])
                        if possibilities.count(deck[c]) > 0:
                            g = possibilities.index(deck[c])
                            possibilities.pop(g)
                    print("\n Your opponent guessed",f,"incorrectly. \n")
        else:
            random.shuffle(incorrect_guesses)
            if incorrect_guesses[0] == player1[0]:
                print("\n Your opponent guessed your thief. You lose. Your opponent's thief was",player2[0],".")
                print()
                a = 1
            elif player1_sort.count(incorrect_guesses[0]) == 0:
                print("\n Your opponent guessed",incorrect_guesses[0],"incorrectly. \n")
                print()
                c = c + 1
                if c < 52:
                    player2.append(deck[c])
                    if possibilities.count(deck[c]) > 0:
                        g = possibilities.index(deck[c])
                        possibilities.pop(g)
            else:
                c = c + 1
                if c < 52:
                    player2.append(deck[c])
                    if possibilities.count(deck[c]) > 0:
                        g = possibilities.index(deck[c])
                        possibilities.pop(g)
                print("\n Your opponent guessed",incorrect_guesses[0],"correctly. \n")
                print()
                player2.append(incorrect_guesses[0])
                incorrect_guesses.pop(0)








  
                
                
                
                
