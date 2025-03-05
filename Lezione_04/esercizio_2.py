def check_length(string):
    if len(string) == 10:
        print(f"{string} tiene 10 letras")
    elif len(string) > 10:
        print(f"{string} tiene mas de 10 letras")
    else:
        print(f"{string} tiene menos de 10 letras")

check_length("managgia la miseria")