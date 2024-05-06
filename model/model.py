from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMap = {}
        for f in self._fermate:
            self._idMap[f.id_fermata] = f

    def buildGraph(self):
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
        print(len(allConnessioni))
        for c in allConnessioni:
            u_nodo = self._idMap[c.id_stazP]
            v_nodo = self._idMap[c.id_stazA]
            self._grafo.add_edge(u_nodo, v_nodo)
            print(f"Added edge between {u_nodo} and {v_nodo}")
    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)