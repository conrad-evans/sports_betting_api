import re
from typing import Dict, Set


class Validator:
    def __init__(self, data: Dict) -> None:
        self.data = data
        self.errors_dict = dict()

    def _checkValueInErrors(self) -> bool:
        """
        checks if `self.value` is in already in the errors dictionary

        Returns:
            `bool` -> `True` if value exists in dictionary else `False`
        """
        return True if self.value in self.errors_dict else False

    def checkAll(self, values: list):
        """
        Iterates through a list to check if all values are in the data provided

        Args:
            `values: (list) -> Keys in data object passed in class initialization

        Returns:
            `Validation` instance of the validation class
        """
        values = set(values)
        for value in values:
            self.check(value)
        return self

    def check(self, value: str, message: str = None):
        """
        checks if the value supplied has a value

        Args:
            `value: (str)`  -> Key in data object passed when initializing the class

        Returns:
            `bool` -> `True` if value exists for the key else `False`
        """
        self.value = value
        if (type(self.data) != dict) or (not self.data.get(self.value)):
            if message:
                self.errors_dict[self.value] = message
            else:
                self.errors_dict[self.value] = f'{self.value} is required'
        return self

    def isEmail(self) -> bool:
        """
        checks if a string is a valid email

        Args:
            `email: (str)` -> String to be checked
        """
        EMAIL_REGEX = R'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if not self._checkValueInErrors():
            if not (re.search(EMAIL_REGEX, self.data[self.value])):
                self.errors_dict[self.value] = f'{self.data[self.value]} is not a valid email'
        return self

    def length(self, minimum: int, maximum: int) -> bool:
        """
        checks if the value is between specificed values

        Args:
            `minimum: int` -> the minimum amount of characters expected
            `maximum: int` -> the maximum amount of characters expected
        """
        if not self._checkValueInErrors():
            if not (minimum <= len(self.data[self.value]) <= maximum):
                self.errors_dict[self.value] = f'{self.value} should be between {minimum} and {maximum} characters'
        return self

    def errors(self) -> Dict:
        """
        returns the dictionary object with errors

        Returns:
            `dict` with key-values of errors and message
        """
        return self.errors_dict
