""" Made by Ampiro"""


def text_generator():
    """ Text generator """
    text = "Lorem ipsum dolor sit amet"
    for word in text.split():
        yield word


if __name__ == "__main__":
    print(list(text_generator()))
