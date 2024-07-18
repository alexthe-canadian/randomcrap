import random
import time
import linecache
f = open('pokemonsaves.txt', 'r')


def battle():
    #read from save file
    num = 0
    pokemoncount = len(f.readlines())
    print(f'Which pokemon do you want to play as? (1 to {pokemoncount}): ')
    for i in range(pokemoncount):
     num = num + 1
     plr = linecache.getline('pokemonsaves.txt', num)
     pname = plr.split('/')
     pname2 = pname[0]
     print(num, '. ', pname2)
    pokemon = input(f'Select a pokemon (1 to {pokemoncount}): ')
    plr = int(pokemon)
    plrline = linecache.getline('pokemonsaves.txt', plr)
    plrstats = plrline.split('/')
    player_name = plrstats[0]
    player_health = int(plrstats[1])
    if(player_health > 1000):
        print('Invalid Health')
        exit(1)
    print(f'Which pokemon do you want your opponent to be? (1 to {pokemoncount}):  ')
    num = 0
    for i in range(pokemoncount):
     num = num + 1
     plr = linecache.getline('pokemonsaves.txt', num)
     pname = plr.split('/')
     pname2 = pname[0]
     print(num, '. ', pname2)
    cpupokemon = input(f'What pokemon do you want your opponent to be (1 to {pokemoncount}): ')
    cpup = int(cpupokemon)
    cpu = linecache.getline('pokemonsaves.txt', cpup)
    cpustats = cpu.split('/')
    cpu_name = cpustats[0]
    cpu_health = int(cpustats[1])
    if(cpu_health > 1000):
        print('Invalid Health')
        exit(1)
    
    #setup attacks
    player_attacks = [plrstats[2], plrstats[3], plrstats[4]]
    cpu_attacks = [cpustats[2], cpustats[3], cpustats[4]]
    

    print(f"{player_name} vs. {cpu_name}!")

    while True:
        print(f"{player_name}: {player_health} HP")
        print(f"{cpu_name}: {cpu_health} HP")

        time.sleep(1)

        print("\nYour turn!")
        print("Choose your attack:")
        for i, attack in enumerate(player_attacks, 1):
            print(f"{i}. {attack}")

        player_attack = int(input("Enter the number of your attack: "))

        time.sleep(1)

        if player_attack == 1:
            print(f"{player_name} used {player_attacks[0]}!")
            time.sleep(1)
            damage = random.randint(10, 15)
            cpu_health -= damage
            print(f"{cpu_name} took {damage} damage!")
        elif player_attack == 2:
            print(f"{player_name} used {player_attacks[1]}")
            time.sleep(1)
            damage = random.randint(5, 20)
            cpu_health -= damage
            print(f"{cpu_name} took {damage} damage!")
        elif player_attack == 3:
            print(f"{player_name} used {player_attacks[2]}")
            time.sleep(1)
            damage = random.randint(0, 30)
            cpu_health -= damage
            print(f"{cpu_name} took {damage} damage!")
        else:
            time.sleep(1)
            print("You missed!")

        time.sleep(1)

        if cpu_health <= 0:

            print(f"{cpu_name} fainted!")
            break

        print(f"\n{cpu_name}'s turn!")

        cpu_attack = random.randint(1, 3)

        time.sleep(1)

        if cpu_attack == 1:
            print(f"{cpu_name} used {cpu_attacks[0]}")
            time.sleep(1)
            damage = random.randint(10, 15)
            player_health -= damage
            print(f"{player_name} took {damage} damage!")
        elif cpu_attack == 2:
            print(f"{cpu_name} used {cpu_attacks[1]}")
            time.sleep(1)
            damage = random.randint(5, 20)
            player_health -= damage
            print(f"{player_name} took {damage} damage!")
        elif cpu_attack == 3:
            print(f"{cpu_name} used {cpu_attacks[2]}")
            time.sleep(1)
            damage = random.randint(0, 30)
            player_health -= damage
            print(f"{player_name} took {damage} damage!")

        time.sleep(1)

        if player_health <= 0:
            print(f"{player_name} fainted!")
            break

        print("\nNext round!")

    print("\nBattle over!")
    if player_health <= 0:
        winner = 'cpu'
    else:
        winner = 'player'
    winnercongrat(winner, player_health)
    time.sleep(5)

def winnercongrat(winner, plrhealth):
    if(winner == "player"):
        
        print("""
                 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌▐░▌    ▐░▌▐░▌          ▐░▌       ▐░▌
▐░▌   ▄   ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌ ▐░▌░▌ ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌          ▐░▌     ▐░▌  
▐░▌░▌   ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀                                                               
          """)
        print("""
         ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌      ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
 ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌          ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌          ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀            ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
          """)
        print('\n\n\n\n')
        print(f'Thanks for playing, of course. You won with {plrhealth} of your health left')
    else:
        print("""
            
                 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌▐░▌    ▐░▌▐░▌          ▐░▌       ▐░▌
▐░▌   ▄   ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌ ▐░▌░▌ ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌          ▐░▌     ▐░▌  
▐░▌░▌   ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀   
              """)
        print("""
▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌
     ▐░▌     ▐░▌               ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌
     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌
     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌
     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌
     ▐░▌               ▐░▌     ▐░▌          ▐░▌          ▐░▌       ▐░▌
 ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                      
              """)
        print('\n\n\n\n')
        print('Thanks for playing, of course.')


battle()
