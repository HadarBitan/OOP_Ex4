import sys

import pygame as pg
from pygame import *
# from pygame import font
from src.GUI.ui_elements import Button

# from client_python.student_code import screen
from src.Graph.GraphAlgo import GraphAlgo


WIDTH, HEIGHT = 1080, 720
pg.font.init()
FONT = pg.font.SysFont("Ariel", 20, bold=True)


def draw_Frame(graph: GraphAlgo):
    pg.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit(0)
        screen.fill(Color(40, 80, 100))
        draw_graph(graph, screen=screen)
        # display.update()
        clock.tick(60)
        pg.display.flip()
    pg.quit()
    sys.exit()


def draw_graph(graph: GraphAlgo, screen):
    """
        This function draw only the graph
    """
    list_of_nodes: {int: tuple} = {}
    for node in graph.get_graph().get_all_v().keys():
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
        x = my_scale(list_of_nodes[node][0], min_x, max_x, min_y, max_y, x=True, screen=screen)
        y = my_scale(list_of_nodes[node][1], min_x, max_x, min_y, max_y, y=True, screen=screen)
        pg.draw.circle(screen, pg.Color(235, 125, 87), (x, y), radius=12)
        id_srf = FONT.render(str(node), True, pg.Color(0, 0, 0))
        id_rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, id_rect)

    #drawing the edges of the graph
    for src in graph.get_graph().get_all_src_dict():
        src_x = my_scale(list_of_nodes[src][0], min_x, max_x, min_y, max_y, screen=screen, x=True)
        src_y = my_scale(list_of_nodes[src][1], min_x, max_x, min_y, max_y, screen=screen, y=True)
        for dest in graph.get_graph().get_all_src_dict()[src].keys():
        # dest = graph.get_graph().get_all_src_dict()[src]
            dx = list_of_nodes.get(dest)[0]
            dy = list_of_nodes.get(dest)[1]
            dest_x = my_scale(dx, min_x, max_x, min_y, max_y, screen=screen, x=True)
            dest_y = my_scale(dy, min_x, max_x, min_y, max_y, screen=screen, y=True)
            pg.draw.line(screen, pg.Color(0, 0,0), (src_x, src_y), (dest_x, dest_y))


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen


def my_scale(data, min_x, max_x, min_y, max_y, screen, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)

if __name__ == '__main__':
    graph = GraphAlgo()
    graph.load_from_json("C:\\Users\hadar\PycharmProjects\Ex4\data\A0")
    draw_Frame(graph)