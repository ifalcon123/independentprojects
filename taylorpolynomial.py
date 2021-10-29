import math


#function that approximates cos using Taylor polynomial in degrees
def cos_approximation_zero_center(x):
    
    degree = 169
    
    #convert x to a degree value greater than or equal 0 and less than 2pi
    x = float(x)
    while x < 0:
        x += 2*math.pi
    while x >= 2*math.pi:
        x -= 2*math.pi
    
    cos = float(0)
    center = float(0)
    
    difference = float(x-center)


    
    for i in range(0,degree+1):
        if i % 2 == 0:
            sign = float((-1)**(i/2))
            factorial = float(math.factorial(i))
            difference = float((x-center)**i)
            cos += (sign*difference)/(factorial)
    
    for i in range(0,degree+3):
        if i % 2 == 0:
            sign = float((-1)**(i/2))
            factorial = float(math.factorial(i))
            difference = float((x-center)**i)
            lagrange_error = (sign*difference)/(factorial)
    
    
    
    cos = round(cos, 7)
    if cos == -0.0:
        cos = 0.0
    
    print("Calculated Value:",cos)
    print("Actual Value:",round(math.cos(x),7))
    print("Error:",round(math.cos(x),7)-cos)
    print("Lagrange Error:",lagrange_error)



