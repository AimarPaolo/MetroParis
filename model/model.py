from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMap = {}
        for f in self._fermate:
            self._idMap[f.id_fermata] = f

    def getBFSnodes(self, source):
        edges = nx.bfs_edges(self._grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited
    #restituisce una lista di nodi che abbiamo visitato, in una tipologia BFS

    def buildGraphPesato(self):
        "questo metodo è del tutto equivalente a buildGraph, ma chiama come metodo per aggiungere gli archi addEdgePesati"
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)
        self.addEdgePesati()

    def addEdgePesati(self):
        self._grafo.clear_edges()
        allConnessioni = DAO.get_all_connessioni()
        for c in allConnessioni:
            if self._grafo.has_edge(self._idMap[c.id_stazP], self._idMap[c.id_stazA]):
                self._grafo[self._idMap[c.id_stazP]][self._idMap[c.id_stazA]]["weight"] += 1
            else:
                self._grafo.add_edge(self._idMap[c.id_stazP], self._idMap[c.id_stazA], weight=1)

    def getDFSnodes(self, source):
        edges = nx.bfs_edges(self._grafo, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited

    def buildGraph(self):
        #viene aggiunta una lista di oggetti fermata
        self._grafo.add_nodes_from(self._fermate)
        #mi aggiunge tutti i nodi che ho nella lista fermate
        #Mode 1: doppio loop su nodi e quey per ogni arco
        """for u in self._fermate:
            for v in self._fermate:
                res = DAO.getAllEdges(u, v)
                if len(res) > 0:
                    self._grafo.add_edge(u, v)
                    print(f"Added edge between {u} and {v}")"""
        #Mode 2: loop singolo sui nodi e query per identificare i vicini
        """for u in self._fermate:
            vicini = DAO.getEdgesVicini(u)
            for v in vicini:
                v_nodo = self._idMap[v.id_stazA]
                self._grafo.add_edge(u, v_nodo)
                print(f"Added edge between {u} and {v_nodo}")"""

        allConnessioni = DAO.get_all_connessioni()
        for c in allConnessioni:
            u_nodo = self._idMap[c.id_stazP]
            v_nodo = self._idMap[c.id_stazA]
            self._grafo.add_edge(u_nodo, v_nodo)
            print(f"Added edge between {u_nodo} and {v_nodo}")

    def buildGraphPesato(self):
        self._grafo.clear_edges()

    def getEdgeWeights(self, v1, v2):
        #questa funzione restituisce il peso del grafo in quel determinato momento
        return self._grafo[v1][v2]["weight"]

    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getArchiPesoMaggiore(self):
        if len(self._grafo.edges) == 0:
            print("Il grafo è vuoto")
            return
        edges = self._grafo.edges
        result = []
        for u, v in edges:
            peso = self._grafo[u][v]["weight"]
            #peso stampa il peso di ogni valore
            if peso > 1:
                result.append((u, v))
        return result
