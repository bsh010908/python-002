import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

DATA_FILE = r"C:\edumgt-java-education\java-education-007\isam_data.dat"
INDEX_FILE = "isam_index.dat"
RECORD_SIZE = 200  # ID + 항구명 + 위도 + 경도

app = FastAPI(title="Port + Ship API Service")

# ------------------------
# ✅ CORS 설정
# ------------------------
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------
# ISAM 레코드 읽기
# ------------------------
def find_record(id: int):
    with open(DATA_FILE, "rb") as data_file, open(INDEX_FILE, "r", encoding="utf-8") as index_file:
        for line in index_file:
            key, pos = line.strip().split(",")
            if int(key) == id:
                data_file.seek(int(pos))
                buffer = data_file.read(RECORD_SIZE)
                raw = buffer.decode("utf-8", errors="ignore")

                # 필드 파싱 (ID|Name|Lat|Lon)
                parts = raw.split("|")
                if len(parts) >= 4:
                    id_str = parts[0].strip()
                    name_str = parts[1].strip()
                    lat_str = parts[2].replace("|", "").strip()
                    lon_str = parts[3].replace("|", "").strip()

                    try:
                        lat_val = float(lat_str)
                    except ValueError:
                        lat_val = None
                    try:
                        lon_val = float(lon_str)
                    except ValueError:
                        lon_val = None

                    return {
                        "id": id_str,
                        "port": name_str,
                        "lat": lat_val,
                        "lon": lon_val,
                    }
    return None

# ------------------------
# Ports API
# ------------------------
@app.get("/ports")
def list_ports():
    results = []
    if not os.path.exists(INDEX_FILE):
        return results

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        for line in f:
            key, _ = line.strip().split(",")
            rec = find_record(int(key))
            if rec:
                results.append(rec)
    return results

@app.get("/ports/{port_id}")
def get_port(port_id: int):
    record = find_record(port_id)
    if record:
        return record
    raise HTTPException(status_code=404, detail="Port not found")

# ------------------------
# Ship API (Fake JSON)
# ------------------------
FAKE_SHIP = {
    "id": "SHIP01",
    "lat": 35.6762,
    "lon": 139.6503,
    "routeIndex": 1
}

@app.get("/ship")
def get_ship():
    return FAKE_SHIP
