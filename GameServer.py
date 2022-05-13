import string
from random import gauss

from Bot import Bot
from BotMapper import BotMapper


class GameServer:
    r = 0

    __fight_map = ""

    bot1: Bot
    bot2: Bot
    bot_stats1: BotMapper
    bot_stats2: BotMapper
    game_field: [[]]

    def __init__(self, bot1: str, bot2: str, bot_stats1: BotMapper, bot_stats2: BotMapper, game_field: []):
        self.game_field = game_field

        bot1 += "\n" + "self.bot1 = Bot(game_field)"
        bot2 += "\n" + "self.bot2 = Bot(game_field)"
        exec(bot1)
        exec(bot2)

        self.bot_stats1 = bot_stats1
        self.bot_stats2 = bot_stats2

    # 1-bot1 winner, 2-bot2 winner, 0-draw
    def start(self):
        while self.r < 60:
            step = self.bot1.consider_step(self.game_field)

            if step[0] == "attack":
                res = self.attack(self.bot_stats1, self.bot_stats2, 1, step[1], step[2])
                self.__fight_map += "1," + "attack," + str(step[1]) +"," + str(step[2]) + ";"

            elif step[0] == "move":
                res = self.attack(self.bot_stats1, self.bot_stats2, 1, step[1], step[2])
                self.__fight_map += "1," + "move," + str(step[1]) + "," + str(step[2]) + ";"
            else:
                res = 0

            if res == 2:
                self.__fight_map += "1," + "kill," + str(step[1]) + "," + str(step[2]) + ";"
                return [1, self.__fight_map]

            step = self.bot2.consider_step(self.game_field)

            if step[0] == "attack":
                res = self.attack(self.bot_stats2, self.bot_stats1, 2, step[1], step[2])
                self.__fight_map += "2," + "attack," + str(step[1]) + "," + str(step[2]) + ";"

            elif step[0] == "move":
                res = self.attack(self.bot_stats2, self.bot_stats1, 2, step[1], step[2])
                self.__fight_map += "2," + "move," + str(step[1]) + "," + str(step[2]) + ";"
            else:
                res = 0

            if res == 2:
                self.__fight_map += "1," + "kill," + str(step[1]) + "," + str(step[2]) + ";"
                return [2, self.__fight_map]

            self.r += 1
        return 0

    # -1 - error, 1- hit, 2 - kill, 0 - miss
    def attack(self, bot: BotMapper, attacked_bot: BotMapper, bot_n: int, x: int, y: int):
        range_of_attack = abs(bot.get_position_x()) - abs(x) + abs(bot.get_position_y()) - abs(y)
        print(str(bot_n) + " " + str(x) + " " + str(y) + str(self.game_field[0][2]) + ";")
        if bot.get_range() < range_of_attack | x < 0 | y < 0:
            return -1
        else:
            if (bot_n == 1 and self.game_field[x][y] == 2) | (bot_n == 2 and self.game_field[x][y] == 1):
                dmg = gauss(bot.get_damage(), 25)
                hp = attacked_bot.get_tiredness() - dmg
                if hp <= 0:
                    return 2
                attacked_bot.set_tiredness(hp)
                return 1
            else:
                return 0

    # -1 - error, 1 - move
    def move(self, bot: BotMapper, x: int, y: int):
        range_of_move = abs(bot.get_position_x()) - abs(x) + abs(bot.get_position_y()) - abs(y)
        if self.game_field[x][y] == 0 and range_of_move < bot.get_speed():
            bot.set_position_xy(x, y)
            return 1
        else:
            return -1
