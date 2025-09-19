import os

DATA_FILE = r"C:\edumgt-java-education\java-education-007\isam_data.dat"
RECORD_SIZE = 120  # 레코드 크기

# ------------------------
# 파일 덤프 확인
# ------------------------
def dump_isam_file():
    if not os.path.exists(DATA_FILE):
        print("⚠️ 데이터 파일이 존재하지 않습니다:", DATA_FILE)
        return

    with open(DATA_FILE, "rb") as f:
        pos = 0
        while True:
            buffer = f.read(RECORD_SIZE)
            if not buffer:
                break
            raw = buffer.decode("utf-8", errors="ignore")
            print(f"[pos={pos}] {repr(raw)}")
            pos += RECORD_SIZE

if __name__ == "__main__":
    dump_isam_file()
