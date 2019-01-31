from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


print("\n\n")

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
mega_elixir = Item("Mega Elixir", "elixir", "Fully restores whole party's HP/MP", 9999)


grenade = Item("Grenade", "attack", "Explodes to deal 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, heal]
player_items = [{"item": potion, "quantity": 5},
                {"item": hi_potion, "quantity": 3},
                {"item": super_potion, "quantity": 1},
                {"item": elixir, "quantity": 2},
                {"item": mega_elixir, "quantity": 1},
                {"item": grenade, "quantity": 3}]

# Instantiate people
player1 = Person("Icarus", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Malachi", 460, 65, 60, 34, player_spells, player_items)

enemy1 = Person("Thanos", 1200, 65, 45, 25, [], [])
enemy2 = Person("Grom", 1200, 65, 45, 25, [], [])

players = [player1, player2]
enemies = [enemy1, enemy2]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An enemy attacks!" + bcolors.ENDC)

while running:
    print("==================")

    print("\n")
    for player in players:
        player.get_stats()
        print("------------------------------------------------------------------")

        print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index == 0:
            damage = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(damage)
            print("=============================")
            print("You attacked " + enemies[enemy].name + " for ", damage, " damage.")

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
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_damage)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_damage),
                      " points of damage to " + enemies[enemy].name + bcolors.ENDC)

            print("=============================")
            print("Enemy HP: ", bcolors.FAIL + str(enemies[enemy].get_hp()) + "/" + str(enemies[enemy].get_maxhp()) + bcolors.ENDC + "\n")

            print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
            print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for ", str(item.prop), " HP" + bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "Mega Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp

                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP & MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals ", str(item.prop),
                      " points of damage to " + enemies[enemy].name + bcolors.ENDC)

    enemy_choice = 1
    target = random.randrange(len(players))
    enemy_damage = enemies[0].generate_damage()
    players[target].take_damage(enemy_damage)
    print("Enemy attacks for ", enemy_damage, " damage.")

    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
        running = False

    elif defeated_players == 2:
        print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
        running = False