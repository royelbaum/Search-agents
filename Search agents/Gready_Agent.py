from Graph import Get_Vertex

class Gready_Agent(object):

    def __init__(self,graph,node):
        self.Graph = graph
        self.State = node
        self.Turns_To_Wait = 0
        self.Score = 0
        self.People_To_Save = number_of_people_in_the_graph(self.Graph)
        self.Terminate = False

    def Do_Turn(self):
        if self.Terminate == False:
            if self.Turns_To_Wait == 0:
                graph2 = self.Graph.copy()
                Dijkstra(graph2, self.State)
                path = Get_Path_Nearest_Goal(graph2)
                if path[0]==0:
                    self.Terminate = True
                else:    
                    self.Turns_To_Wait = self.Graph.edges[self.State ,path[0]]["weight"]
                    self.State = path[0]
                    self.People_To_Save = number_of_people_in_the_graph(self.Graph)
                    self.Score += Get_Vertex(self.State, self.Graph)["P"]
                    print ("the agent saved: " , Get_Vertex(self.State, self.Graph)["P"] )
                    print ("and the agent general score is: " , self.Score)
                    Get_Vertex(self.State, self.Graph)["P"] = 0
                    print("all the path cost: " , self.Turns_To_Wait)
            else:
                print("Grady Agent still need to wait: ", self.Turns_To_Wait , "turns")
                self.Turns_To_Wait-=1
        else:
            print("The Gready Agent is TERMINATED")
    
    

def gready(graph,node):
    people_in_the_graph = number_of_people_in_the_graph(graph)
    state = node
    score = 0
    weightpath = 0
    sum_weight_path = 0
    graph2 = graph.copy()
    while people_in_the_graph > 0:
        Dijkstra(graph2, state)
        path = Get_Path_Nearest_Goal(graph2)
        state, weightpath = Go_In_Path(graph2 , path ,state)
        sum_weight_path += weightpath 
        people_in_the_graph-= Get_Vertex(state, graph)["P"]
        score += Get_Vertex(state, graph)["P"]
        print ("the agent saved: " , Get_Vertex(state, graph)["P"] )
        print ("and the agent general score is: " , score)
        Get_Vertex(state, graph)["P"] = 0
        Get_Vertex(state, graph2)["P"] = 0
    print("all the path cost: " , sum_weight_path)
    
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


def Get_Path_Nearest_Goal(graph):
    mindist = float('inf')
    vertex = []
    for i in graph.nodes():
        if graph.nodes[i]["P"] > 0:
            if(mindist >= graph.nodes[i]["dist"]):
                mindist = graph.nodes[i]["dist"]

    if mindist == float('inf'):
        return [0]

    for i in graph.nodes():
        if graph.nodes[i]["dist"] == mindist:
            vertex.append(i)
    minlength = float('inf')
    the_chosen_vertex = 0
    for i in vertex:
        count = 0
        prevVertex = graph.nodes[i]
        while  prevVertex["prev"]!= None:
            count +=1
            prevVertex = graph.nodes[prevVertex["prev"]]
        if (count <= minlength):
            minlength = count
            the_chosen_vertex = i


    path = []
    prevVertex = the_chosen_vertex
    while graph.nodes[prevVertex]["prev"]!= None:
        path.insert(0 , prevVertex)
        prevVertex = graph.nodes[prevVertex]["prev"]
    
    return path



def Go_In_Path(graph , path , start):
    state = start
    sum_path_weight = 0
    for i in path:
        sum_path_weight += graph.edges[state,i]["weight"]
        print("the aget walks from vertex: ", state , "to vertex: ", i, "and the edge was with weight: ", graph.edges[state,i]["weight"])
        state = i 
    return state , sum_path_weight


def number_of_people_in_the_graph(graph):
    sumpeople = 0
    for i in graph.nodes:
        vertex = Get_Vertex(i,graph)
        sumpeople+=vertex["P"]
    return sumpeople


    
def get_minimum_vertex(graph , vertexset):
    mindist = float('inf')
    out = 0
    for i in vertexset:
        if graph.nodes[i]["dist"] <= mindist:
            mindist = graph.nodes[i]["dist"]
            out = i
    return out