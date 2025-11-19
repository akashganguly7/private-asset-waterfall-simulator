import numpy as np

def return_capital(capital, total_distribution):
    amount = min(capital, total_distribution)
    remaining = total_distribution - amount
    return amount, remaining

def preferred_return(capital, years, hurdle_rate, remaining):
    pref = capital * ((1 + hurdle_rate) ** years - 1)
    amount = min(pref, remaining)
    remaining -= amount
    return amount, remaining

def gp_catch_up(capital, total_profit, carry, remaining, lp_pref, lp_capital_return):
    lp_total_due = lp_capital_return + lp_pref
    gp_carry_target = carry * total_profit
    
    amount_needed = gp_carry_target
    amount = min(amount_needed, remaining)
    remaining -= amount
    return amount, remaining

def final_split(remaining, lp_share=0.8, gp_share=0.2):
    lp_amount = remaining * lp_share
    gp_amount = remaining * gp_share
    return lp_amount, gp_amount

def irr(cashflows):
    return np.irr(cashflows)
