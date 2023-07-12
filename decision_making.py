import requests
import pandas as pd

#Function that retrieves information about an anime based on its MAL ID 
def animeInfo(id):

    #makes a request to the JIKANPY API using the requests library 
    anime_id = requests.get(f"https://api.jikan.moe/v4/anime/{id}/full").json()["data"]

    #stores relevant information about anime into an array
    info = [
        anime_id["title"],
        anime_id["episodes"],
        anime_id["status"],
        anime_id["airing"],
        anime_id["score"],
        anime_id["year"]
    ]
    return info

# Retrieve information for the first anime (ID: 1)
init = animeInfo(1)

# Create initial DataFrame with the first anime's information
mydfdata = [(init[0], init[1], init[2], init[3], init[4], init[5] )]
mydf = pd.DataFrame(mydfdata, columns = ['name', 'episodes', 'status', 'airing', 'score', 'year'])

# Loop to retrieve information for multiple anime (IDs: 15 to 199)
anime_data = []
for i in range(15, 200):
    try:
        anime_data.append(animeInfo(i))
        #mydf.loc[len(mydf.index)] = [anime[0], anime[1], anime[2], anime[3], anime[4], anime[5]]
    except KeyError:
        #Ignore any anime for which information couldn't be retrieved (KeyError)
        continue

# Concatenate the new anime data with the existing DataFrame
mydf = pd.concat([mydf, pd.DataFrame(anime_data, columns=mydf.columns)], ignore_index=True)

# Display the DataFrame with all anime information
print(mydf)


#Multiple User promts to filter the dataframe and find the right anime for the user 
while True:
    try:
        episodes = int(input("How many episodes do you want the anime to have (max): "))
        if episodes <= 0:
            print("Please enter a positive integer value.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


while True:
    try:
        score = float(input("what would you like the anime to have a minimum score of? (format x.xx): "))
        if score <= 0.00:
            print("Please enter a positive value.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

        
while True:
    try:
        year = int(input("At what year would you like the anime to have been released at the very least? (format xxxx): "))
        if year <= 0:
            print("Please enter a positive integer value.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


print("-----------------Filtering criteria:----------------------")
print("Episodes:", episodes)
print("Score:", score)
print("Year:", year)

# Filter the DataFrame based on the user's criteria
filtered_df = mydf.query('episodes <= @episodes and score >= @score and year >= @year')
print(filtered_df)

