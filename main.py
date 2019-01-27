from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "damage": 60},
         {"name": "Thunder", "cost": 10, "damage": 50},
         {"name": "Blizzard", "cost": 10, "damage": 70},]


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
        print("You attacked for ", damage, " damage. Enemy HP:", enemy.get_hp() )

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("Enemy attacks for ", enemy_damage, " damange. Player HP:", player.get_hp())