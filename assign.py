from audioop import reverse


def assign_to_project(contributors, project):
    assignments = []
    active = [True for _ in contributors]

    mentored = [False for _ in project["roles"]]
    for role_id, role in enumerate(project["roles"]):
        name, level = role

        if mentored[role_id]:
            if level == 1:
                candidates = list(filter(lambda i: active[i], range(len(contributors))))
            else:
                candidates = list(filter(lambda i: active[i] and name in contributors[i]["skills"] and contributors[i]["skills"][name] >= level-1, range(len(contributors))))
        else:
            candidates = list(filter(lambda i: active[i] and name in contributors[i]["skills"] and contributors[i]["skills"][name] >= level, range(len(contributors))))
        candidates = sorted(candidates, key=lambda x: contributors[x]["availability"])
        #candidates = sorted(candidates, key=lambda x: contributors[x]["skills"][name], reverse=True)

        if len(candidates) == 0:
            return False, []

        idx = candidates[0]
        assignments.append(contributors[idx])
        active[idx] = False

        for role_id, role2 in enumerate(project["roles"]):
            name2, level2 = role2
            if name2 in contributors[idx]["skills"] and contributors[idx]["skills"][name2] >= level2:
                mentored[role_id] = True

    next_available = max([x["availability"] for x in assignments]) + project["days"]
    for x in assignments:
        x["availability"] = next_available

    for assigned, role in zip(assignments, project["roles"]):
        name, level = role

        if name in assigned["skills"]:
            if assigned["skills"][name] <= level:
                assigned["skills"][name] += 1
        else:
            assigned["skills"][name] = 1

    return True, assignments

def assign_to_projects(contributors, projects):
    project_assignments = []

    for contributor in contributors:
        contributor["availability"] = 0

    for project in projects:
        success, people = assign_to_project(contributors, project)
        if success:
            project_assignments.append((project["name"], people))
    return project_assignments
