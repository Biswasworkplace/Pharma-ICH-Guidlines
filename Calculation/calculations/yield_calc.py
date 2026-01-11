def calculate_yield(actual_yield, theoretical_yield):
    if theoretical_yield == 0:
        raise ValueError("Theoretical yield cannot be zero")
    return (actual_yield / theoretical_yield) * 100
