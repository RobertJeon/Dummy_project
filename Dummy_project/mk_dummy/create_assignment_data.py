import csv
import pandas as pd
from .dummy_data_utils import random_score

# def create_assignment_data_csv(name_userid_list, assignments, file_path):
#     with open("assignment_data.csv", "w", encoding="utf-8", newline="") as csvfile:
#         fieldnames = ["이름", "userid", "과제", "점수"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()

#         for name, userid in name_userid_list:
#             for assignment in assignments:
#                 score = random_score()
#                 writer.writerow({"이름": name, "userid": userid, "과제": assignment, "점수": score})


def create_assignment_data_csv(name_userid_list, assignments, file_path):
    data = []
    for name, userid in name_userid_list:
        for assignment in assignments:
            score = random_score()
            data.append([name, userid, assignment, score])

    df = pd.DataFrame(data, columns=["name", "userid", "assignment", "score"])
    df.to_csv(file_path, index=False)
