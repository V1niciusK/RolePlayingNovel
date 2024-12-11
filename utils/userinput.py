import saythis

def read_options(choices: list):
    saythis.narrating("Your options are:")
    for choice in choices:
        saythis.narrating(f" - {choice}")

def user_choses(pre_message: str, choices: list):
    saythis.narrating(pre_message)
    read_options(choices)
    usr_input = input("Pick an option:  ")
    while usr_input not in choices:
        saythis.narrating("I didn't quite catch that. Please type one of the options")
        read_options(choices)
        usr_input = input("Pick an option:  ")
    
    return usr_input

if __name__ == "__main__":
    print("Testing user input")
    test_choices = ['I see a choice', 'I see another choice', 'turnip']
    print(f"{test_choices = }")
    usr_chosen = user_choses("This is a test user input", test_choices)
    print(f"The choice picked was: {usr_chosen}")
    print("Test end")
