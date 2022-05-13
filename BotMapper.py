class BotMapper:
    __position_x = 0
    __position_y = 0
    __charge = 0.0
    __weight = 0.0
    __speed = 0.0
    __tiredness = 0.0
    __rang = 0.0
    __damage = 0.0
    __game_field = [[]]

    def __init__(self, charge: float, weight: float, speed: float, tiredness: float, damage: float, rang: float,
                 position_x: int, position_y: int, game_field):
        self.__game_field = game_field
        self.__charge = charge
        self.__weight = weight
        self.__tiredness = tiredness
        self.__speed = speed
        self.__rang = rang
        self.__damage = damage
        self.__position_y = position_y
        self.__position_x = position_x

    def get_tiredness(self):
        return self.__tiredness

    def set_tiredness(self, tiredness):
        self.__tiredness = tiredness

    def get_charge(self):
        return self.__charge

    def get_speed(self):
        return self.__speed

    def get_weight(self):
        return self.__weight

    def get_range(self):
        return self.__rang

    def get_damage(self):
        return self.__damage

    def get_position_x(self):
        return self.__position_x

    def get_position_y(self):
        return self.__position_y

    def set_position_xy(self, position_x: int, position_y: int):
        self.__position_x = position_x
        self.__position_y = position_y


