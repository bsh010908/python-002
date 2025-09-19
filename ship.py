import os

DATA_FILE = "C:\edumgt-java-education\java-education-007\isam_data.dat"
INDEX_FILE = "isam_index.dat"
RECORD_SIZE = 80  # ID + 항구명 고정 길이 (UTF-8)

def insert_record(id, port_name):
    # 데이터 파일 열기 (없으면 생성, 있으면 이어쓰기)
    with open(DATA_FILE, "ab+") as data_file, open(INDEX_FILE, "a", encoding="utf-8") as index_file:
        pos = data_file.tell()  # 현재 파일 끝 위치

        # ID (5자리)
        id_str = f"{id:05d}".encode("utf-8")

        # 항구명 (고정 70바이트)
        name_bytes = port_name.encode("utf-8")
        name_fixed = name_bytes[:70] + b' ' * (70 - len(name_bytes)) if len(name_bytes) < 70 else name_bytes[:70]

        # 레코드 = ID + 구분자 + 이름
        record = id_str + b"|" + name_fixed

        # 크기 맞추기
        if len(record) < RECORD_SIZE:
            record += b' ' * (RECORD_SIZE - len(record))

        data_file.write(record)
        index_file.write(f"{id},{pos}\n")

def find_record(id):
    with open(DATA_FILE, "rb") as data_file, open(INDEX_FILE, "r", encoding="utf-8") as index_file:
        for line in index_file:
            key, pos = line.strip().split(",")
            if int(key) == id:
                data_file.seek(int(pos))
                buffer = data_file.read(RECORD_SIZE)
                return buffer.decode("utf-8").strip()
    return None


if __name__ == "__main__":
    # 테스트용 데이터 (일부만)
    ports = [
        (1001, "Los Angeles"),
        (1002, "Long Beach"),
        (2001, "Tokyo"),
        (2002, "Yokohama"),
        (3001, "Veracruz"),
        (3002, "Manzanillo")
    ]

    # 파일 초기화
    if os.path.exists(DATA_FILE): os.remove(DATA_FILE)
    if os.path.exists(INDEX_FILE): os.remove(INDEX_FILE)

    # 레코드 저장
    for pid, name in ports:
        insert_record(pid, name)

    # 검색
    print("찾은 레코드:", find_record(2001))  # Tokyo
    print("찾은 레코드:", find_record(3002))  # Manzanillo
