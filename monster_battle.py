player = {'name': 'A A-Ron', 'attack': 10, 'heal': 16, 'health': 100}
monster = {'name': 'Booger Jones', 'attack': 12, 'health': 100}
game_running = True

while game_running == True:
    print('Welcome to Monster Battle')
    print(f"1) Attack {monster['name']}")
    print("2) Heal yourself!")

    player_input = input()

    if player_input == '1':
        print(f"Attacking {monster['name']} for {player['attack']} hit points...\n")
        monster['health'] = monster['health'] - player['attack']
        print(f"{monster['name']} health: {monster['health']}\n")
    elif player_input == '2':
        print(f'Ohh that healing feeling!\n')
        player['health'] = player['health'] + player['heal']
    else:
        print('Sorry, game over sucka!')
        game_running = False

    if monster['health'] <= 0:
        print(f"{player['name']} wins!! {monster['name']} FATALITY :)\n")
        print("GAME OVER")
        game_running = False