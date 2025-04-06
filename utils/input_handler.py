from colorama import init, Fore, Style

def validate(input_:str, type:str, selection:dict=None):
    if not input_:
        raise ValueError("Missing input")

    elif "int" in type:
        if not input_.isdigit():
            raise ValueError("Not numeric")

        elif "menu" in type:
            if int(input_) < 1 or int(input_) > len(selection):
                raise ValueError("Not in option")

        elif "move" in type:
            if not input_.isdigit():
                raise ValueError("Not numeric")
            elif int(input_) < 1 or int(input_) > (len(selection) ** 2):
                raise ValueError("Not in option")

    elif "str" in type:
        if not input_.isalpha():
            raise ValueError("Not a letter")

def alert(error):
    init(autoreset=True)

    print(Fore.LIGHTRED_EX + Style.BRIGHT + f"Error : {error}\n")
