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
