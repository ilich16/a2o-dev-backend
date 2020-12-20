from typing import Dict, List

class Game:
    """
    A class used to represent a Padel game

    ...

    Attributes
    ----------
    home_team : str
        the name of the home team
    home_team_score : int
        the score of the home team
    away_team: str
        the name of the away team
    away_team_score : int
        the socre of the away team

    """

    def __init__(self, home_team: str, home_team_score: int, away_team: str, away_team_score: int):
        """
        Parameters
        ----------
        home_team : str
            the name of the home team
        home_team_score : int
            the score of the home team
        away_team: str
            the name of the away team
        away_team_score : int
            the socre of the away team

        """
        self.home_team = home_team
        self.home_team_score = home_team_score
        self.away_team = away_team
        self.away_team_score = away_team_score

class Category:
    """
    A class used to represent a category in a Padel league

    ...

    Attributes
    ----------
    title : str
        the title of the category
    games : List[Game]
        a list of all games played in that category
    teams : List[str]
        a list with all participing teams in that category

    """

    def __init__(self, title: str, games: List[Game], teams: List[str]):
        """
        Parameters
        ----------
        title : str
            the title of the category
        games : List[Game]
            a list of all games played in that category
        teams : List[str]
            a list with all participing teams in that category

        """
        self.title = title
        self.games = games
        self.teams = teams

class FirstProblem:
    """
    A class used to represent the first problem in the project

    ...

    Attributes
    ----------
    user_input : str
        the user input text for the first problem

    Methods
    -------
    get_answer() -> List[str]
        Get the answer of the problem

    """

    def __init__(self, user_input: str):
        """
        Parameters
        ----------
        user_input : str
            The user input text of the problem

        """
        self.user_input = user_input

    def get_answer(self) -> List[str]:
        """
        Get the answer for the first problem

        Returns
        -------
        List[str]
            a list where each item is the name of the winner and
            the number of missing games of each category 

        """
        categories = get_categories(self.user_input)
        answer: str = []
        for category in categories:
            standings = get_category_standings(category)
            highest_score = get_highest_score(standings, category.teams)
            winner = get_winner(standings, highest_score)
            missing_games = get_missing_games(category)
            # Format each item for add to answer list
            answer.append(f'{winner} {missing_games}')
        
        return answer

def get_categories(user_input: str) -> List[Category]:
    """
    Get the categories from the user input text

    Parameters
    ----------
    user_input : str
        the user input text of the problem
    
    Returns
    -------
    List[Category]
        a list with all the existing categories extracted from
        the user input text

    """
    categories: List[Category] = []
    # Get a list of categories
    categories_list = user_input.split('FIN')
    # The last item is empty, so remove it
    categories_list.pop()
    # Iterate over the list of categories
    for item in categories_list:
        # Get a list of each line
        item = item.split('\n')
        # Remove each empty item from the list
        item = list(filter(None, item))
        games = []
        # The first element is the title of category. So iterate from
        # the second element of the list
        for game in item[1:]:
            # Remove spaces at the beginning and the end
            game = game.strip()
            # Get a list with the teams and their scores
            game_details = game.split(' ')
            # Create a game object to save data about the game 
            new_game = Game(game_details[0], int(game_details[1]), game_details[2], int(game_details[3]))
            games.append(new_game)
        teams: List[str] = []
        # Iterate over all games
        for game in games:
            # Get all participating teams and save them
            if game.home_team not in teams:
                teams.append(game.home_team)
            if game.away_team not in teams:
                teams.append(game.away_team)
        
        # Create a category with a title, games and teams
        category = Category(item[0], games, teams)
        categories.append(category)
    
    return categories

def get_category_standings(category: Category) -> Dict[str, int]:
    """
    Get the standings of a category

    Parameters
    ----------
    category : Category
        the category to get its standings

    Returns
    -------
    Dict[str, int]
        a dictionary where each data value is the name of the
        team with its points

    """
    standings: Dict[str, int] = {}
    # Iterate over all teams to get the everyteam's points
    for team in category.teams:
        points = 0
        # Iterate over all games of a category to check each team
        for game in category.games:
            if game.home_team == team or game.away_team == team:
                # Check if the team won or lost
                if game.home_team == team:
                    if game.home_team_score > game.away_team_score:
                        points += 2
                    else:
                        points += 1
                if game.away_team == team:
                    if game.away_team_score > game.home_team_score:
                        points += 2
                    else:
                        points += 1
        # Save the points of the team
        standings[team] = points
    
    return standings

def get_highest_score(standings: Dict[str, int], teams: List[str]) -> int:
    """
    Get the highest score of the standings

    Parameters
    ----------
    standings : Dict[str, int]
        the standings to get its highest score
    
    teams : List[str]
        the list of participating teams

    Returns
    -------
    int
        a int that represents the highest score in the standings

    """
    highest_score = 0
    # Iterate over all teams
    for team in teams:
        # Compare the values
        if standings[team] > highest_score:
            highest_score = standings[team]

    return highest_score

def get_winner(standings: Dict[str, int], highest_score: int) -> str:
    """
    Get the name of the winner based on the standings

    Parameters
    ----------
    standings : Dict[str, int]
        the standings to get the name of the winner

    highest_score : int
        the highest score in the standings

    Returns
    -------
    str
        the name of the winner 
    """
    winner = ""
    highest_score_frecuency = 0
    # Iterate over each team with its score
    for team, score in standings.items():
        # Compare the highest score for save the team's name
        if highest_score == score:
            winner = team
            # Save the frecuency of the highest score to check if there is
            # more than one team with the highest score
            highest_score_frecuency += 1
    # If the frecuency is more than one, return 'EMPATE'
    if highest_score_frecuency > 1:
        winner = "EMPATE"

    return winner

def get_missing_games(category: Category) -> int:
    """
    Get the number of missing games in a category

    Parameters
    ----------
    category : Category
        the category from which the missing games will be obtained
    
    Returns
    -------
    int
        the number of missing games
    
    """
    # Get the total games that have to be played
    total_games = len(category.teams) * (len(category.teams) - 1)
    # Get the difference between the games played in the games to be played
    missing_games = total_games - len(category.games)

    return missing_games