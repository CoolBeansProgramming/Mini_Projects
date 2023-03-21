

def monthly_interest_earned():
    """
    Calculates the total interest earned per month.
    """
    pass

def update_balance():
    """
    Updates the balance when interest is added and additional deposits are made. 
    """

def savings_goal():
    """
    Outputs a time line of how much needs to be saved monthly to reach a savings goal. 
    """
    pass

def compound_interest(principal: float, interest_rate: float, rate_freq: float, years: float, payments: float):
    """
    Calculates compound interest when only an initial deposit is made and returns the balance.
    https://www.wikihow.com/Calculate-Bank-Interest-on-Savings
    https://www.nerdwallet.com/article/banking/savings-calculator
    https://github.com/tuomaskivioja/5-super-quick-automation-ideas/blob/main/wealth_calculator.py
    
    """
    interest_compound = (interest_rate/100)/rate_freq
    
    accumulated_savings = principal*(1+(interest_compound))**(rate_freq*years)
    
    contributions = payments*((1+interest_compound)**(rate_freq*years)-1)*(1/interest_compound)
    
    total = accumulated_savings + contributions
    
    return total

def deposit_amount():
    """
    Exports deposit amounts into an Excel spreadsheet 
    """
    pass

def main(): 
    initial_deposit, interest_rate, freq, years, deposits = [float(s) for s in input("Enter the initial deposit amount, interest rate, times interest is paid, number of years. and monthly contribution amount: ").split()]

    balance = compound_interest(initial_deposit, interest_rate, freq, years, deposits)
    
    print(f"In {int(years)} years, your balance will be ${balance: .2f}.")
    



main()