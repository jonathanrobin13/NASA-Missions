print("\nWelcome to NASA-Missions! (An unnofficial project)")
print("Would you like to create a new mission or do you want to load a mission?")
decision = input("Type 0 for new mission or 1 for loading a mission: ")


if decision == '0':
    is_planet = input("\nIs it a planet? (y/n) ")

    if is_planet == 'y':
        planet = {}
        planet['Planet_name'] = input(
            "What is the name of the planet you found? ")
        planet['Mission_name'] = input(
            "What is the name of the mission? (Be creative) ")
        planet['Gravity'] = input("How fast do objects fall? (Gravity) ")
        planet['Extra_info'] = input("Anything else you want to put? ")


#  Planet should store:
# - gravity
# - distance from earth
# - number of moons
# - fuel
# - graph fuel
# = compare
# create missions to existing planets/moons in solar system
