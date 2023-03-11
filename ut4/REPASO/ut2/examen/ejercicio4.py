def doubleage (mom: int, daughter: int):
    new_mom = mom - daughter
    new_daughter = 0
    for age in range(mom+1):
        if new_daughter*2 == new_mom:
            return  new_mom,new_daughter
        else: 
            new_mom += 1
            new_daughter += 1
    return None

print(doubleage(24,14))