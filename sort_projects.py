def sort_projects(projects, contributors):
    for project in projects:
        score_per_day = project["score"] / project["days"]
        score_per_bb = project["score"] / project["best_before"]
        score_per_roles = project["score"] / len(project["roles"])

        max_level = 0
        level_sum = 0
        for role in project["roles"]:
            max_level = max(max_level, role[1])
            level_sum += role[1]
        score_per_h_level = project["score"] / max_level
        score_per_level_sum = project["score"] / level_sum


        project["priority"] = score_per_day + score_per_bb + score_per_roles + \
                            score_per_h_level + score_per_level_sum
        project["priority"] = score_per_day * score_per_bb * score_per_roles * \
                            score_per_h_level * score_per_level_sum

    return sorted(projects, key = lambda i: i['priority'], reverse=True)