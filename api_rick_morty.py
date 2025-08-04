"""
This script queries the Rick and Morty API to retrieve information about characters
based on a user-provided name.

How it works:
- The user is prompted to enter the name of a character.
- The script sends a GET request to the Rick and Morty API with the character name as a query parameter.
- If the API returns a successful response (HTTP 200), it parses the JSON data.
- It then checks for matching characters and prints basic information for each match:
  - Name
  - Status (Alive, Dead, or Unknown)
  - Species (e.g., Human, Alien)
- If no characters are found, or the API fails to respond properly, it notifies the user.

Example usage:
    Enter the Character: Rick
    Name: Rick Sanchez, Status: Alive, Species: Human
"""

import requests

character = input("Enter the Character: ")

url = f'https://rickandmortyapi.com/api/character/?name={character}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    results = data.get('results', [])
    if results:
        for char in results:
            print(f"Name: {char['name']}, Status: {char['status']}, Species: {char['species']}")
    else:
        print("No characters found.")
else:
    print(f"Failed to retrieve data: {response.status_code}")
