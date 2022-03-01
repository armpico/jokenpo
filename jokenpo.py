import random

from click import option

class Option:
    rock = 'pedra'
    papper = 'papel'
    scissors = 'tesoura'

    def from_int(int_value:int) -> str:
        assert(int_value in {1,2,3})
        if int_value == 1:
            Option.rock
            return Option.rock
        if int_value == 2:
            return Option.papper
        if int_value == 3:
            return Option.scissors

class Result:
    player = 'O jogador venceu.'
    opponent = 'O oponente venceu.'
    draw = 'Empate.'

def winner(player_option: str, opponent_option: str) -> str:
    if player_option == Option.rock and opponent_option == Option.rock:
        return Result.draw
    if player_option == Option.rock and opponent_option == Option.papper:
        return Result.opponent
    if player_option == Option.rock and opponent_option == Option.scissors:
        return Result.player
    if player_option == Option.papper and opponent_option == Option.rock:
        return Result.player
    if player_option == Option.papper and opponent_option == Option.papper:
        return Result.draw
    if player_option == Option.papper and opponent_option == Option.scissors:
        return Result.opponent
    if player_option == Option.scissors and opponent_option == Option.rock:
        return Result.opponent
    if player_option == Option.scissors and opponent_option == Option.papper:
        return Result.player
    if player_option == Option.scissors and opponent_option == Option.scissors:
        return Result.draw

while True:
    player_input = input("\n1-Pedra\n2-Papel\n3-Tesoura\nq-Sair\n\n>> ")
    if player_input == 'q':
        break
    if player_input not in {'1','2','3'}:
        print('Opção inválida')
        continue
    
    player_option = Option.from_int(int(player_input))
    opponent_option = Option.from_int(random.randrange(1,4))

    print(f"O jogador escolheu {player_option}.")
    print(f"O oponente escolheu {opponent_option}.")

    print(winner(player_option, opponent_option))
