class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        return self.__genre_name == other.__genre_name

    def __lt__(self, other):
        if not isinstance(self, Genre) or not isinstance(other, Genre):
            return False
        if self.__genre_name < other.__genre_name:
            return True
        return False

    def __hash__(self):
        return hash(self.__genre_name)