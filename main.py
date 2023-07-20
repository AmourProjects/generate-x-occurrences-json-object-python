import json
import random
from datetime import date, timedelta

# List of possible names
possible_names = [
    "Pasta DANSSOU",
    "John Doe",
    "Jane Smith",
    "Alice Johnson",
    "Bob Williams",
    "Michael Brown",
    "Jennifer Davis",
    "David Wilson",
    "Lisa Martinez",
    "James Anderson",
    "Sophia Lee",
    "Alexander Perez",
    "Mia Turner",
    "Daniel Scott",
    "Emma Garcia",
    "Andrew Miller",
    "Olivia Rodriguez",
    "Joseph Taylor",
    "Ava Martinez",
    "William Hernandez",
    "Isabella Lopez",
    "Christopher Gonzalez",
    "Sophie King",
    "Samuel White",
    "Sofia Mitchell",
    "Josephine Adams",
    "Jacob Turner",
    "Grace Campbell",
    "Ethan Hill",
    "Chloe Murphy",
    "Ryan Cooper",
    "Lily Hall",
    "Matthew Allen",
    "Hannah Green",
    "Benjamin Rivera",
    "Amelia Ward",
    "Nathan Torres",
    "Ella Carter",
    "Logan Phillips",
    "Avery Baker",
    "Liam Wright",
    "Aria Parker",
    "Jayden Stewart",
    "Harper Turner",
    "Muhammad Sanchez",
    "Scarlett Collins",
    "Aiden Howard",
    "Aubrey Price",
    "Lucas Powell",
    "Eleanor Jenkins",
    "Gabriel Reed",
    "Madison Ross",
    "Henry Cox",
    "Elizabeth Rivera",
    "Owen Bennett",
    "Addison Long",
    "Jackson Hughes",
    "Victoria Perry",
    "Sebastian Jenkins",
    "Grace Foster",
    "David Murphy",
    "Penelope Hayes",
    "Carter Simmons",
    "Aurora Ramirez",
    "Matthew Ward",
    "Luna Coleman",
    "Connor Powell",
    "Stella Richardson",
    "Julian Scott",
    "Savannah Myers",
    "Eli Collins",
    "Brooklyn Reed",
    "Wyatt Howard",
    "Natalie Bryant",
    "Grayson Kim",
    "Layla Washington",
    "Isaac Butler",
    "Hazel Brooks",
    "Anthony Bell",
    "Skylar Gomez",
    "Thomas Price",
    "Paisley Coleman",
    "Jonathan Stewart",
    "Bella Watson",
    "Levi Jenkins",
    "Nova Mitchell",
    "Christopher Bailey",
    "Emilia Green",
    "Josiah Diaz",
    "Lillian Torres",
    "Joshua Cooper",
]

def generate_random_data():
    data = {
        "id": random.randint(1, 100),
        "name": random.choice(possible_names),
        "date": str(date.today() - timedelta(days=random.randint(0, 365))),
        "amount": str(random.randint(100000, 500000)),
        "observation": "RAS"
    }
    return data

# Total number of desired occurrences
total_occurrences = 50000000

# Create a list of 50,000,000 different JSON object occurrences
json_list = [generate_random_data() for _ in range(total_occurrences)]

# Write the list to a JSON file
with open('output.json', 'w') as outfile:
    json.dump(json_list, outfile)

print("The JSON file with 50,000,000 random occurrences including the 'name' field was created.")
