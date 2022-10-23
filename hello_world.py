""" Made by Ampiro"""


def text_generator():
    """ Text generator """
    text = "Lorem ipsum dolor sit amet , consectetur adipiscing elit"
    for word in text.split():
        yield word


def fast_forward_function():
    """
    This function has description only because
    pylint made me do this
    make mess
    in
    master
    """
    text = "Are there any reasons to live except to gain knowledge?"
    return text

# removing


def function_two():
    """ Returning one """
    return 2


# more removes


if __name__ == "__main__":
    print(list(text_generator()))
    print("Make conflicts great again")
    print(list(text_generator()))
    print(list(text_generator()))
    print(list(text_generator()))
