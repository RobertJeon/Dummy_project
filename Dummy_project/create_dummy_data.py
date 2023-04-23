import os
from mk_dummy.dummy_data_utils import create_name_userid_list
from mk_dummy.create_understanding_data import create_understanding_data_csv
from mk_dummy.create_assignment_data import create_assignment_data_csv

def main():
    num_dummy = int(input("생성할 더미 데이터의 개수를 입력하세요: "))
    name_userid_list = create_name_userid_list(num_dummy)
    
    notes = ["n11", "n12", "n13", "n14", "n21", "n22", "n23", "n24", "n31", "n32", "n33", "n34"]
    assignments = ["n11", "n12", "n13", "n14", "sc1x", "n21", "n22", "n23", "n24", "sc2x", "n31", "n32", "n33", "n34", "sc3x"]

    if not os.path.exists('data'):
        os.makedirs('data')

    # create_understanding_data_csv(name_userid_list, notes, os.path.join("data", "understanding_data.csv"))
    # create_assignment_data_csv(name_userid_list, assignments, os.path.join("data", "assignment_data.csv"))

    create_understanding_data_csv(name_userid_list, notes, "data/understanding_data.csv")
    create_assignment_data_csv(name_userid_list, assignments, "data/assignment_data.csv")


if __name__ == "__main__":
    main()