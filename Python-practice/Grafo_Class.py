
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self,vertex):
        if vertex in self.graph:
            print("Vertex already in graph")
        self.graph[vertex] = []
    
    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 not in self.graph:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph[v1].append(v2)

    def is_vertex_in(self, vertex):
        return vertex in self.graph
    
    def get_vertex(self, vertex_name):
        for v in self.graph:
            if vertex_name == v.get_name():
                return v
        print(f'Vertex {vertex_name} does not exist')

    def get_neighbors(self, vertex_name):
        return self.graph[vertex_name]
    
    def __str__(self):
        all_edges = ''
        for v1 in self.graph:
            for v2 in self.graph[v1]:
                all_edges += v1.get_name() + ' ----- ' + v2.get_name() + "\n"
        return all_edges

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
   
    def get_v1(self):
        return self.v1
    
    def get_v2(self):
        return self.v2
    
    def __str__(self):
        return self.v1.get_name() + '-----' + self.v2.get_name()
    
class Vertex:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    
def Distancia(Apoint, Bpoint):
    dis = ((Apoint[0] - Bpoint[0])**2+(Apoint[1] - Bpoint[1])**2+(Apoint[2] - Bpoint[2])**2)**(1/2)
    return dis

Coordenadas = []
with open("Au60.xyz","r") as data:
    for i in data:
        x = float(i[7:16])
        y = float(i[21:30])
        z = float(i[35:44])
        Atomo = (x,y,z)
        Coordenadas.append(Atomo)
data.close()

G1 = Graph()

j = 0
for i in Coordenadas:
    nombre = "Atom" + str(j+1)
    G1.add_vertex(Vertex(nombre))
    j = j+1 

for i in range(0,60):
    for j in range(0,60):
        if  Distancia(Coordenadas[i],Coordenadas[j]) >= 2.6 and Distancia(Coordenadas[i],Coordenadas[j]) <= 4:
            nombre = "Atom" + str(i+1)
            nombre1 = "Atom" + str(j+1)
            G1.add_edge(Edge(G1.get_vertex(nombre), G1.get_vertex(nombre1)))

print(G1)