from Problem import State
import networkx as nx


def Sort_By_F(open):
    return sorted(open, key=lambda s:s.h+s.g)

       
def restore_path(state):
    path=[state.Node]
    while state.Prev!=None:
        path.insert(0 , state.Prev.Node)
        state=state.Prev
    return path


def restore_path_states(state):
    path=[state]
    while state.Prev!=None:
        path.insert(0 , state)
        state=state.Prev
    return path


def in_close(close,state):
    for s in close:
        if s.Node==state.Node and s.Nodes_W_P==state.Nodes_W_P and s.g <= state.g:
            return True
    return False


def collect_P(state):
    if state.Node in state.Nodes_W_P:
        state.Nodes_W_P.remove(state.Node)


def Expand(state,graph):
    nighbores = []
    for i in list(graph.adj[state.Node]):
        newnode = State(i,graph,state,state.g+graph.edges[state.Node,i]["weight"])
        nighbores.append(newnode)
    return nighbores

def Expand_gridy(state,graph):
    nighbores = []
    for i in list(graph.adj[state.Node]):
        newnode = State(i,graph,state,0)
        nighbores.append(newnode)
    return nighbores

def Dijkstra (graph,source):
    VertexSet = []
    for i in graph.nodes:             
        graph.nodes[i]["dist"] =  float('inf')                
        graph.nodes[i]["prev"] = None        
        VertexSet.append(i)                         
    graph.nodes[source]["dist"] = 0 
    while (len(VertexSet) > 0):
        mindist = get_minimum_vertex(graph,VertexSet)   
        VertexSet.remove(mindist)
        for neighbor in graph.adj[mindist]:       
            alt = graph.nodes[mindist]["dist"] + graph.edges[mindist,neighbor]["weight"]
            if alt < graph.nodes[neighbor]["dist"]:              
                    graph.nodes[neighbor]["dist"] = alt 
                    graph.nodes[neighbor]["prev"] = mindist 


    
def get_minimum_vertex(graph , vertexset):
    mindist = float('inf')
    out = 0
    for i in vertexset:
        if graph.nodes[i]["dist"] <= mindist:
            mindist = graph.nodes[i]["dist"]
            out = i
    return out




def reduct_for_H(graph,state):
    reducted_graph=nx.Graph()
    sorce=state.Node
    nodes=state.Nodes_W_P
    if sorce not in state.Nodes_W_P:
        nodes+=[sorce]
    for i in nodes:
        reducted_graph.add_node(i,P=graph.nodes[i]["P"])

    for i in nodes:
        Dijkstra(graph,i)
        for j in nodes:
            if j>i and graph.nodes[j]["dist"]!= float('inf'):
                reducted_graph.add_edge(i,j,weight=graph.nodes[j]["dist"])

    return reducted_graph

def mst_hurisrtic(state,graph):
    small_g=reduct_for_H(graph,state)
    nodes=[state.Node]
    edges=[]
    while len(nodes)<len(small_g.nodes):
        min_weight=float('inf')
        min_edge=None
        for n in nodes:
            for e in small_g.edges:
                if e not in edges and (e[0]==n or e[1]==n):
                    if (e[0]==n and  e[1] not in nodes) or (e[1]==n and  e[0] not in nodes):
                        w=small_g.edges[e[0],e[1]]["weight"]
                        if min_weight>w:
                            min_weight=w
                            min_edge=e
        if min_edge!= None:
            edges+=[min_edge]
            if min_edge[0] in nodes:
                nodes+=[min_edge[1]]
            else:
                nodes+=[min_edge[0]]
        else:
            return "failure"
    h_result=0
    for (i,j) in edges:
        h_result+=small_g.edges[i,j]["weight"]
    return h_result
    
def update_h_val(state,graph,h):
    sol =  h(state, graph)
    if sol == "failure":
        return sol
    state.h=sol


def Sort_By_H_tag(open):
    return sorted(open,key=lambda s:s.h)