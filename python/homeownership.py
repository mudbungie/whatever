from tkinter import W


ANNUAL_MARKET_RETURN = 1.11
HOME_VALUE_GROWTH = 1.05
HOUSE_PRICE = 405000
DOWN_PAYMENT = .2
RENT = 2100
INTEREST = .0375


def determine_investments_value(starting_principal, years):
    investment_growth_proportion = ANNUAL_MARKET_RETURN ** years
    investments_value = starting_principal * investment_growth_proportion
    return investments_value

def determine_home_value(home_value, years):
    home_value_growth_proportion = HOME_VALUE_GROWTH ** years
    home_value = home_value * home_value_growth_proportion
    return home_value

def determine_home_loan_cost(home_value, interest_rate, down_payment_proportion, years, monthly_payment):
    loan_value = 1 

def determine_investment_outcome(years):
    starting_principal = HOUSE_PRICE * DOWN_PAYMENT
    investments_value = determine_investments_value(starting_principal, years)
    rent = RENT * 12 * years
    net_after_years = investments_value - rent
    return investments_value - rent


def determine_homeownership_outcome(years):
    starting_principal = 0
    investments_value = determine_investments_value(starting_principal, years)
    rent = 0 * years

    

    home_value_growth_proportion = HOME_VALUE_GROWTH ** years


    home_value = HOUSE_PRICE * home_value_growth_proportion
    return home_value

if __name__ == "__main__":
    print(f"The expected value of investments after 0  years is ${determine_investment_outcome(0)}")
    print(f"The expected value of investments after 1  years is ${determine_investment_outcome(1)}")
    print(f"The expected value of investments after 10 years is ${determine_investment_outcome(10)}")
    print(f"The expected value of investments after 20 years is ${determine_investment_outcome(20)}")
    print(f"The expected value of investments after 30 years is ${determine_investment_outcome(30)}")