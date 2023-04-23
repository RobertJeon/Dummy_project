import csv
import pandas as pd
from .dummy_data_utils import random_understanding

# def create_understanding_data_csv(name_userid_list, notes, file_path):
#     with open("understanding_data.csv", "w", encoding="utf-8", newline="") as csvfile:
#         fieldnames = ["이름", "userid", "진행 노트", "오전 이해도", "오후 이해도"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
        
#         for name, userid in name_userid_list:
#             for note in notes:
#                 morning_understanding = random_understanding()
#                 afternoon_understanding = random_understanding()
#                 writer.writerow({"이름": name, "userid": userid, "진행 노트": note, "오전 이해도": morning_understanding, "오후 이해도": afternoon_understanding})

def create_understanding_data_csv(name_userid_list, notes, file_path):
    data = []
    for name, userid in name_userid_list:
        for note in notes:
            morning_understanding = random_understanding()
            afternoon_understanding = random_understanding()
            data.append([name, userid, note, morning_understanding, afternoon_understanding])

    df = pd.DataFrame(data, columns=["name", "userid", "note", "morning_understanding", "afternoon_understanding"])
    df.to_csv(file_path, index=False)