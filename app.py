from flask import Flask, request, jsonify
from flask_restful import Api, Resource

from BotMapper import BotMapper
from GameServer import GameServer

app = Flask(__name__)
api = Api(app)

array = []


class Fight(Resource):
    def post(self):
        return self.start_game_by_json(request.get_json())

    def start_game_by_json(self, req):
        field = self.get_int_field((req['arena'])['field'])
        temp_pos = self.get_position_for(field, 1)

        temp = req['robot1']
        bot_stat1 = BotMapper(temp['charge'], temp['weight'], temp['speed'],
                              temp['tiredness'], temp['damage'], temp['range'],
                              temp_pos[0], temp_pos[1], field)
        bot1_string = (temp['botAlgorithm'])['algorithm']

        temp_pos = self.get_position_for(field, 2)
        temp = req['robot2']
        bot_stat2 = BotMapper(temp['charge'], temp['weight'], temp['speed'],
                              temp['tiredness'], temp['damage'],
                              temp['range'], temp_pos[0], temp_pos[1], field)
        bot2_string = (temp['botAlgorithm'])['algorithm']

        game = GameServer(bot1_string, bot2_string, bot_stat1, bot_stat2, field)
        res = game.start()

        return jsonify(
            {"winner": res[0], "fight_map": res[1]}
        )


    def get_position_for(self, field, t: int):
        for x in range(len(field)):
            for y in range(len(field[x])):
                if field[x][y] == t:
                    return [x, y]

    def get_int_field(self, field):
        temp_field = field.split("\n")
        f_res = []
        for x in range(len(temp_field)):
            list = []
            for y in temp_field[x]:
                if y == '0':
                    list.append(0)
                elif y == '1':
                    list.append(1)
                elif y == '2':
                    list.append(2)
            f_res.append(list)

        print(f_res)
        return f_res


api.add_resource(Fight, '/fight/')
