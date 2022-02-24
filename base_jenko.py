import numpy as np
from sort_projects import sort_projects
from assign_jenko import assign_to_projects
from copy import deepcopy

#file_name = "a_an_example"
#file_name = "b_better_start_small"
file_name = "c_collaboration"
#file_name = "d_dense_schedule"
#file_name = "e_exceptional_skills"
# file_name = "b_better_start_small"
with open("in/" + file_name + ".in.txt") as f:
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

project_list = sort_projects(project_list, contrib_list)

best_assignment = []
best_score = -1
for i in range(10):
    total_score, project_assignments = assign_to_projects(deepcopy(contrib_list), project_list)
    if i % 10 == 0:
        print(i)

    if total_score > best_score:
        print(total_score)
        best_score = total_score
        best_assignment = project_assignments


with open(file_name + ".txt", 'w') as f:  
    f.write(str(len(project_assignments)) + "\n")
    
    for assignment in project_assignments:
        name, people = assignment
        
        f.write(name + "\n")
        f.write(" ".join([x["name"] for x in people]) + "\n")
