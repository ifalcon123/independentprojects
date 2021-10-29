from scipy.stats import norm
import math
from scipy import stats

type = input("Type 'm' for a mean hypothesis test and 'p' for proportion:")


if type == 'm':
    sample_count = int(input("Type '1' for 1 sample and '2' for 2 samples:"))
    if sample_count == 1:
        mu = float(input("Ho="))
        curve = int(input("Type 0 for z test or 1 for t test:"))
        if curve == 0:
            n = int(input("Sample size: n="))
            mean = float(input("Sample mean:"))
            standard_deviation = float(input("Standard deviation:"))
            direction = input("For alternative hypothesis: Type 'g' for greater than, 'l' for less than, or 'n' for not equal to:")
            alpha = float(input("Alpha value="))
            standard_error = standard_deviation/(math.sqrt(n))
            z = (mean-mu)/standard_error
            if direction == 'g':
                p_value = norm.cdf(z)
                p_value = 1 - p_value
            elif direction == 'l':
                p_value = norm.cdf(z)
            elif direction == 'n':
                p_value = norm.cdf(abs(z)*-1)*2
            if p_value <= alpha:
                print("P-value =",p_value)
                print("Reject the null hypothesis.")
            else:
                print("P-value =",p_value)
                print("Fail to reject the null hypothesis.")
        if curve == 1:
            df = int(input("df="))
            mean = float(input("Sample mean:"))
            standard_deviation = float(input("Standard deviation:"))
            direction = input("For alternative hypothesis: Type 'g' for greater than, 'l' for less than, or 'n' for not equal to:")
            alpha = float(input("Alpha value="))
            standard_error = standard_deviation/(math.sqrt(df+1))
            t = (mean-mu)/standard_error
            if direction == 'g':
                p_value = stats.t.sf(t, df)
            elif direction == 'l':
                p_value = stats.t.sf(t, df)   
                p_value = 1 - p_value
            elif direction == 'n':
                p_value = stats.t.sf(abs(t), df)*2            
            if p_value <= alpha:
                print("P-value =",p_value)
                print("Reject the null hypothesis.")
            else:
                print("P-value =",p_value)
                print("Fail to reject the null hypothesis.")
    elif sample_count == 2:
        curve = int(input("Type 0 for z test or 1 for t test:"))
        if curve == 0:
            n1 = int(input("Sample size 1: n1="))
            n2 = int(input("Sample size 2: n2="))
            mean1 = float(input("Sample mean 1:"))
            mean2 = float(input("Sample mean 2:"))
            standard_deviation1 = float(input("Standard deviation 1:"))
            standard_deviation2 = float(input("Standard deviation 2:"))
            direction = input("For alternative hypothesis: Mu 1 - Mu 2 ?? 0: Type 'g' for greater than, 'l' for less than, or 'n' for not equal to:")
            alpha = float(input("Alpha value="))
            standard_error = math.sqrt(((standard_deviation1)**2)/n1 + ((standard_deviation2)**2)/n2)
            z = (mean1-mean2)/standard_error
            if direction == 'g':
                p_value = norm.cdf(z)
                p_value = 1 - p_value
            elif direction == 'l':
                p_value = norm.cdf(z)
            elif direction == 'n':
                p_value = norm.cdf(abs(z)*-1)*2
            if p_value <= alpha:
                print("P-value =",p_value)
                print("Reject the null hypothesis.")
            else:
                print("P-value =",p_value)
                print("Fail to reject the null hypothesis.")
        if curve == 1:
            df1 = int(input("Degrees of freedom 1: df1="))
            df2 = int(input("Degrees of freedom 2: df2="))
            df_list = [df1,df2]
            df = min(df_list)
            mean1 = float(input("Sample mean 1:"))
            mean2 = float(input("Sample mean 2:"))
            standard_deviation1 = float(input("Standard deviation 1:"))
            standard_deviation2 = float(input("Standard deviation 2:"))
            direction = input("For alternative hypothesis: Mu 1 - Mu 2 ?? 0: Type 'g' for greater than, 'l' for less than, or 'n' for not equal to:")
            alpha = float(input("Alpha value="))
            standard_error = math.sqrt(((standard_deviation1)**2)/(df1 + 1) + ((standard_deviation2)**2)/(df2 + 1))
            t = (mean1-mean2)/standard_error
            if direction == 'g':
                p_value = stats.t.sf(t, df)
            elif direction == 'l':
                p_value = stats.t.sf(t, df)
                p_value = 1 - p_value
            elif direction == 'n':
                p_value = stats.t.sf(abs(t), df)*2
            if p_value <= alpha:
                print("P-value =",p_value)
                print("Reject the null hypothesis.")
            else:
                print("P-value =",p_value)
                print("Fail to reject the null hypothesis.")

if type == 'p':
    sample_count = int(input("Type '1' for 1 sample and '2' for 2 samples:"))
    if sample_count == 1:
        p = float(input("Ho="))
        n = int(input("Sample size: n="))
        p_hat = float(input("Sample proportion:"))
        direction = input("For alternative hypothesis: Type 'g' for greater than, 'l' for less than, or 'n' for not equal to:")
        alpha = float(input("Alpha value="))
        standard_deviation = math.sqrt((p)(1-p)/n)
        z = (p_hat - p)/standard_deviation
        if direction == 'g':
            p_value = norm.cdf(z)
        elif direction == 'l':
            p_value = norm.cdf(z)
            p_value = 1 - p_value
        elif direction == 'n':
            p_value = norm.cdf(abs(z)*-1)*2
        if p_value <= alpha:
            print("P-value =",p_value)
            print("Reject the null hypothesis.")
        else:
            print("P-value =",p_value)
            print("Fail to reject the null hypothesis.")
    elif sample_count == 2:
        n1 = int(input("Sample size 1: n1="))
        n2 = int(input("Sample size 2: n2="))
        p_hat1 = float(input("Sample proportion 1:"))
        p_hat2 = float(input("Sample proportion 2:"))
        direction = input("For alternative hypothesis: p1 - p2 ?? 0: Type 'g' for greater than, 'l' for less than, or 'n' for not equal to:")
        alpha = float(input("Alpha value="))
        total_success = (p_hat1)*n1 + (p_hat2)*n2
        total_n = n1 + n2
        pc = total_success/total_n
        inverse_pc = 1 - pc
        second = ((1/n1)+(1/n2))
        first = pc * inverse_pc
        standard_deviation = math.sqrt(first * second)
        z = (p_hat1 - p_hat2)/standard_deviation
        if direction == 'g':
            p_value = norm.cdf(z)
        elif direction == 'l':
            p_value = norm.cdf(z)
            p_value = 1 - p_value
        elif direction == 'n':
            p_value = norm.cdf(abs(z)*-1)*2
        if p_value <= alpha:
            print("P-value =",p_value)
            print("Reject the null hypothesis.")
        else:
            print("P-value =",p_value)
            print("Fail to reject the null hypothesis.")
            
            
            
            

