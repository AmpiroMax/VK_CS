""" Made by Ampiro"""


def text_generator():
    """ Text generator """
    text = "Lorem ipsum dolor sit amet"
    for word in text.split():
        yield word


def fast_forward_function():
    """
    This function has description only because
    pylint made me do this
    """
    text = "Are there any reasons to live except to gain knowledge?"
    return text


if __name__ == "__main__":
    print(list(text_generator()))
