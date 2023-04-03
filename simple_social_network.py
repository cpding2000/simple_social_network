"""A simple social netwrok for tracking connections between people"""


class Person:
    """A Person in the social network.
    
    Attributes:
        name(str): the persons name.
        connnections(set of person): other people in the social network
        who know this person"""