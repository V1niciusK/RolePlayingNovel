from sys import stdout
from time import sleep

def narrating(text: str) -> None:
    text_lines = text.split("\n")
    for line in text_lines:
        talk(line, 0.03)
        sleep( len(line) / 40 )

def gently(message: str) -> None:
    talk(message, 0.08)

def normally(message: str) -> None:
    talk(message, 0.06)

def slowly(message: str) -> None:
    talk(message, 0.03)

def screaming(message: str) -> None:
    talk(message.upper() , 0.3)

def talk(message: str, speed: float) -> None:
    """Slowly prints a message, character by character, pausing between characters.

    Args:
        message (str): The message to be printed character by character
        speed (float): Waiting period between characters. Recommended to be between 0.01 (regular speed) and 0.03 (really slow)
    """
    for char in message:
        if char == " ":
            sleep(0.02)
        stdout.write(char)
        stdout.flush()
        sleep(speed)
    sleep(0.03)
    print("")

if __name__ == "__main__":
    print("Testing saythis")

    gentle = "This is a gentle text"
    normaltxt = "This is a normal text"
    scream = "This is a scream!"
    print("Testing inputs:")
    print(f"{gentle = }")
    print(f"{normaltxt = }")
    print(f"{scream = }")
    print("Testing gentle:")
    gently(gentle)
    print("Testing normal")
    normally(normaltxt)
    print("Testing scream")
    screaming(scream)
    print("End test")