class Chessplayer:
    def __init__(self, name = "", year = 0, rating = 0):
        self.name = name
        self.year = year
        self.rating = rating
    def __str__(self):
        return "Name: {}\nYear: {}\nRating: {}".format(self.name, self.year, self.rating)

def get_highest_rated_player(players):
    highest_rating = 0
    for player in players:
        if player.rating > highest_rating:
            highest_rating = player.rating
            highest_rating_player = player
    return highest_rating_player

def get_average_rating(players):
    sum_of = 0
    for player in players:
        sum_of += player.rating
    average = sum_of/len(players)
    return "{:.2f}".format(average)
    
def main():   
    number_of_players = int(input("Number of players: "))
    players = []
    counter = 0
    print("--- Reading players ---")
    #here you should get info from the user about 
    #number_of_players many chess player
    # code goes here...
    while counter < number_of_players:
        name = input("Enter Name: ")
        year = int(input("Enter Year: "))
        rating = int(input("Enter Rating: "))
        print("")
        players.append(Chessplayer(name, year, rating))
        counter += 1
    print("--- Displaying players ---")
    #here you should print each player
    #code goes here....
    for player in players:
        print("Name: {}".format(player.name))
        print("Year: {}".format(player.year))
        print("Rating: {}".format(player.rating))
        print()
    highest_rated_player = get_highest_rated_player(players)
    print("Highest rated player: ")
    print(highest_rated_player)
    print()

    average_rating = get_average_rating(players)
    print("Average rating:", average_rating)

main()