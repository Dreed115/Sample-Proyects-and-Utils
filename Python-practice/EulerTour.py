class EulerTour:

    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree
    
    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree.root(),0,[])
        
    def _tour(self, p, d, path):
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer
    
    def _hook_previsit(self, p, d ,path):
        pass

    def _hook_postvisit(self, p, d ,path, results):
        pass

class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*"" + str(p.element()))