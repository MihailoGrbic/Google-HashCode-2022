class qentry():
    pass

class Node():
    def __init__(self, name, days, score, best_before, contributors, neighbors):
        self.name = name
        self.days = days
        self.score = score
        self.best_before = best_before
        self.contributors = contributors

        self.neighbors = neighbors
        self.reverse_edges = []

        self.indeg = len(neighbors)
        self.start_time = None
        self.end_time = None

def has_intersection(cont1, cont2):
    return (len(set(cont1).intersection(cont2)) > 0)

def simulate(assignments, projects):
    # print("Simulating for: ")
    # print(assignments)
    
    graph = []
    
    # Generate graph
    for ass in assignments:
        # print("Formiram ", ass["name"])
        for project in projects:
            if ass["name"] == project["name"]:
                # print("Matchovao sam ", ass["name"])
                neighbors = []
                for i in range(len(graph)):
                    if has_intersection(ass["contributors"], graph[i].contributors):
                        neighbors.append(i)
                        graph[i].reverse_edges.append(len(graph))

                graph.append(Node(
                    ass["name"],
                    project["days"],
                    project["score"],
                    project["best_before"],
                    ass["contributors"],
                    neighbors
                ))
                break
    
    # Print graph
    # print("Ispisujem graf")
    # for node in graph:
    #     print(node.name)
    #     print(node.score)
    # print()

    # Toposort
    # print("Toposort")
    queue = []
    for node in graph:
        # print("indeg ", node.indeg)
        if node.indeg == 0:
            node.start_time = 0
            queue.append(node)

    # print("queue ", len(queue))
    # print()

    # Run projects
    # print("Run projects")
    total_score =  0
    while len(queue) > 0:
        cur = queue[0]
        queue.pop(0)
        # print("Obradjujem ", cur.name)

        cur.end_time = cur.start_time + cur.days - 1
        penalty = max(0, cur.end_time + 1 - cur.best_before)
        real_value = max(0, cur.score - penalty)
        # print("Posao ", cur.name, cur.start_time, cur.end_time)
        # print("Vredi", real_value)
        total_score += real_value
        
        for next_idx in cur.reverse_edges:
            next = graph[next_idx]
            next.indeg -= 1
            # print("Razmatram next ", next.name)
            # print("Njegov indeg ", next.indeg)
            if next.indeg == 0:
                next.start_time = cur.end_time + 1
                queue.append(next)

    return total_score

def adapt_assignments(assignments):
    ret = []
    for ass in assignments:
        name, people = ass
        ret.append(
            {
                "name": name,
                "contributors": [x["name"] for x in people]
            }
        )

    return ret
     

if __name__ == "__main__":
    assignments = [
        {
            "name": "WebServer",
            "contributors": ["Bob", "Anna"]
        },
        {
            "name": "Logging",
            "contributors": ["Anna"]
        },
        {
            "name": "WebChat",
            "contributors": ["Maria", "Bob"]
        }
    ]

    projects = [
        {'name': 'Logging', 'days': 5.0, 'score': 10.0, 'best_before': 5.0, 'roles': [('C++', 3.0)]}, 
        {'name': 'WebServer', 'days': 7.0, 'score': 10.0, 'best_before': 7.0, 'roles': [('HTML', 3.0), ('C++', 2.0)]}, 
        {'name': 'WebChat', 'days': 10.0, 'score': 20.0, 'best_before': 20.0, 'roles': [('Python', 3.0), ('HTML', 3.0)]}]

    print(simulate(assignments, projects))