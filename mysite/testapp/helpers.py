from icecream import ic

class AccessResolver():
    _access_level = None

    def __init__(self, access_level):
        self._access_level = access_level
        ic(self._access_level)