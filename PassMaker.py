import random
from time import sleep

# Colors code
r = "\033[1;31;40m"
b = "\033[1;34;40m"
g = "\033[1;32;40m"
bl = "\033[1;30;40m"
w = "\033[3;37;40m"
y = "\033[1;33;40m"

# Variables for composition
alphabets = "abcdefghijklmnopqrstuvwxyz"
upper = alphabets.upper()
numbers = "0123456789"
symbols = "!@#$%^&*?"


# Banner
def printLow(Str):
    for char in Str:
        print(char, end="", flush=True)
        sleep(.005)
printLow(
    f'''
{r}
{r}    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
{r}    █{b}   ╭━━━╮╱╱╱╱╱╱╱╱╭━╮╭━╮╱╱╭╮        {r}        █
{r}    █{b}   ┃╭━╮┃╱╱╱╱╱╱╱╱┃┃╰╯┃┃╱╱┃┃        {r}        █
{r}    █{b}   ┃╰━╯┣━━┳━━┳━━┫╭╮╭╮┣━━┫┃╭┳━━┳━╮ {r}        █
{r}    █{b}   ┃╭━━┫╭╮┃━━┫━━┫┃┃┃┃┃╭╮┃╰╯┫┃━┫╭╯ {r}        █
{r}    █{b}   ┃┃╱╱┃╭╮┣━━┣━━┃┃┃┃┃┃╭╮┃╭╮┫┃━┫┃  {r}        █
{r}    █{b}   ╰╯╱╱╰╯╰┻━━┻━━┻╯╰╯╰┻╯╰┻╯╰┻━━┻╯  {r}        █
{r}    █{y}         made by: @Amirprx3       {r}        █
{r}    █{y}   Github: https://github.com/Amirprx3{r}    █
{r}    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

    '''
)

# Get password length
def get_length():
    while True:
        try:
            length = input(f"\n{g}[+] {w}Enter the number of characters (must be between 4 and 16): ")  #Amirprx3
            if length.isdigit() and 4 <= int(length) <= 16:
                return int(length)
            else:
                print(f"{y}    The character count should be between 4 and 16. Please try again. {g}")
        except ValueError:
            print(f"{y}    Invalid input. Please enter a number. {g}")

# Choose custom or random password
def get_custom_or_random():
    while True:
        choice = input(f"{g}[+] {w}Custom or random password (custom/random)==> ").lower()
        if choice in ["custom", "random"]:
            return choice
        else:
            print(f"{y}Invalid option. Please enter 'custom' or 'random'. {g}")

# Using symbol for custom password
def get_symbols_choice():
    while True:
        choice = input(f"{g}[+] {w}Are you using the symbols (Yes/No)==> ").lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print(f"{y}Invalid input. Please enter 'Yes' or 'No'. {g}")  #Amirprx3

# Get password number
def get_number_of_passwords():
    while True:
        num_passwords = input(f"{g}[+] {w}How many passwords do you need==> ")
        if num_passwords.isdigit() and int(num_passwords) > 0:
            return int(num_passwords)
        else:
            print(f"{y}Invalid input. Please enter a positive number. {g}")

# Firstname and Lastname error handeling
def get_name(prompt):
    while True:
        name = input(f"{g}[-] {w}{prompt}: ")
        if name.strip():
            return name
        else:
            print(f"{y}Invalid input. Please enter a non-empty name. {g}")  #Amirprx3

# Birth year error handeling
def get_year(prompt):
    while True:
        year = input(f"{g}[-] {w}{prompt}: ")
        if year.isdigit():
            return year
        else:
            print(f"{y}Invalid input. Please enter a valid year. {g}")

# Generate password and create a text file and put the password in the file
def generate_passwords(password_string, length, file_name, num_passwords):
    with open(file_name + ".txt", "a") as file:
        for _ in range(num_passwords):
            password = "".join(random.sample(password_string, length))
            file.write(password + "\n\n")
    print(f"{g}[✓] Your password file has been created.")

# Calling functions 
def main():
    length = get_length()
    choice = get_custom_or_random()
    
    if choice == "custom":
        Fname = get_name("FirstName")
        Lname = get_name("LastName")
        Year = get_year("BirthYear")
        if get_symbols_choice():
            password_string = Fname + Lname + Year + symbols
        else:
            password_string = Fname + Lname + Year
    else:
        password_string = alphabets + upper + numbers + symbols
    
    file_name = get_name("Enter the name for text file")
    num_passwords = get_number_of_passwords()
    
    generate_passwords(password_string, length, file_name, num_passwords)

if __name__ == "__main__":
    main()

# Amirprx3