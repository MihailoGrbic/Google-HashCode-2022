def sort_projects(projects):
    for project in projects:
        project["score_per_day"] = project["score"] / project["days"]
        project["score_per_bb"] = project["score"] / project["best_before"]
        project["score_per_roles"] = project["score"] / len(project["roles"])

        project["priority"] = project["score_per_day"] + project["score_per_bb"] + project["score_per_roles"]

    return sorted(projects, key = lambda i: i['priority'], reverse=True)