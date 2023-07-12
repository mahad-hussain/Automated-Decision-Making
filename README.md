# Automated-Decision-Making
Script that aids user in finding anime based on certain criteria

# Anime Data Filtering

This script retrieves information about anime from the Jikan API and allows you to filter the data based on criteria such as the number of episodes, minimum score, and minimum release year. The filtered results are displayed in a DataFrame using the pandas library.

## Prerequisites

- Python 3.x
- requests library (`pip install requests`)
- pandas library (`pip install pandas`)

## Usage

1. Clone the repository or download the `anime_data_filtering.py` file.

2. Install the required dependencies by running the following command:
pip install -r requirements.txt

3. Run the script using the following command:
python anime_data_filtering.py

4. Follow the prompts to input the desired filtering criteria:
- Enter the maximum number of episodes you want the anime to have.
- Enter the minimum score you want the anime to have.
- Enter the minimum release year for the anime.

5. After providing the filtering criteria, the script will display the filtered anime information in a DataFrame.

## Example

Here is an example usage scenario:

$ python anime_data_filtering.py

[Output]
name episodes status airing score year
0 Anime1 12 Airing True 8.5 2020
1 Anime2 24 Ended False 7.9 2018
2 Anime3 10 Airing True 9.1 2022

How many episodes do you want the anime to have (max): 15
What would you like the anime to have a minimum score of? (format x.xx): 8.0
At what year would you like the anime to have been released at the very least? (format xxxx): 2021

-----------------Filtering criteria:----------------------
Episodes: 15
Score: 8.0
Year: 2021

name episodes status airing score year
0 Anime1 12 Airing True 8.5 2020

In this example, the script retrieves anime information from the Jikan API and displays it in the initial DataFrame. The user then specifies the filtering criteria, and the script filters the anime based on the provided criteria, displaying the filtered results.

Feel free to modify the code according to your requirements and enjoy finding anime!

Please note that you may need to adjust the file name and dependencies section based on the actual file name and the libraries used in your code.
