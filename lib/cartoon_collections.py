def roll_call_dwarves(names):
    i = 1
    for name in names:
        print(f"{i}. {name}")
        i += 1

def summon_captain_planet(calls):
    return [call.capitalize() + "!" for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in cheeses:
            return snack
    
