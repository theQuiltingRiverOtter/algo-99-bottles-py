def bottle_song(num: int = 99, drink: str = "beer") -> None:
    upper_limit = num

    for i in range(num, -1, -1):
        btl_txt = "bottles" if i - 1 > 1 else "bottle"
        if i == 0:
            print(
                f"No more bottles of {drink} on the wall, no more bottles of {drink}."
            )
            print(
                f"Go to the store and buy some more, {upper_limit} bottles of {drink} on the wall."
            )

        elif i == 1:
            print(f"{num} bottle of {drink} on the wall, {num} bottle of {drink}.")
            print(
                f"Take one down and pass it around, no more bottles of {drink} on the wall."
            )
        else:
            print(f"{num} bottles of {drink} on the wall, {num} bottles of {drink}.")
            print(
                f"Take one down and pass it around, {num-1} {btl_txt} of {drink} on the wall."
            )
        num -= 1


def bottle_song_recursive(
    num: int = 99, drink: str = "beer", upper_limit: int = 99
) -> None:
    if num == 0:
        print(f"No more bottles of {drink} on the wall, no more bottles of {drink}.")
        print(
            f"Go to the store and buy some more, {upper_limit} bottles of {drink} on the wall."
        )
    elif num == 1:
        print(f"{num} bottle of {drink} on the wall, {num} bottle of {drink}.")
        print(
            f"Take one down and pass it around, no more bottles of {drink} on the wall."
        )
        bottle_song_recursive(num - 1, drink, upper_limit)
    elif num == 2:
        print(f"{num} bottles of {drink} on the wall, {num} bottles of {drink}.")
        print(
            f"Take one down and pass it around, {num-1} bottle of {drink} on the wall."
        )
        bottle_song_recursive(num - 1, drink, upper_limit)
    else:
        print(f"{num} bottles of {drink} on the wall, {num} bottles of {drink}.")
        print(
            f"Take one down and pass it around, {num-1} bottles of {drink} on the wall."
        )
        bottle_song_recursive(num - 1, drink, upper_limit)


bottle_song_recursive()
