

def test():
    raise ValueError('value err')  # NameError('乌拉拉')


try:
    test()
except (NameError, ValueError) as e:
    print('nameerror', e)
except Exception as e:
    print(e.value)


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    def __init__(self, expression: str, message: str):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    def __init__(self, previous, next, message) -> None:
        self.previouse = previous
        self.next = next
        self.message = message
