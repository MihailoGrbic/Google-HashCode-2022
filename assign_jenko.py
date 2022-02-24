from simulate import simulate, adapt_assignments
import random

def assign_to_project(contributors, project):
    assignments = []
    active = [True for _ in contributors]

    for role in project["roles"]:
        name, level = role
        candidates = list(filter(lambda i: active[i] and name in contributors[i]["skills"] and contributors[i]["skills"][name] >= level, range(len(contributors))))
        # candidates = sorted(candidates, key=lambda x: contributors[x]["availability"])

        if len(candidates) == 0:
            return False, []

        idx = random.sample(candidates, k=1)[0]
        # if project["name"] == "StadiaNextv9":
        #     print("idx", idx)
        assignments.append(contributors[idx])
        active[idx] = False
    
    next_available = max([x["availability"] for x in assignments]) + project["days"]
    for x in assignments:
        x["availability"] = next_available

    for assigned, role in zip(assignments, project["roles"]):
        name, level = role
        if assigned["skills"][name] <= level:
            assigned["skills"][name] += 1

    return True, assignments

def assign_to_projects(contributors, projects):
    project_assignments = []

    for contributor in contributors:
        contributor["availability"] = 0

    for project in projects:
        success, people = assign_to_project(contributors, project)
        if success:
            project_assignments.append((project["name"], people))
    
    total_score = simulate(adapt_assignments(project_assignments), projects)
    return total_score, project_assignments
