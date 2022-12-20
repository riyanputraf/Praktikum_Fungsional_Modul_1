heroes = [
    {
        "Hero": "Kagura",
        "Role": "Mage",
        "DMG": 350,
        "Gold": 1000
    },
    {
        "Hero": "Yve",
        "Role": "Mage",
        "DMG": 250,
        "Gold": 1000
    },
    {
        "Hero": "Lancelot",
        "Role": "Assassin",
        "DMG": 200,
        "Gold": 1000
    },
    {
        "Hero": "Hayabusa",
        "Role": "Assassin",
        "DMG": 300,
        "Gold": 1000
    },
    {
        "Hero": "Natalia",
        "Role": "Assassin",
        "DMG": 150,
        "Gold": 1000
    },
    {
        "Hero": "Cecilion",
        "Role": "Mage",
        "DMG": 200,
        "Gold": 1000}
]

sihir = [
    {
        "Name": "Necklace of Durance",
        "DMG": 50,
        "Price": 250
    },
    {
        "Name": "Lightning Truncheon",
        "DMG": 100,
        "Price": 300
    },
    {
        "Name": "Blood Wings",
        "DMG": 300,
        "Price": 500
    }
]

serangan = [
    {
        "Name": "War Axe", "DMG": 100, "Price": 250
    },
    {
        "Name": "Endless Battle", "DMG": 300, "Price": 400
    },
    {
        "Name": "Blade of Despair", "DMG": 400, "Price": 700
    }
]

mantra = [
    {
        "Name": "Execute", "DMG": 300
    },
    {
        "Name": "Flameshot", "DMG": 200
    }
]


def print_for(function, iterator, sequence):
    # variable init
    length = len(sequence)
    index = [i for i in range(length)]
    list_map = list(map(function, index, sequence))

    if iterator == length:  # base case
        return
    else:  # recursive iteration
        print(list_map[iterator])
        return print_for(function, iterator + 1, sequence)


def print_format(string, *args):
    # print(string.format(*args))
    return string.format(*args)


def pilihHero(hero):
    selectedHero = {}

    print("Select 1 Hero you want to play: ")
    print_for(lambda x, y: f"Id : {x} \nDetail : {y}", 0, hero)

    inputs = int(input("silahkan masukkan pilihan Id: "))
    try:
        selectedHero.update(hero[inputs])
        return selectedHero
    except Exception as err:
        raise Exception(err)


def pilihMantra(hero, mantra):
    selectedHero = hero
    hero_name = selectedHero['Hero']
    hero_dmg = selectedHero['DMG']

    print(print_format("\n{} - DMG {}\n", hero_name, hero_dmg))
    print_for(lambda x, y: f"Id: {x} : {y['Name']} - DMG {y['DMG']}", 0, mantra)

    inputs = int(input("Pilih Id spell yang akan dipakai? "))
    try:
        selectedHero["Spell"] = mantra[inputs]
        hero_spell = selectedHero['Spell']
        print(print_format("\n{} - DMG {} - Spell {}\n", hero_name, hero_dmg, hero_spell))
        return selectedHero
    except Exception as err:
        raise Exception(err)


def beli_item(hero):
    selectedHero = hero
    hero_name = selectedHero["Hero"]
    hero_dmg = selectedHero["DMG"]
    hero_gold = selectedHero["Gold"]
    hero_role = selectedHero["Role"]

    print(print_format("\n{} - DMG {} - Gold {}\n", hero_name, hero_dmg, hero_gold))

    def buy_category_item(hero, category_item):
        print_for(lambda x, y: f"Id: {x} : {y['Name']} - DMG {y['DMG']} - Price {y['Price']}", 0, category_item)

        inputs = int(input("silahkan masukkan pilihan Id: "))
        try:
            if hero["Gold"] < category_item[inputs]["Price"]:
                print("Gold not enough")
                return hero
            else:
                hero["DMG"] += category_item[inputs]["DMG"]
                hero["Gold"] -= category_item[inputs]["Price"]
                print("\nBUYING SUCCESS")
                print(print_format("\n{} - DMG {} - Gold {}\n", hero['Hero'], hero['DMG'], hero['Gold']))
        except Exception as err:
            raise Exception(err)

        if hero["Gold"] < 250:
            return hero
        else:
            inputs = input("Ingin beli lagi?(y/n)")
            if inputs.lower() == "y":
                beli_item(hero)
                return hero
            else:
                return hero

    if hero_role == "Mage":
        return buy_category_item(hero, sihir)
    elif hero_role == "Assassin":
        return buy_category_item(hero, serangan)


def bertarung(hero):
    lord = 1000
    selectedHero = hero
    hero_name = selectedHero["Hero"]
    hero_dmg = selectedHero["DMG"]
    hero_spell = selectedHero["Spell"]

    print("Fight Begin\n")
    print(print_format("\nLord - HP: {}\n", lord))
    while lord > 0:
        print(print_format("0 || {} - DMG {}", hero_name, hero_dmg))
        print(print_format("1 || {} - DMG {}", hero_spell["Name"], hero_spell["DMG"]))

        fight = input("Select 0 to fight with hero DMG or 1 to fight with Spell DMG: ")
        if fight == "0":
            lord -= hero_dmg
        elif fight == "1":
            lord -= hero_spell["DMG"]
        else:
            print("Wrong Input!")

        if lord > 0:
            print("\nLord - HP: {}\n".format(lord))
        else:
            lord = 0
            print("\nLord - HP: {}\n".format(lord))
            # print("Lord Has Been Slain\n")
            return "Lord Has Been Slain\n"


def main():
    hero = pilihHero(heroes)
    selectedherospell = pilihMantra(hero, mantra)
    hero_name = selectedherospell["Hero"]
    hero_role = selectedherospell["Role"]
    hero_dmg = selectedherospell["DMG"]
    hero_spell = selectedherospell["Spell"]

    print("Welcome to mini Mobile Legends Game\n\n")
    pilihan = input("mulai main (y) / batal (n)?")
    if pilihan.lower() == 'y':
        flag = True
    else:
        print("Thank you for playing this game")
        flag = False

    while flag:
        print("Select the activity you want to do:")
        menu = ["Check Hero", "Buy Item", "Fight Lord", "Exit"]
        print_for(lambda x, y: f"{x + 1}. {y}", 0, menu)
        inputs = input("Choose the number :) ")
        if inputs == "1":
            print(print_format("{} - {} - DMG {} - Spell {}", hero_name, hero_role, hero_dmg, hero_spell))
        elif inputs == "2":
            selectedherospell = beli_item(selectedherospell)
        elif inputs == "3":
            print(bertarung(selectedherospell))
        elif inputs == "4":
            print("Thank you for playing this game")
            flag = False
        else:
            return "Wrong Input"


main()
