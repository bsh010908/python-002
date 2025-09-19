from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import math

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
# Fake Port 데이터
# ------------------------
FAKE_PORTS = [
    {"id": "1001", "port": "Los Angeles", "lat": 33.7406, "lon": -118.276},
    {"id": "2001", "port": "Tokyo", "lat": 35.6762, "lon": 139.6503},
    {"id": "3001", "port": "Veracruz", "lat": 19.1738, "lon": -96.1342},
]

# ------------------------
# Fake Ship 데이터 (동적 시뮬레이션)
# ------------------------
FAKE_SHIP = {
    "id": "SHIP01",
    "lat": 35.6762,    # Tokyo 출발
    "lon": 139.6503,
    "route": [
        {"lat": 35.6762, "lon": 139.6503},   # Tokyo
        {"lat": 38.0, "lon": 170.0},         # Pacific mid
        {"lat": 33.7406, "lon": -118.276},   # Los Angeles
        {"lat": 25.0, "lon": -110.0},        # Mexico Gulf entry
        {"lat": 19.1738, "lon": -96.1342}    # Veracruz
    ],
    "routeIndex": 1
}

# 이동 속도 (km 단위)
SPEED = 500.0

# ------------------------
# 거리 계산 (Haversine formula)
# ------------------------
def distance(lat1, lon1, lat2, lon2):
    R = 6371
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = (math.sin(dLat/2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dLon/2) ** 2)
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

# ------------------------
# Port API
# ------------------------
@app.get("/ports")
def list_ports():
    """모든 항구 데이터 리턴"""
    return FAKE_PORTS

@app.get("/ports/{port_id}")
def get_port(port_id: str):
    """특정 ID의 항구 검색"""
    for port in FAKE_PORTS:
        if port["id"] == port_id:
            return port
    raise HTTPException(status_code=404, detail="Port not found")

# ------------------------
# Ship API
# ------------------------
@app.get("/ship")
def get_ship():
    """배 현재 위치 반환 (매 호출마다 조금씩 이동)"""
    ship = FAKE_SHIP
    route = ship["route"]
    idx = ship["routeIndex"]

    target = route[idx]
    d = distance(ship["lat"], ship["lon"], target["lat"], target["lon"])

    # 도착했으면 다음 목적지로
    if d < 50:
        ship["routeIndex"] = (ship["routeIndex"] + 1) % len(route)
        target = route[ship["routeIndex"]]
        d = distance(ship["lat"], ship["lon"], target["lat"], target["lon"])

    # 비율로 이동 (단순 선형 보간)
    ratio = min(1.0, SPEED / d)
    ship["lat"] += (target["lat"] - ship["lat"]) * ratio
    ship["lon"] += (target["lon"] - ship["lon"]) * ratio

    return ship
