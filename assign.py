def assign_to_project(contributors, project):
    assignments = []
    active = [True for _ in contributors]

    for role in project["roles"]:
        name, level = role
        candidates = list(filter(lambda i: active[i] and name in contributors[i]["skills"] and contributors[i]["skills"][name] >= level, range(len(contributors))))
        candidates = sorted(candidates, key=lambda x: contributors[x]["availability"])

        if len(candidates) == 0:
            return False, []

        idx = candidates[0]
        assignments.append(contributors[idx])
        active[idx] = False
    
    next_available = max([x["availability"] for x in assignments]) + project["days"]
    for x in assignments:
        x["availability"] = next_available

    return True, assignments

def assign_to_projects(contributors, projects):
    project_assignments = []

    for contributor in contributors:
        contributor["availability"] = 0

    for project in projects:
        success, people = assign_to_project(contributors, project)
        if success:
            project_assignments.append((project["name"], people))
        # print(" ".join([str(x["availability"]) for x in contributors]))
    return project_assignments
    