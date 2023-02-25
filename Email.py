import random
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--scrambled', type=bool, default=False)
args = parser.parse_args()

def generate_email():
    # List available domain names
    domains = ["outlook.com", "yahoo.com", "cloudbreakers.com", "msn.com", "aol.com", "icloud.com", "gmx.com", "zoho.com", "gmail.com"]
    # Choose random domain from list
    domain = random.choice(domains)

    if args.scrambled: # scrambled characters usersname
        # Listing possible characteres username
        letters = string.ascii_lowercase
        # Generating random username of 10 characters length
        username = ''.join(random.choice(letters) for i in range(10))
    else : # more humanoid username
        # List of adjectives and nouns to choose from
        adjectives = ['vt', 'turn', 'funny', 'serious', 'smart', 'holy', 'cute', 'XY', 'lol', 'fyi']
        nouns = ['frank', 'zita', 'turan', 'morgan', 'lion', 'tiger', 'local','cedric','nelly', 'tom', 'tim', 'tessa', 'bert', 'sam']
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        # Generate a random username by combining two words
        username = random.choice(adjectives) + random.choice(nouns) + str(num1) + str(num2)

    # Combination of username & domain to get a complete e-mailadres
    email = username + "@" + domain
    return email

print(generate_email())