def insert_dashes(num: int) -> str:
    num_to_str = str(num)

    for i in num_to_str:
        if int(i) % 2 == 1:
            return f"{i}-{num_to_str[1]}"

        return num_to_str


    #return num_to_str[i] + - num_to_str[;i +1]

insert_dashes(202579)


#E   TypeError: 'int' object is not subscriptable

#if 7 %2 == 1 and 9 % 2 == 1:
        #     return "7-9"
        # if int(num_to_str[i]) % 2 == 1 and int(num_to_str[i + 1]) % 2 == 1:
        #     pass
