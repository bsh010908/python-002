# 파일 열기
with open("C:\\edumgt-java-education\\java-education-001\\resources\\test.txt", "r", 
          encoding="utf-8") as f:
    # 한 줄씩 읽기
    for line in f:
        print(line.strip())  # 개행 제거 후 출력
