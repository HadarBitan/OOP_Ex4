from decimal import Decimal
from pygame import Color, display


def find_edge(p_x: float, p_y: float, type: int, graph, algo) -> (int, int):
    """
    The function finds the edge of a giving pokemon
    """
    for edge in graph.Edges:
        src = algo.get_pos(edge.src)
        dst = algo.get_pos(edge.dest)
        s_x = src[0]
        s_y = src[1]
        d_x = dst[0]
        d_y = dst[1]
        m = (Decimal(s_y)-Decimal(d_y))/(Decimal(s_x)-Decimal(d_x))
        b1 = Decimal(s_y)-(Decimal(m)*Decimal(s_x))
        b2 = Decimal(p_y)-(Decimal(m)*Decimal(p_x))
        if abs(b1 - b2) < 0.00001:
            if type == -1:
                return max(edge.src, edge.dest), min(edge.src, edge.dest)
            return min(edge.src, edge.dest), max(edge.src, edge.dest)


def game_over(score, pygame, screen, FONT, sleeper, client):
    """
    The function prints the game over screen, and stop the client from running
    """
    screen.fill(Color(0, 0, 0))
    go = pygame.image.load('../img/GameOver.png')
    go = pygame.transform.scale(go, (screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(go, (screen.get_rect().center[0] - (screen.get_rect().center[0] / 2),
                     screen.get_rect().center[1] - (screen.get_rect().center[1] / 2)))
    scorelabel = FONT.render(f"Score: {score}", True, (255, 0, 0))
    screen.blit(scorelabel, (screen.get_rect().center[0] - (screen.get_rect().center[0] / 15),
                             screen.get_rect().center[1] - (screen.get_rect().center[1])))
    display.update()
    sleeper.sleep(3)
    client.stop()
    client.stop_connection()
    pygame.quit()
    exit(0)


def open_game(pygame, screen, FONT, sleeper, client):
    """
    The function starts the game, she creates the opening screen and tells the client to start
    """
    openingPic = pygame.image.load('../img/openingPic.png')
    openingPic = pygame.transform.scale(openingPic, (500, 500))
    screen.blit(openingPic, (screen.get_rect().center[0] - (screen.get_rect().center[0] / 2),
                             screen.get_rect().center[1] - (screen.get_rect().center[1] / 2)))
    openLable = FONT.render("Welcome to our game! Go catch those Pokemons!", True, (255, 0, 0))
    screen.blit(openLable, (screen.get_rect().center[0] - (screen.get_rect().center[0] / 3),
                             screen.get_rect().center[1] - (screen.get_rect().center[1])))

    display.update()
    sleeper.sleep(2)
    client.start()


def choose_next_node(agents, pokemons, poke_data, graph, algo, client):
    """
    This function choose the next edge for each agent according to minimum distance from the pokemons, and send this
    agent to catch the pokemon.
    """
    for agent in agents:
        if agent.dest == -1:
            min_dist = 1000000000
            i = 0
            for p in pokemons:
                e = find_edge(poke_data[i][0], poke_data[i][1], poke_data[i][2], graph, algo)
                print(e)
                t_dist, t_list = algo.shortest_path(agent.src, e[0])
                i += 1
                if t_dist == 0:
                    next_node = e[1]
                    break
                if t_dist < min_dist:
                    min_dist = t_dist
                    next_node = t_list[1]
            client.choose_next_edge(
                '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
            ttl = client.time_to_end()
            print(ttl, client.get_info())

