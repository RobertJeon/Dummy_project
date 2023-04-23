import random
import string

# def random_name():          # 랜덤 이름 3글자
#     return ''.join([chr(random.randint(0xAC00, 0xD7AF)) for _ in range(3)])

first_names = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임"]
middle_names = ["철", "영", "민", "지", "성", "현", "수", "혜", "예", "유"]
last_names = ["수", "아", "영", "훈", "원", "진", "호", "윤", "원", "민"]

def random_name():          # 랜덤 이름 3글자
    first = random.choice(first_names)
    middle = random.choice(middle_names)
    last = random.choice(last_names)
    return first + middle + last


def random_userid():        # 유저 id 
    return random.randint(10000, 99999)

def random_understanding(): # 이해도 조사
    return random.choice(["미진행", 1, 2, 3])

def random_score():         # 과제 점수
    return random.randint(-1, 3)

# 진행 강의 노트
notes = ["n11", "n12", "n13", "n14", "n21", "n22", "n23", "n24", "n31", "n32", "n33", "n34"]

# 과제 및 시험
assignments = ["n11", "n12", "n13", "n14", "sc1x", "n21", "n22", "n23", "n24", "sc2x", "n31", "n32", "n33", "n34", "sc3x"]

def create_name_userid_list(n):
    name_userid_list = []
    for _ in range(n):
        name = random_name()
        userid = random_userid()
        while (name, userid) in name_userid_list:
            name = random_name()
            userid = random_userid()
        name_userid_list.append((name, userid))
    return name_userid_list