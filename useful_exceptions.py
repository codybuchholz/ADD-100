def modify_artist_list(top_artists):
    try:
        index = int(input("Enter the number of the artist to replace: "))
        new_artist = input("Enter the new artist name: ")
        top_artists[index] = new_artist
        print("Updated list:", top_artists)
    except (ValueError, IndexError):
        print("An input error occurred.")


def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", 
                   "Mariah Carey", "Stevie Wonder", "Janet Jackson", 
                   "Michael Jackson", "Whitney Houston", "Rihanna"]
    modify_artist_list(top_artists)


main()