from statistics import mean
import random




def calculate_total_deviation(rats):
    from statistics import mean
    mean = mean(rats)
    mean1 = (rats[0] + rats[1] + rats[2] + rats[3] + rats[4])/5 
    mean2 = (rats[5] + rats[6] + rats[7] + rats[8] + rats[9])/5 
    mean3 = (rats[10] + rats[11] + rats[12] + rats[13] + rats[14])/5 
    mean4 = (rats[15] + rats[16] + rats[17] + rats[18] + rats[19])/5 
    mean5 = (rats[20] + rats[21] + rats[22] + rats[23])/4
    a = abs(mean - mean1)
    b = abs(mean - mean2)
    c = abs(mean - mean3)
    d = abs(mean - mean4)
    e = abs(mean - mean5)
    total_deviation_rat_list = a + b + c + d + e 
    return total_deviation_rat_list
    

total_deviation = 1000000000

attempts = 0


rats = [145.5,147,148.16667,157.16667,160.33333,164.83333,167.5,167.83333,
        169.33333,170.33333,170.66667,172.16667,179,183.16667,184.5,186.83333,
        187,187.5,188,188.5,189.33333,189.83333,190,191.66667]

total_mean = mean(rats)

lowest_total_deviation = 1000000000
lowest_rat_list = []

while total_deviation > 0.1:
    
    attempts = attempts + 1
    
    
    random.shuffle(rats)

    
    mean1 = (rats[0] + rats[1] + rats[2] + rats[3] + rats[4])/5 
    mean2 = (rats[5] + rats[6] + rats[7] + rats[8] + rats[9])/5 
    mean3 = (rats[10] + rats[11] + rats[12] + rats[13] + rats[14])/5 
    mean4 = (rats[15] + rats[16] + rats[17] + rats[18] + rats[19])/5 
    mean5 = (rats[20] + rats[21] + rats[22] + rats[23])/4
    
    mean_list = [mean1,mean2,mean3,mean4,mean5]
    
    total_deviation = 0
    for mean in mean_list:
        total_deviation += abs(total_mean-mean)
    
    
    if total_deviation < lowest_total_deviation:
        lowest_total_deviation = total_deviation
        lowest_rat_list = list(rats)
    


    
    if attempts%1000000 == 0:
        print("Attempts so far:",attempts)
        print("Lowest total deviation:",lowest_total_deviation)
        print(lowest_rat_list)
        print()

    

print("The total deviation is:",total_deviation)
print(rats)








#total deviation of 0.1263876667
#group 1 = 170.33333, 179, 167.5, 187.5, 167.83333
#group 2 = 184.5, 148.16667, 187, 183.16667, 169.33333
#group 3 = 188, 191.66667, 160.33333, 186.83333, 145.5
#group 4 = 147, 189.83333, 188.5, 157.16667, 189.33333
#group 5 = 164.83333, 172.16667, 190, 170.66667



# group1 = [187.0000, 179.0000, 189.8333, 147.0000, 169.3333]
# group2 = [188.5000, 167.8333, 188.0000, 160.3333, 167.5000]
# group3 = [186.8333, 145.5000, 164.8333, 183.1667, 191.6667]
# group4 = [157.1667, 170.6667, 184.5000, 170.3333, 190.0000]
# group5 = [172.1667, 189.3333, 187.5000, 148.1667]


# deivation = calculate_total_deviation(group1+group2+group3+group4+group5)



# print(deivation)




