from a_star_alg import A_Star
from Part2_Gready_Aget import Gready_Heuristic_Agent
from Real_Time_A_Star import Real_Time_A_Star
from Problem import Problem
from Helpful_Function import restore_path

class Agent(object):

    # it holds the H L and F to be able to opparate each agent with diffrent heuristic fuction and limit
    def __init__(self, policy, graph,h,f,initialstate=1,l=10):
        self.Policy = policy
        self.Graph = graph
        # self.Reducted_Graph = reduct(graph, initialstate)
        self.Problem = Problem(graph,initialstate)
        self.H = h
        self.F = f
        self.L = l
        self.Road = []
        self.Terminate = False
        self.Score = 0
        self.Current_Node = self.Problem.Initial_State.Node
        self.Collected_People = 0
    
    # the agent find the best way to go in and restore it in the Road and then give 1 step each time
    def Do_Turn(self):
        if self.Road == [] and self.Terminate == False:
            if self.Policy == "A_Star":
                sol=A_Star(self.Problem,self.H,self.F)
            elif self.Policy == "Gready_Agent":
                sol=Gready_Heuristic_Agent(self.Problem,self.H)
            elif self.Policy == "Real_Time_A_Star":
                sol=Real_Time_A_Star(self.Problem,self.H,self.F,self.L)
            # map = make_map(self.Graph, 1)
            if sol == "failure":
                return sol
            if not isinstance(sol, str):
                r=restore_path(sol)
                # self.Road = restore_original_path(r, map)
                self.Road = r
                print("The road from ",self.Policy,":" ,self.Road)
                self.Current_Node=self.Road.pop(0)
            self.Terminate = True
            # return self.Current_Node

        elif self.Road == []:
            return "Terminated"
        # else:
        # print(len(self.Road))
        if len(self.Road)>0:
            step = self.Road.pop(0)
            self.Score = self.Score + self.Graph.edges[self.Current_Node,step]["weight"]
            self.Collected_People = self.Collected_People + self.Graph.nodes[step]["P"]
            self.Current_Node = step
            print("The Agent Collet: ", self.Collected_People, "The Total Road Weight So Far is: ", self.Score, "And His Corrent Location is: ", self.Current_Node)
            return step

        return      self.Current_Node
            

                





