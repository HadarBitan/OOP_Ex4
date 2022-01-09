import pygame
from pygame import RESIZABLE, Color
from src.GUI.ui_elements import Button
from src.Graph.GraphAlgo import GraphAlgo


WIDTH, HEIGHT = 1080, 800
pygame.font.init()
FONT = pygame.font.SysFont("Ariel", 20)
FONT_ele = pygame.font.SysFont("arial.ttf", 25)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
screen.fill(pygame.Color(40, 80, 100))
backg = pygame.image.load("C:\\Users\hadar\OneDrive - Ariel University\Desktop\Ex4\img\\background.jpg")
backg = pygame.transform.scale(backg, (screen.get_width(), screen.get_height()))
screen.blit(backg, (0, 0))


def draw_Frame(graph: GraphAlgo, moves, points, time, agents, pokemons):
    """
    The function drawing the basic frame, aka the graph and the stop button
    those items don't change the entire game.
    :param graph:
    :return:
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            _draw_graph(graph)
            draw_button("STOP")
            draw_moves(moves)
            draw_points(points)
            draw_time_to_end(time)
            draw_agent(agents)
            draw_pokemon(pokemons)
            clock.tick(60)
            pygame.display.flip()
            backg = pygame.image.load("C:\\Users\hadar\OneDrive - Ariel University\Desktop\Ex4\img\\background.jpg")
            backg = pygame.transform.scale(backg, (screen.get_width(), screen.get_height()))
            screen.blit(backg, (0, 0))


def draw_button(title: str):
    """
        This function responsible to draw the stop button
    """
    button = Button(title, (60, 30), (234, 16, 6))
    button.render(screen, (190, 5))
    button.add_click_listener(func_button)
    button.check()


def func_button():
    """
    The function stops the pygame window, this function is build to the stop button
    :return:
    """
    pygame.quit()
    exit(0)


def draw_points(points):
    """
        This function responsible only to draw the overall points
    """
    point_srf = FONT_ele.render("Overall Points = " + str(points), True, pygame.Color(0, 0, 0))
    point_rect = point_srf.get_rect(center=(90, 20))
    screen.blit(point_srf, point_rect)


def draw_moves(moves):
    """
        This function responsible only to draw the overall points
    """
    point_srf = FONT_ele.render("moves = " + str(moves), True, pygame.Color(0, 0, 0))
    point_rect = point_srf.get_rect(center=(50, 70))
    screen.blit(point_srf, point_rect)


def draw_time_to_end(time):
    """
        This function responsible only to draw the overall points
    """
    point_srf = FONT_ele.render("time to end: " + str(time), True, pygame.Color(0, 0, 0))
    point_rect = point_srf.get_rect(center=(200, 70))
    screen.blit(point_srf, point_rect)


def _draw_graph(graph: GraphAlgo):
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
    print(list_of_x)
    min_x = min(list(list_of_x))
    min_y = min(list(list_of_y))
    max_x = max(list(list_of_x))
    max_y = max(list(list_of_y))

    #drawin the nodes of the graph
    for node in list_of_nodes:
        x = _my_scale(list_of_nodes[node][0], min_x, max_x, min_y, max_y, x=True)
        y = _my_scale(list_of_nodes[node][1], min_x, max_x, min_y, max_y, y=True)
        pygame.draw.circle(screen, pygame.Color(235, 125, 87), (x, y), radius=12)
        id_srf = FONT.render(str(node), True, pygame.Color(0, 0, 0))
        id_rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, id_rect)

    #drawing the edges of the graph
    for src in graph.get_graph().get_all_src_dict():
        src_x = _my_scale(list_of_nodes[src][0], min_x, max_x, min_y, max_y, x=True)
        src_y = _my_scale(list_of_nodes[src][1], min_x, max_x, min_y, max_y, y=True)
        for dest in graph.get_graph().get_all_src_dict()[src].keys():
        # dest = graph.get_graph().get_all_src_dict()[src]
            dx = list_of_nodes.get(dest)[0]
            dy = list_of_nodes.get(dest)[1]
            dest_x = _my_scale(dx, min_x, max_x, min_y, max_y, x=True)
            dest_y = _my_scale(dy, min_x, max_x, min_y, max_y, y=True)
            pygame.draw.line(screen, pygame.Color(0, 0, 0), (src_x, src_y), (dest_x, dest_y))


def _scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen


def _my_scale(data, min_x, max_x, min_y, max_y, x=False, y=False):
    if x:
        return _scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return _scale(data, 150, screen.get_height() - 50, min_y, max_y)


def draw_agent(agents):
    """
        This function responsible only to draw the agents
    """
    for agent in agents.values():
        pygame.draw.circle(screen, Color(122, 61, 23), (agent.get_pos()[0], agent.get_pos()[1]), 10)


def draw_pokemon(pokemons):
    """
        This function responsible only to draw the pokemons
    """
    for p in pokemons:
        pygame.draw.circle(screen, Color(0, 255, 255), (int(p.get_pos()[0]), int(p.get_pos()[1])), 10)


# if __name__ == '__main__':
#     graph = GraphAlgo()
#     graph.load_from_json("C:\\Users\hadar\PycharmProjects\Ex4\data\A0")
#     draw_Frame(graph)