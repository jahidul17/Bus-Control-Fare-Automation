import math

loc_coords = {
    "Badda": (23.7806, 90.4200),
    "Jatrabari": (23.7255, 90.4250),
    "Gulshan": (23.7800, 90.4100)
}

def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def fare_calc(distance_km):
    if distance_km <= 2:
        return 10.0
    else:
        return 10.0 + (distance_km - 2) * 3.0


