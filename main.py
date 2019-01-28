from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "damage": 100},
         {"name": "Thunder", "cost": 10, "damage": 120},
         {"name": "Blizzard", "cost": 10, "damage": 150},]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

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
        print("You attacked for ", damage, " damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic: ")) - 1
        magic_damage = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough Magic Points!\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_damage)
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_damage), " points of damage!" + bcolors.ENDC)

        print("=============================")
        print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC + "\n")

        print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
        print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")


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