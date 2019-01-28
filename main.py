from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


# Create black magic.py
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic.py
cure = Spell("Cure", 12, 120, "white")
heal = Spell("Heal", 18, 200, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 hp", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 hp", 100)
super_potion = Item("Super-Potion", "potion", "Heals 200 hp", 200)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
super_elixir = Item("Super Elixir", "elixir", "Fully restores whole party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Explodes to deal 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, heal]
player_items = [potion, hi_potion, super_potion, elixir, grenade]

# Instantiate people
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An enemy attacks!" + bcolors.ENDC)

while running:
    print("==================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        damage = player.generate_damage()
        enemy.take_damage(damage)
        print("=============================")
        print("You attacked for ", damage, " damage.")
        print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC + "\n")

        print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_damage = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough Magic Points!\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_damage)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for ",  str(magic_damage), " HP" + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_damage)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_damage), " points of damage!" + bcolors.ENDC)

        print("=============================")
        print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC + "\n")

        print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
        print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")

    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose Item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for ", str(item.prop), " HP" + bcolors.ENDC)

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("Enemy attacks for ", enemy_damage, " damage.")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You have been defeated!" + bcolors.ENDC)
        running = False