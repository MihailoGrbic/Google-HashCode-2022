import numpy as np
# from common import Contributor, Project

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
        project_assignments.append(assign_to_project(contributors, project))
    return project_assignments
    

with open('in/a_an_example.in.txt') as f:
    line = f.readline()
    c, p = line.split()
    c, p = int(c), int(p)

    contrib_list = []
    project_list = []
    for i in range(c):
        line = f.readline()
        person_name, num_skills = line.split()
        contr = {"name" : person_name}
        skills = {}
        for j in range(int(num_skills)):
            line = f.readline()
            skill_name, skill_level = line.split()
            skills[skill_name] = float(skill_level)
        contr["skills"] = skills
        contrib_list.append(contr)

    for i in range(p):
        line = f.readline()
        name, days, score, best_before, num_roles = line.split()
        project = {"name": name, "days" : float(days), "score" : float(score), "best_before" : float(best_before)}
        roles = []
        for j in range(int(num_roles)):
            line = f.readline()
            skill_name, skill_level = line.split()
            roles.append((skill_name, float(skill_level)))
        project["roles"] = roles
        project_list.append(project)

    project_assignments = assign_to_projects(contrib_list, project_list)
    for project, assignment in zip(project_list, project_assignments):
        success, people = assignment
        if not success:
            continue

        print(project["name"])
        print(" ".join([x["name"] for x in people]))
