import openpyxl as xl

print("\nWelcome to NASA-Missions! (An unnofficial project)")
print("Would you like to create a new mission or do you want to load a mission?")
decision = input("Type 0 for new mission or 1 for loading a mission: ")

wb = xl.load_workbook('NASA-Missions.xlsx')


if decision == '0':
    is_planet_moon = input("\nIs it a planet or a moon? (p/m) ")

    if is_planet_moon.lower == 'p':
        planet = {}
        planet['Planet Name'] = input(
            "What is the name of the planet you found? ")
        planet['Mission Name'] = input(
            "What is the name of the mission? (Be creative) ")
        planet['Gravity'] = input(
            "How fast do objects fall? (Rate of Gravity) ")
        planet['Extra Info'] = input("Anything else you want to add? ")

        sheet = wb['Created Missions']

        sheet.cell(2, 1).value = planet['Mission Name']
        sheet.cell(2, 2).value = planet['Planet Name']
        sheet.cell(2, 3).value = planet['Gravity']
        sheet.cell(2, 4).value = planet['']

    if is_planet_moon.lower == 'm':
        moon = {}
        moon['Moon Name'] = input(
            "What is the name of the moon you found? (Be creative) ")
        moon['Mission Name'] = input("What is the name of the mission? ")
        moon['Gravity'] = input("How fast do objects fall? (Rate of Gravity) ")
        moon['Extra Info'] = input("Anything else you want to add? ")


#  Planet should store:
# - gravity
# - distance from earth
# - number of moons
# - fuel
# - graph fuel
# = compare
# create missions to existing planets/moons in solar system
