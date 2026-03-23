def collect_info():
    """Collect information about a person"""
    info = {
        "name": input("What is your name? "),
        "city": input("What city are you in? "),
        "hobby": input("What is your favorite hobby? "),
        "ai_goal": input("What do you hope to build with AI? ")
    }
    return info

def save_to_file (info, filename="my_info.txt"):
    """Save the collected information to a text file."""
    with open(filename,"w") as file:
        file.write("=== My Profile ===\n")
        for key,value in info.items():
            file.write(f"{key.capitalize()}: {value}\n")
        print(f"\nSaved your profile to {filename}!")

def main():
    print("Welcome to your Personal Organizer!")
    print("-" * 35)
    my_info = collect_info()
    save_to_file(my_info)

main()