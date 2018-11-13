# file = open("word.txt", "w")
# file.write("파일 내용을 작성합니다.")
# file.close()

with open("word.txt", "r") as file:
    for line in file:
        print(line)

with open("list.csv", "w", encoding="utf8") as file:
    file.write("이름,성별,나이\n")
    file.write("김수남,남,23\n")
    file.write("성수남,남,23\n")

def read_file():
    with open("list.csv", "r", encoding="utf8") as file:
        for line in file:
            print("a.csv line >>> ", line)

read_file()