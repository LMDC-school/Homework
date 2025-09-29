#Part I
def dream_house_1():
    total_cost=float(input("Enter the price of the house you chose:"))    #User inputs
    annual_salary=float(input("Enter your starting annual salary:"))
    portion_saved=float(input("Enter the portion of your salary you choose to save (in decimal form):"))
    portion_down_payment=0.25    #Given variables
    down_payment=total_cost*portion_down_payment
    current_savings=0.0
    r=0.04
    number_of_months=0    #Output variable
    while current_savings<=down_payment:     #Start of the loop
        number_of_months+=1     #Every iteration of the loop represents one month
        current_savings+=current_savings*(r/12)
        current_savings+=portion_saved*(annual_salary/12)
    return f'Number of months :{number_of_months}'

#Part II
def dream_house_2():
    total_cost=float(input("Enter the price of the house you chose:"))    #User inputs
    annual_salary=float(input("Enter your starting annual salary:"))
    portion_saved=float(input("Enter the portion of your salary you choose to save (in decimal form):"))   
    semi_annual_raise=float(input("Enter the percentage of your semi-annual raise (in decimal form):"))
    portion_down_payment=0.25    #Given variables
    down_payment=total_cost*portion_down_payment
    current_savings=0.0
    r=0.04
    number_of_months=0    #Output variable
    while current_savings<=down_payment:     #Start of the loop
        number_of_months+=1     #Every iteration of the loop represents one month
        if number_of_months%6==0:
            annual_salary+=annual_salary*semi_annual_raise
        current_savings+=current_savings*(r/12)
        current_savings+=portion_saved*(annual_salary/12)
    return f'Number of months :{number_of_months}'

#Part III

def dream_house_3():
    annual_salary=float(input("Enter your starting annual salary:"))    #User inputs
    portion_down_payment=0.25    #Given variables
    total_cost=1000000
    r=0.04
    semi_annual_raise=0.07
    number_of_months=36
    down_payment=total_cost*portion_down_payment
    best_rate=0.0    #Output variable
    steps_in_bisection=0
    low_bound=0
    high_bound=10000
    def savings_36_months(annual_salary,savings_rate):
        current_savings=0.0
        for month in range(1, number_of_months + 1):
            if month%6==0:
                annual_salary+=annual_salary*semi_annual_raise
            current_savings+=current_savings*(r/12)
            current_savings+=(annual_salary/12)*(savings_rate/10000)
        return current_savings
    maximum_savings=savings_36_months(annual_salary,10000)
    if maximum_savings<down_payment-100:
        return "It is not possible to pay the down payment in three years."
    else:
        while (high_bound-low_bound)>1:
            middle=(low_bound+high_bound)/2
            steps_in_bisection+=1
            current_savings=savings_36_months(annual_salary,middle)
            if abs(current_savings-down_payment)<=100:
                best_rate=middle/10000
                break
            elif down_payment>current_savings:
                low_bound=middle
            else:
                high_bound=middle
        return f"Best savings rate : {best_rate}, Steps in bijection search: {steps_in_bisection}"
    


if __name__ == "__main__":
    print(dream_house_3())
        