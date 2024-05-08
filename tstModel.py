from datetime import datetime

from model.model import Model

mymodel = Model()
mymodel.buildGraph()

# tic = datetime.now()
# mymodel.addEdgeMode1()
# toc = datetime.now()
# print(f"Time elapsed: {toc-tic}")
#
# tic = datetime.now()
# mymodel.addEdgeMode2()
# toc = datetime.now()
# print(f"Time elapsed: {toc-tic}")

tic = datetime.now()
mymodel.addEdgeMode3()
toc = datetime.now()
print(f"Time elapsed: {toc-tic}")


mymodel.getDFS()

print(f"The graph has {mymodel.getNumNodes()} nodes.")
print(f"The graph has {mymodel.getNumEdges()} edges.")
