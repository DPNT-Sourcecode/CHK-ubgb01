# noinspection PyUnusedLocal
# friend_name = unicode string


def hello(friend_name):
    """
    Return string with message.

    param friend_name: a String.
    @return: a String containing a message.
    """
    if not (isinstance(friend_name, unicode)):
        return 'Please enter a string only.'
    return "Hello, {}".format('World!')
