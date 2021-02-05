text = open("WorldSeriesWinners.txt", "r")

year = 1903
series_wins = {}
year_wins = {}
team_list = []
for team in text:
    team = team.strip()
    team = team.split("\n")
    team_list.append(team)

    for team in team:
        if team in series_wins:
            series_wins[team] = series_wins[team] + 1
        else:
            series_wins[team] = 1

text.close
text = open("WorldSeriesWinners.txt", "r")
for team in text:
    team = team.strip()
    team = team.split("\n")

    for team in team:
        if year == 1904 or year == 1994:
            year += 1
            year_wins[year] = team
    else:
        if year in year_wins:
            year += 1
        else:
            year_wins[year] = team
            year += 1
print(year_wins)


# for key in year_wins:
# print(key, ":", year_wins[key])


def sorted_wins(series_wins):
    for key in series_wins:
        print(key, ":", series_wins[key])
    print("\n\n")


def specific_year(series_wins, year_wins):
    choice = int(input("Enter a year from 1903 - 2009: "))

    if choice == 1904 or choice == 1994:
        print("There was no World Series in", choice)
    elif choice < 1903 or choice > 2009:
        print("The year chosen is outside of the required range")
    else:
        print("The team that won in", choice, "was the", year_wins[choice])
        team = year_wins[choice]
        win_number = series_wins[team]
        print("The", team, "have won the World Series", win_number, "times.")


sorted_wins(series_wins)
specific_year(series_wins, year_wins)
