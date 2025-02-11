from graphviz import Graph
from classes.GraphObjects import *


class Design():
    def create(self):
        return Graph('G', format='png', engine='neato')

    def trace(self, graph, design_objects):
        self._trace_buildings(graph, [obj for obj in design_objects if isinstance(obj, (Building, Warehouse))])
        self._trace_highways(graph, [obj for obj in design_objects if isinstance(obj, Highway)])
        graph.render('graph_with_node', format='png', view=True)

    def _trace_buildings(self, graph, building_objects):
        for building in building_objects:
            color = building.color

            for i, (x, y, _) in enumerate(building.params):
                graph.node(f"{building.typology}_{i}", color=color, pos=f'{x},{y}!', label=f"({x},{y})",shape='point')
            for i in range(len(building.params) - 1):
                graph.edge(f"{building.typology}_{i}", f"{building.typology}_{i + 1}", color=color)
            if len(building.params) > 1:
                graph.edge(f"{building.typology}_0", f"{building.typology}_{len(building.params) - 1}",color=color)

    def _trace_highways(self, graph, highway_objects):
        allHighways = []

        for highway in highway_objects:
            if isinstance(highway.params[0], tuple):
                graph.node(f"{highway}_1", pos=f'{highway.params[0][0]},{highway.params[1]}!', shape='point')
                graph.node(f"{highway}_2", pos=f'{highway.params[0][1]},{highway.params[1]}!', shape='point')
                graph.edge(f"{highway}_1", f"{highway}_2", penwidth=str(highway.params[2]),label=str(highway.params[2]))

            elif isinstance(highway.params[1], tuple):
                graph.node(f"{highway}_1", pos=f'{highway.params[0]},{highway.params[1][0]}!', shape='point')
                graph.node(f"{highway}_2", pos=f'{highway.params[0]},{highway.params[1][1]}!', shape='point')
                graph.edge(f"{highway}_1", f"{highway}_2", penwidth=str(highway.params[2]),label=str(highway.params[2]))

            #plot a node if two highways intersect
            xyPassed, _ = highway.pathstops()
            for k in xyPassed:
                if k in allHighways:
                    graph.node(f"{highway}", pos=f'{k[0]},{k[1]}!', shape='point')
                allHighways.append(k)

