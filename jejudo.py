import os
import pandas as pd
import folium
import streamlit as st
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

# 데이터 로드
st.write("### 제주특별자치도 태양광에너지 발전시설 현황")
df2 = pd.read_csv('제주특별자치도_신재생에너지발전시설현황_20221116.csv', encoding='cp949')

# 원동력종류가 '태양광'인 데이터만 필터링
df2 = df2[df2['원동력종류'] == '태양광']
df2.reset_index(drop=True, inplace=True)

# 주소 리스트
geo_addr = df2['설치장소'].unique()

# 주소를 위도와 경도로 변환하는 함수
def geocoding(address):
    geolocoder = Nominatim(user_agent='South korea', timeout=None)
    geo = geolocoder.geocode(address)
    if geo is None:
        return None, None
    else:
        return geo.latitude, geo.longitude

# 주소를 위도와 경도로 변환
unique_addr = []
unique_lat = []
unique_lng = []

progress_text = st.empty()


# 지오코딩 작업을 한 번에 처리하고, 하나씩 업데이트하지 않음
with st.spinner('위도와 경도로 변환 중...'):
    for addr in geo_addr:
        lat, lng = geocoding(addr)
        if lat is None or lng is None:
            continue
        unique_addr.append(addr)
        unique_lat.append(lat)
        unique_lng.append(lng)

# 변환된 결과를 데이터프레임으로 저장
df_unique = pd.DataFrame({'주소': unique_addr, '경도(x)': unique_lng, '위도(y)': unique_lat})


# Folium을 사용하여 marker 표시하기
jeju_map = folium.Map(location=[33.38, 126.55], zoom_start=11)

for i in range(len(df_unique)):
    pos_list = [df_unique.iloc[i]['위도(y)'], df_unique.iloc[i]['경도(x)']]
    folium.Marker(pos_list, popup=df_unique.iloc[i]['주소']).add_to(jeju_map)

# Streamlit에서 Folium 지도 출력
folium_static(jeju_map)