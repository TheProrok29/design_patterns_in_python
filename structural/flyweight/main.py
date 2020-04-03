from structural.flyweight.game import CounterGame

game = CounterGame()
game.main_game()
for player in game.players:
    print(id(player.weapon))
