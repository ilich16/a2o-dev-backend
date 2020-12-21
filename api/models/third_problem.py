from typing import List

class ThirdProblem:
    """
    A class used to represent the third problem in the project

    ...

    Attributes
    ----------
    user_input : str
        the user input text for the third problem

    Methods
    -------
    get_answer() -> int
        get the answer of the problem

    """

    def __init__(self, user_input: str):
        """
        Parameters
        ----------
        user_input : str
            the user input text of the problem

        """
        self.user_input = user_input

    def get_answer(self) -> int:
        """
        Get the answer for the third problem

        Returns
        -------
        int
            an int that represents the maximum value of a word

        """
        word = self.user_input
        # Get substrings from a word
        substrings = get_substrings(word)

        return get_max_value(word, substrings)

def get_substrings(word: str) -> List[str]:
    """
    Get substrings from a word

    Parameters
    ----------
    word : str
        the word from which substrings are to be extracted

    Returns
    -------
    List[str]
        a list with all substrings of a word

    """
    substrings: List[str] = []
    # Iterate 'over' the word
    for i in range(1, len(word) + 1):
        for j in range(len(word)):
            k = j + i
            if k > len(word):
                break
            # Get each substring
            substring = word[j:k]
            # Append substring just one time
            if substring not in substrings:
                substrings.append(substring)
    
    return substrings

def get_max_value(word: str, substrings: List[str]) -> int:
    """
    Get the max value from a list of substrings of a word

    Parameters
    ----------
    word : str
        the word to check each substring
    
    substrings : List[str]
        list of substring to check the ocurrences in a word

    Returns
    -------
    int
        return the max value of the substrings. Each value is calculated
        with the next function:
            s -> substring
            f(s) = |s| * Number of times s occurs in word

    """
    max_value = 0
    # Iterate over all substrings
    for substring in substrings:
        ocurrences = get_ocurrences(word, substring)
        # Calculate the value of each substring
        value = len(substring) * ocurrences
        # Compare values
        if value > max_value:
            max_value = value
    
    return max_value

def get_ocurrences(word: str, substring: str) -> int:
    """
    Get the number of ocurrences of a substring in a word

    Parameters
    ----------
    word : str
        the word from where get the number of ocurrences
    
    substring : str
        the substring for find ocurrences in a word

    Returns
    -------
    int
        an int that represents the number of ocurrences of a substring
        in a word

    """
    ocurrences = 0
    start = 0
    while True:
        # Find ocurrence in a word given a start
        index = word.find(substring, start)
        if index != -1:
            ocurrences += 1
            start = index + 1
        else:
            return ocurrences