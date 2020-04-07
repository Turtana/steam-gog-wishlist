import requests
import sys
import webbrowser

print("This program requires that your Steam wishlist is public. If it's not, set it to public and restart this program.")
profId = input("Your Steam profile ID: ")

steam_url = "https://store.steampowered.com/wishlist/profiles/" + profId + "/wishlistdata/"
gog_search_url = "https://embed.gog.com/games/ajax/filtered?mediaType=game&search="
gog = "https://www.gog.com/"

data = requests.get(url = steam_url).json()

steam_game_names = []
gog_games = {}
for game in data:
    steam_game_names.append(data[game]["name"])

print("\nYour Steam wishlist:\n")

for name in steam_game_names:
    search_url = gog_search_url + name
    data = requests.get(url = search_url).json()
    if len(data["products"]) > 0:
        for product in data["products"]:
            if product["title"].lower() == name.lower():
                print(name + ": Found!")
                gog_games[name] = product["url"]
                break
        else:
            print(name + ": Not found")
    else:
        print(name + ": Not found")

print("\nThe following games in your Steam wishlist can be found in GOG:\n")
for game in gog_games:
    print(game)
print()

select = ""
while select != "y" and select != "n":
    select = input("Open the store pages of these games in your web browser? (y/n): ")
if select == "n":
    sys.exit()

for game in gog_games:
    webbrowser.open(gog + gog_games[game])






