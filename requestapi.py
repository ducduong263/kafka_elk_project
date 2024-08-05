from confluent_kafka import Producer
import json
import requests
from datetime import datetime, timezone
import pytz

# Khởi tạo Producer Kafka
p = Producer({'bootstrap.servers': 'localhost:9092'})

coordinates = [
    {"name": "Ho Chi Minh", "lon": 106.666672, "lat": 10.75},
    {"name": "Ha Noi", "lon": 105.841171, "lat": 21.0245},
    {"name": "Da Nang", "lon": 108.220833, "lat": 16.06778}
]

part = "minutely,hourly,daily"
api_key = "1bef61e5d3e122984de2d9b700f1e7f7"

for coord in coordinates:
    name = coord["name"]
    lat = coord["lat"]
    lon = coord["lon"]

    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&exclude={part}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        data['name'] = name

        # Chuyển đổi thời gian dt từ Unix timestamp sang chuỗi datetime
        dt_utc = datetime.fromtimestamp(data['current']['dt'], tz=timezone.utc)
        dt_vietnam = dt_utc.astimezone(pytz.timezone('Asia/Ho_Chi_Minh'))
        data['current']['dt'] = dt_vietnam.strftime('%Y-%m-%d %H:%M:%S')

        # Chuyển đổi thời gian sunrise và sunset từ Unix timestamp sang chuỗi datetime
        dt_sunrise_utc = datetime.fromtimestamp(data['current']['sunrise'], tz=timezone.utc)
        dt_sunset_utc = datetime.fromtimestamp(data['current']['sunset'], tz=timezone.utc)

        tz_vietnam = pytz.timezone('Asia/Ho_Chi_Minh')
        dt_sunrise_vietnam = dt_sunrise_utc.astimezone(tz_vietnam)
        dt_sunset_vietnam = dt_sunset_utc.astimezone(tz_vietnam)

        data['current']['sunrise'] = dt_sunrise_vietnam.strftime('%Y-%m-%d %H:%M:%S')
        data['current']['sunset'] = dt_sunset_vietnam.strftime('%Y-%m-%d %H:%M:%S')

        print(data)
        # Đẩy dữ liệu vào Kafka
        p.produce('weather', key=name.encode('utf-8'), value=json.dumps(data))

        p.flush()

    else:
        print(f"Failed to retrieve data for {name}")