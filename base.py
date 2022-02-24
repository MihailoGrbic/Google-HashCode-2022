import numpy as np
from common import Contributor, Project

# contr = []
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
            skills[skill_name] = skill_level
        contr["skills"] = skills
        contrib_list.append(contr)

    for i in range(p):
        line = f.readline()
        print(line)
        name, days, score, best_before, num_roles = line.split()
        project = {"name": name, "days" : days, "score" : score, "best_before" : best_before}
        roles = []
        for j in range(int(num_roles)):
            line = f.readline()
            skill_name, skill_level = line.split()
            roles.append((skill_name, skill_level))
        project["roles"] = roles
        project_list.append(project)

    