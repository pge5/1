from random import gauss

from Bot import Bot


class Game:
    r = 0

    bot1: Bot
    bot2: Bot
    game_field: [[]]

    def __init__(self, bot1: Bot, bot2: Bot):
        self.bot1 = bot1
        self.bot2 = bot2

    # 1-bot1 winner, 2-bot2 winner, 0-draw
    def start(self):
        while self.r < 60:
            step = self.bot1.consider_step(self.game_field)

            if step[0] == "attack":
                res = self.attack(self.bot1, self.bot2, 1, step[1], step[2])
            elif step[0] == "move":
                res = self.move(self.bot1, step[1], step[2])
            else:
                res = 0

            if res == 2:
                return 1

            step = self.bot2.consider_step(self.game_field)

            if step[0] == "attack":
                res = self.attack(self.bot2, self.bot1, 2, step[1], step[2])
            elif step[0] == "move":
                res = self.move(self.bot2, step[1], step[2])
            else:
                res = 0

            if res == 2:
                return 2

            self.r += 1
        return 0

    # -1 - error, 1- hit, 2 - kill, 0 - miss
    def attack(self, bot: Bot, attacked_bot: Bot, bot_n: int, x: int, y: int):
        range_of_attack = abs(bot.get_position_x()) - abs(x) + abs(bot.get_position_y()) - abs(y)
        if bot.get_range() < range_of_attack | x < 0 | y < 0 | len(self.game_field) < x | len(self.game_field[x]) < y:
            return -1
        else:
            if (bot_n == 1 & self.game_field[x, y] == 2) | (bot_n == 2 & self.game_field[x, y] == 1):
                dmg = gauss(bot.get_damage(), 25)
                hp = attacked_bot.get_tiredness() - dmg
                if hp <= 0:
                    return 2
                attacked_bot.set_tiredness(hp)
                return 1
            else:
                return 0

    def move(self, bot: Bot, x: int, y: int):
        range_of_move = abs(bot.get_position_x()) - abs(x) + abs(bot.get_position_y()) - abs(y)
        if self.game_field[x, y] != 0 & range_of_move < bot.get_speed() | len(self.game_field) < x | len(self.game_field[x]) < y:
            return -1
        else:
            bot.set_position_xy(x, y)
            return 1
