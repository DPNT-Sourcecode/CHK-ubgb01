# noinspection PyUnusedLocal
# friend_name = unicode string


def hello(friend_name):
    """
    Return string with message.

    param friend_name: a String.
    @return: a String containing a message.
    """
    if not (isinstance(friend_name, str)):
        return 'Please enter a string only.'
    if not (friend_name.isalpha()):
        return 'Please enter a string with Alphabetic characters only'
    return "Hello, {}".format(friend_name)
