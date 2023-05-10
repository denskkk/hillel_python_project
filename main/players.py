def players_repr(players: list[dict], verbose: bool) -> None:
    if verbose:
        print(">>>> TEAM:")

    for player in players:
        print(f"{player['name']=}, {player['age']=}")


def players_add(players: list[dict], player: dict) -> list[dict]:
    players.append(player)
    return players


def players_del(players: list[dict], name: str) -> list[dict]:
    players = [p for p in players if p["name"] != name]
    return players


def players_find(players: list[dict], name: str) -> list[dict]:
    result = [p for p in players if p["name"] == name]
    return result


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    for player in players:
        if player["name"] == name:
            return player
    return None


def main():
    team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Marry", "age": 33, "number": 3},
        {"name": "Cavin", "age": 33, "number": 12},
    ]

    options = ["repr", "add", "del", "find", "get", "exit"]

    while True:
        if not (user_input := input(f"Enter your choice {options}:")):
            break

        if user_input == "repr":
            players_repr(team, True)
        elif user_input == "add":
            player = {
                "name": input("Enter player name: "),
                "age": int(input("Enter player age: ")),
                "number": int(input("Enter player number: ")),
            }
            team = players_add(team, player)
        elif user_input == "del":
            name = input("Enter player name to delete: ")
            team = players_del(team, name)
        elif user_input == "find":
            name = input("Enter player name to search: ")
            players = players_find(team, name)
            players_repr(players, True)

        elif user_input == "get":
            name = input("Enter player name to get: ")
            player = players_get_by_name(team, name)
            if player:
                print(f"{player['name']} found.")
            else:
                print(f"No player found with name {name}.")
        elif user_input == "exit":
            break
        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
