import pygame as pg
from pygame import gfxdraw
from pygame import *
# from pygame import font

# from client_python.student_code import screen
from src.Graph.GraphAlgo import GraphAlgo

WIDTH, HEIGHT = 1080, 720
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
FONT = pg.font.SysFont("Ariel", 20, bold=True)


def run(agents, pokemons, graph):
    pg.init()
    clock = pg.time.Clock()
    pg.font.init()
    screen.fill(Color(40, 80, 100))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
        draw_agent(agents)
        draw_pokemon(pokemons)
        draw_graph(graph)
        display.update()
        clock.tick(60)


def draw_agent(agents):
    """
        This function responsible only to draw the agents
    """
    for agent in agents:
        pg.draw.circle(screen, Color(122, 61, 23), (int(agent.get_pos()[0]), int(agent.get_pos()[1])), 10)


def draw_pokemon(pokemons):
    """
        This function responsible only to draw the pokemons
    """
    for p in pokemons:
        pg.draw.circle(screen, Color(0, 255, 255), (int(p.get_pos()[0]), int(p.get_pos()[1])), 10)


def draw_graph(graph: GraphAlgo):
    """
        This function draw only the graph
    """
    list_of_nodes: {int: tuple} = {}
    for node in graph.get_graph().get_all_v():
        list_of_nodes[node] = graph.get_graph().get_all_v()[node].get_location()
    list_of_x = []
    list_of_y = []
    for pos in list_of_nodes.values():
        list_of_y.append(pos[1])
        list_of_x.append(pos[0])
    min_x = min(list(list_of_x))
    min_y = min(list(list_of_y))
    max_x = max(list(list_of_x))
    max_y = max(list(list_of_y))

    #drawin the nodes of the graph
    for node in list_of_nodes:
        x = my_scale(list_of_nodes[node][0], min_x, max_x, min_y, max_y, x=True)
        y = my_scale(list_of_nodes[node][1], min_x, max_x, min_y, max_y, y=True)
        pg.draw.circle(screen, pg.Color(235, 125, 87), (x, y), radius=5)
        id_srf = FONT.render(str(node), True, pg.Color(0, 0, 0))
        id_rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, id_rect)

    #drawin the edges of the graph
    for src in graph.get_graph().get_all_src_dict():
        src_x = my_scale(list_of_nodes[src][0], min_x, max_x, min_y, max_y, x=True)
        src_y = my_scale(list_of_nodes[src][1], min_x, max_x, min_y, max_y, y=True)
        dest = graph.get_graph().get_all_src_dict()[src]
        dest_x = my_scale(list_of_nodes[dest][0], min_x, max_x, min_y, max_y, x=True)
        dest_y = my_scale(list_of_nodes[dest][1], min_x, max_x, min_y, max_y, y=True)
        pg.draw.line(screen, pg.Color(0, 0,0), (src_x, src_y), (dest_x, dest_y))


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen


def my_scale(data, min_x, max_x, min_y, max_y, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)
