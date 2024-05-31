import string
import time

_BASE = 62


class HashDigest:
    """Base base 62 hash library."""

    def __init__(self):
        self.base = string.ascii_letters + string.digits
        self.short_str = ''

    def encode(self, j):
        """Returns the repeated div mod of the number.
        :param j: int
        :return: list
        """
        if j == 0:
            return [j]
        r = []
        dividend = j
        while dividend > 0:
            dividend, remainder = divmod(dividend, _BASE)
            r.append(remainder)
        r = list(reversed(r))
        return r

    def shorten(self, i):
        """
        :param i:
        :return: str
        """
        self.short_str = ""
        encoded_list = self.encode(i)
        for val in encoded_list:
            self.short_str += self.base[val]
        return self.short_str
