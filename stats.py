def get_book_text(path):
    with open(path) as f:
        txt = f.read()
    return txt


def count_characters(txt):
    counted: dict[str, int] = {}
    for temp in txt:
        if temp.lower() in counted:
            counted[temp.lower()] += 1
        else:
            counted[temp.lower()] = 1
    return counted


def helper(dict):  # for sort() to use the frequency as the key
    return dict["num"]


def sort_count(counted):
    dictlist = []
    for char in counted:
        # print(f"char: {char}, num: {counted[char]}")
        if char.isalpha():  # check if it's a letter
            dictlist.append(
                {"char": char, "num": counted[char]}
            )  # add its dictionary to the list
    dictlist.sort(reverse=True, key=helper)
    # calls helper with the current index element it's sorting, doesn't need a variable or anything
    return dictlist
