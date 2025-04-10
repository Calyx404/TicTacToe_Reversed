from colorama import init, Fore, Style

def validate(input_:str, type:str, **kwargs) -> None:
    selection = kwargs.get('selection')
    occupied = kwargs.get('occupied', [])

    if not input_:
        raise ValueError("Missing input")

    if "int" in type:
        if not input_.isdigit():
            raise ValueError("Not numeric")

        num = int(input_)

        if "menu" in type:
            if not selection or num < 1 or num > len(selection):
                raise ValueError("Not in option")

        if "move" in type:
            if not selection or num < 1 or num > (len(selection) ** 2):
                raise ValueError("Move not it range")
            if num in occupied:
                raise ValueError("Cell already occupied")

    if "str" in type:
        if not input_.isalpha():
            raise ValueError("Only letters are allowed")

        if "limit" in type:
            if len(input_) > 10:
                raise ValueError("Maximum of 10 characters only")

def alert(error) -> None:
    init(autoreset=True)

    print(Fore.LIGHTRED_EX + Style.BRIGHT + f"Error : {error}\n")
