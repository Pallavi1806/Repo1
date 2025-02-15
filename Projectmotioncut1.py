import random
import string

# Pre-defined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Fast", "Brave", "Silly", "Clever", "Lucky", "Funky", "Chill", "Swift"]
nouns = ["Tiger", "Dragon", "Eagle", "Panther", "Wolf", "Bear", "Shark", "Falcon", "Lion", "Hawk"]

# Function to generate a random username
def generate_username(include_numbers=True, include_special_chars=True, length=8):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    username = adjective + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special_chars:
        username += random.choice(string.punctuation)
    
    # Adjust length if needed
    if len(username) > length:
        username = username[:length]
    
    return username

# Function to save usernames to a file
def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"\nUsernames saved to {filename}")

# Main function to interact with the user
def main():
    print("Welcome to the Random Username Generator!")
    
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers in usernames? (yes/no): ").strip().lower() == "yes"
    include_special_chars = input("Include special characters in usernames? (yes/no): ").strip().lower() == "yes"
    length = int(input("Enter the maximum length for usernames (default is 8): ") or 8)
    
    usernames = []
    for _ in range(num_usernames):
        username = generate_username(include_numbers, include_special_chars, length)
        usernames.append(username)
        print(f"Generated username: {username}")
    
    save_usernames(usernames)

if __name__ == "__main__":
    main()
