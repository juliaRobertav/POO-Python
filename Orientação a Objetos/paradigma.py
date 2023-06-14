#properties

class Cliente:
    def __init__(self, nome):
        """_summary_

        Args:
            nome (_type_): _description_
        """
        self.__nome = nome
    @property
    def limite(self):
        return self.__limite

    #@limite.setter
