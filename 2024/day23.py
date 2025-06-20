from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        graph: dict[str, set[str]] = dict()

        for l in self.dataRaw.split('\n'):
            c1, c2 = l.split('-')
            graph.setdefault(c1, set())
            graph.setdefault(c2, set())
            graph[c1].add(c2)
            graph[c2].add(c1)

        triangles = []
        for u in graph:
            for v in graph[u]:
                if v > u:
                    common = graph[u].intersection(graph[v])
                    for w in common:
                        if w > v:
                            triangles.append((u, v, w))

        return len([i for i in triangles if any(j.startswith("t") for j in i)])

    def Part2(self) -> BaseSolution.ResultType:
        graph: dict[str, set[str]] = dict()

        for l in self.dataRaw.split('\n'):
            c1, c2 = l.split('-')
            graph.setdefault(c1, set())
            graph.setdefault(c2, set())
            graph[c1].add(c2)
            graph[c2].add(c1)

        def BronKerbosch(
            currentClique: set[str],
            candidates:    set[str],
            visited:       set[str],
            graph:         dict[str, set[str]],
            cliques:       list[set[str]]
        ):
            if not candidates and not visited:
                cliques.append(currentClique)
                return

            for v in list(candidates):
                BronKerbosch(currentClique.union({v}), candidates.intersection(graph[v]), visited.intersection(graph[v]), graph, cliques)
                candidates.remove(v)
                visited.add(v)

        cliques = []
        BronKerbosch(set(), set(graph.keys()), set(), graph, cliques)

        return ",".join(sorted(max(cliques, key=len)))
