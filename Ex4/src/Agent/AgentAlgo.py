import json

from src.Agent.Agent import Agent
from src.Graph.Point3D import Point3D


class AgentAlgo:
    """
        This class representing an algorithm to agent, its purpose is to run a functions on the agent
    """
    def __init__(self):
        self._list_of_agent: {int: Agent} = {}

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as f:  # Open a file for reading
                Jsonfile = json.load(f)
                for agent in Jsonfile["Agents"]:
                    pos = tuple(map(float, str(agent["pos"]).split(",")))
                    new_agent = Agent(agent["id"], agent["value"], agent["src"], agent["dest"],
                                      agent["speed"], Point3D(pos[0], pos[1], pos[2]))
                    self.list_of_agent[agent["id"]] = new_agent
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        dictionary = {"Agents": []}
        for agent in self.list_of_agent.values():
            agent_dict = {"Agent": {"id": agent.get_id(), "value": agent.get_value(), "src": agent.get_src(),
                                    "dest": agent.get_dest(), "speed": agent.get_speed(),
                                    "pos": str(agent.get_pos())}}
            dictionary["Agents"].append(agent_dict)
        try:
            json_object = json.dumps(dictionary, indent=4)
            with open(file_name, 'w') as outfile:  # Open a file for writing
                outfile.write(json_object)
                return True
        except Exception as e:
            print(e)
            return False
