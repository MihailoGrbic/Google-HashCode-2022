def assign_to_project(contributors, project):
    assignments = []
    active = [True for _ in contributors]

    for role in project["roles"]:
        success = False 

        for i in range(len(contributors)):
            contributor = contributors[i]
            if not active[i]:
                continue

            name, level = role
            skills = contributor["skills"]
            if name in skills and skills[name] >= level:
                assignments.append(contributor)
                active[i] = False
                success = True
                break
        
        if not success:
            return False, []
                
    return True, assignments

def assign_to_projects(contributors, projects):
    project_assignments = []
    for project in projects:
        success, people = assign_to_project(contributors, project)
        if success:
            project_assignments.append((project["name"], people))
    return project_assignments
    