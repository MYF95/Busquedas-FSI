# Search methods

import search

ab = search.GPSProblem('A', 'E', search.romania)



print search.breadth_first_graph_search(ab).path()
print search.depth_first_graph_search(ab).path()
print search.sorted_graph_search(ab).path()
print search.sorted_first_tree_search(ab).path()
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# [<Node B>, <Node F>, <Node S>, <Node R>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 211 + 99 + 80 + 146 + 120 + 75 + 70 + 111 + 118 = 1030
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418

#[<Node U>, <Node B>, <Node F>, <Node S>, <Node A>] : 85 + 211 + 99 + 140 = 535
#[<Node U>, <Node B>, <Node F>, <Node S>, <Node R>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 85 + 211 + 99 + 80 + 146 + 120 + 75 + 70 + 111 + 118 = 1115
#[<Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 85 + 101 + 97 + 80 + 140 = 503

