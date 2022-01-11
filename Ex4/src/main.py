"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import time as sleeper
from types import SimpleNamespace
from client import Client
import json
from pygame import gfxdraw
import pygame
import random
from Graph.GraphAlgo import GraphAlgo
from pygame import *
from algorithms import *
import time as t


# init pygame
WIDTH, HEIGHT = 1000, 600

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'

pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)

pokemons = client.get_pokemons()
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))

graph_json = client.get_graph()
algo = GraphAlgo()
algo.load_from_json(graph_json)

FONT = pygame.font.SysFont('Arial', 20, bold=True)

# load the json string into SimpleNamespace Object
graph = json.loads(
    graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

for n in graph.Nodes:
    x, y, _ = n.pos.split(',')
    n.pos = SimpleNamespace(x=float(x), y=float(y))

# get data proportions
min_x = min(list(graph.Nodes), key=lambda node: node.pos.x).pos.x
min_y = min(list(graph.Nodes), key=lambda node: node.pos.y).pos.y
max_x = max(list(graph.Nodes), key=lambda node: node.pos.x).pos.x
max_y = max(list(graph.Nodes), key=lambda node: node.pos.y).pos.y


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values
def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


radius = 15
poke_data = {}
agents_num = int(json.loads(client.get_info()).get("GameServer").get("agents"))
nodes_num = len(algo.get_graph().get_all_v())
for i in range(agents_num):
    client.add_agent("{\"id\":" + str(random.randint(0, nodes_num)) + "}")

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""

background = pygame.image.load('../img/background.jpg')
background = pygame.transform.scale(background, (WIDTH * 1.3, HEIGHT * 1.3))

ash = pygame.image.load('../img/ash.jpg')
ash = pygame.transform.scale(ash, (50, 50))

bulbasaur = pygame.image.load('../img/bulbasaur.jpg')
bulbasaur = pygame.transform.scale(bulbasaur, (50, 50))

jigglupuff = pygame.image.load('../img/jigglupuff.jpg')
jigglupuff = pygame.transform.scale(jigglupuff, (50, 50))

pikachu = pygame.image.load('../img/pikachu.jpg')
pikachu = pygame.transform.scale(pikachu, (50, 50))

squirtle = pygame.image.load('../img/squirtle.jpg')
squirtle = pygame.transform.scale(squirtle, (50, 50))
pokepics = [pikachu, bulbasaur, jigglupuff, squirtle]
score = 0

# this commnad starts the server - the game is running now
open_game(pygame=pygame, screen=screen, sleeper=sleeper, FONT=FONT, client=client)
while client.is_running() == 'true':
    pokemons = json.loads(client.get_pokemons(),
                          object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokemons = [p.Pokemon for p in pokemons]
    i = 0
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        poke_data[i] = (x, y, p.type)
        p.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
        i = i + 1
    agents = json.loads(client.get_agents(),
                        object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(
            float(x), x=True), y=my_scale(float(y), y=True))
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over(score, pygame=pygame, screen=screen, FONT=FONT, sleeper=sleeper, client=client)

    # refresh surface
    screen.fill(Color(0, 0, 0))
    screen.blit(background, (0, 0))

    # collect data to show on screen
    info = json.loads(client.get_info()).get("GameServer")
    score = info["grade"]
    moves = info["moves"]
    ttl = int(Decimal(client.time_to_end()) / 1000)

    # print lables
    scorelabel = FONT.render(f"Score: {score}", True, (50, 50, 50))
    rect = scorelabel.get_rect(center=(200, 10))
    screen.blit(scorelabel, rect)

    timelabel = FONT.render(f"Time Left: {int(ttl)}", True, (50, 50, 50))
    rect = timelabel.get_rect(center=(70, 10))
    screen.blit(timelabel, rect)

    moveslabel = FONT.render(f"Moves: {moves}", True, (50, 50, 50))
    rect = moveslabel.get_rect(center=(300, 10))
    screen.blit(moveslabel, rect)

    # draw edges
    for e in graph.Edges:
        # find the edge nodes
        src = next(n for n in graph.Nodes if n.id == e.src)
        dest = next(n for n in graph.Nodes if n.id == e.dest)

        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, Color(61, 72, 126),
                         (src_x, src_y), (dest_x, dest_y))

        # draw nodes
        for n in graph.Nodes:
            x = my_scale(n.pos.x, x=True)
            y = my_scale(n.pos.y, y=True)

            # its just to get a nice antialiased circle
            gfxdraw.filled_circle(screen, int(x), int(y),
                                  radius, Color(64, 80, 174))
            gfxdraw.aacircle(screen, int(x), int(y),
                             radius, Color(255, 255, 255))

            # draw the node id
            id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)

    # draw agents
    for agent in agents:
        screen.blit(ash, (int(agent.pos.x), int(agent.pos.y)))

    # draw pokemons
    i = 0
    poksize = len(pokemons)
    for p in pokemons:
        screen.blit(pokepics[i % 4], (int(p.pos.x), int(p.pos.y)))
        i += 1

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    choose_next_node(agents=agents, pokemons=pokemons, poke_data=poke_data, graph=graph,algo=algo, client=client)
    sleeper.sleep(0.09)
    client.move()
    t.sleep(0.1)

# game over:
game_over(score, pygame=pygame, screen=screen, FONT=FONT, sleeper=sleeper, client=client)
# print(client.get_info())
# if __name__ == '__main__':

