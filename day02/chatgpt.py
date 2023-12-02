def is_possible(game, red_count, green_count, blue_count):
    current_red = 0
    current_green = 0
    current_blue = 0

    for subset in game:
        for cube in subset:
            count, color = cube.split() # color, count = cube.split()
            count = int(count)
            if color == 'red':
                current_red += count
            elif color == 'green':
                current_green += count
            elif color == 'blue':
                current_blue += count

    return current_red <= red_count and current_green <= green_count and current_blue <= blue_count # return current_red == red_count and current_green == green_count and current_blue == blue_count


def possible_games(games, red_count, green_count, blue_count):
    possible_game_ids = []

    for game_id, game in games.items():
        if is_possible(game, red_count, green_count, blue_count):
            possible_game_ids.append(game_id)

    return possible_game_ids


def main():
    games_input = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ]

    games = {}

    for game_input in games_input:
        game_info = game_input.split(":")
        game_id = int(game_info[0].split()[1])
        subsets = [subset.strip().split(",") for subset in game_info[1].split(";")]
        games[game_id] = subsets

    red_count = 12
    green_count = 13
    blue_count = 14

    possible_ids = possible_games(games, red_count, green_count, blue_count)

    print("Possible game IDs:", possible_ids)
    print("Sum of possible game IDs:", sum(possible_ids))


if __name__ == "__main__":
    main()