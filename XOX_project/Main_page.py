from XOX_project.Single_player import SinglePlayer
from XOX_project.Multi_player import MultiPlayer


def main():
    while True:
        game_type = input("SINGLE PLAYER OR MULTI PLAYER (S OR M): ").upper()
        if game_type in ["S", "M"]:
            break
        else:
            print('***ENTER PROPER INPUT***')

    if game_type == "S":
        difficulty = input("EASY MODE OR HARD MODE (E OR H): ").upper()
        while difficulty not in ["E", "H"]:
            print('***ENTER PROPER INPUT***')
            difficulty = input("EASY MODE OR HARD MODE (E OR H): ").upper()
        game = SinglePlayer(difficulty)
    else:
        game = MultiPlayer()

    game.play()


if __name__ == "__main__":
    main()
