from Gready_Agent import Dijkstra , number_of_people_in_the_graph
from Helpful_Function import *


def h(state,graph):
        num_of_p=len(state.Nodes_W_P)
        if num_of_p == 0 or (num_of_p==1 and state.Node==state.Nodes_W_P[0]):
            return 0
        Dijkstra(graph, state.Node)
        min_w = float('inf')
        for i in state.Nodes_W_P:
            if i!=state.Node and min_w > graph.nodes[i]["dist"]:
                min_w = graph.nodes[i]["dist"]
        return min_w


def f(h,state,graph):
    return state.g + h(state,graph)


def Real_Time_A_Star(problem, h,f, L=10):
    OPEN = [problem.Initial_State]
    CLOSE = []
    count=0
    limit = L
    startstate = []
    numberofwaysinroad = 0
    while(True):
        numberofwaysinroad+=1
        for i in range(limit):
            if len(OPEN) == 0:
                return "failure"
            else:
                state = OPEN.pop(0)
                if i ==0:
                    startstate.append(state)
                collect_P(state)

                if problem.Goal_Test(state, h):
                    print("number of expanding", count)
                    return state
                if not in_close(CLOSE,state):
                    #print("I insert to close the state: ", state.Node, state.Nodes_W_P , state.g) 
                    CLOSE.insert(0, state)
                    expandarray = Expand(state,problem.Graph)
                    for s in expandarray:
                        fail = update_h_val(s, problem.Graph, h)
                        if fail == "failure":
                            return "failure"
                    OPEN = OPEN + expandarray
                    count += 1
                OPEN=Sort_By_F(OPEN)

        OPEN=Sort_By_F(OPEN)
        state = OPEN.pop(0)
        roadstates = restore_path_states(state)
        for j in range(numberofwaysinroad):
            state = roadstates.pop(0)
        CLOSE = []
        OPEN = [state]     
            



