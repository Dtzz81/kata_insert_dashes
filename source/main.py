def insert_dashes(num: int) -> str:
    num_to_str = str(num)


    for i in num_to_str:
        if int(i) % 2 == 1:
            if int(num_to_str[1]) % 2 == 1:
                if len(num_to_str) < 3:
                    return f"{i}-{num_to_str[1:]}"
                elif int(num_to_str[2]) % 2 == 1:
                    if len(num_to_str) < 4:
                        return f"{i}-{num_to_str[1]}-{num_to_str[2:]}"
                    elif int(num_to_str[3]) % 2 == 1:
                        return f"{i}-{num_to_str[1]}-{num_to_str[2]}-{num_to_str[3:]}"
                    else:
                        return f"{i}-{num_to_str[1]}-{num_to_str[2:]}"
                else:
                    return f"{i}-{num_to_str[1:]}"

        return num_to_str

insert_dashes(202579)
