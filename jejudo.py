{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "61812521-5f5c-43bf-a79f-092341ea1a5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "pd.set_option('mode.chained_assignment', None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "3bfc6839-c761-4da4-a941-77723b570738",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>NO</th>\n",
       "      <th>허가일자</th>\n",
       "      <th>상호</th>\n",
       "      <th>설비용량(KW)</th>\n",
       "      <th>설치장소</th>\n",
       "      <th>상태</th>\n",
       "      <th>사업개시일</th>\n",
       "      <th>데이터기준일자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2006-03-03</td>\n",
       "      <td>오복산전</td>\n",
       "      <td>59.87</td>\n",
       "      <td>제주특별자치도 제주시 한경면 신창리 760번지 2호</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2006-07-11</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   NO        허가일자    상호  설비용량(KW)                          설치장소    상태  \\\n",
       "0   1  2006-03-03  오복산전     59.87  제주특별자치도 제주시 한경면 신창리 760번지 2호  사업개시   \n",
       "\n",
       "        사업개시일     데이터기준일자  \n",
       "0  2006-07-11  2024-06-30  "
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('제주특별자치도_태양광발전소현황_20240630.csv', encoding = 'cp949')\n",
    "df.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "5cd5ca57-85d5-4bfe-984f-be4129a3b2a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1643 entries, 0 to 1642\n",
      "Data columns (total 8 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   NO        1643 non-null   int64  \n",
      " 1   허가일자      1643 non-null   object \n",
      " 2   상호        1643 non-null   object \n",
      " 3   설비용량(KW)  1643 non-null   float64\n",
      " 4   설치장소      1643 non-null   object \n",
      " 5   상태        1643 non-null   object \n",
      " 6   사업개시일     1643 non-null   object \n",
      " 7   데이터기준일자   1643 non-null   object \n",
      "dtypes: float64(1), int64(1), object(6)\n",
      "memory usage: 102.8+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "4c6013a3-ab64-4fad-9b37-8dc6081f2d04",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>NO</th>\n",
       "      <th>허가일자</th>\n",
       "      <th>상호</th>\n",
       "      <th>설비용량(KW)</th>\n",
       "      <th>설치장소</th>\n",
       "      <th>상태</th>\n",
       "      <th>사업개시일</th>\n",
       "      <th>데이터기준일자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2006-03-03</td>\n",
       "      <td>오복산전</td>\n",
       "      <td>59.87</td>\n",
       "      <td>제주특별자치도 제주시 한경면 신창리 760번지 2호</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2006-07-11</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2006-08-24</td>\n",
       "      <td>오복산전 3호</td>\n",
       "      <td>29.52</td>\n",
       "      <td>제주특별자치도 제주시 한경면 신창리 760번지 3호</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2006-09-25</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2007-01-05</td>\n",
       "      <td>민솔라에너지</td>\n",
       "      <td>90.72</td>\n",
       "      <td>제주특별자치도 제주시 조천읍 대흘리 110번지 4호</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2007-04-04</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2007-02-21</td>\n",
       "      <td>(주)도암엔지니어링건축사사무소</td>\n",
       "      <td>3.00</td>\n",
       "      <td>제주특별자치도 제주시 한경면 일주서로 4716-8</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2007-02-27</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2007-02-21</td>\n",
       "      <td>제주에너지 주식회사</td>\n",
       "      <td>200.00</td>\n",
       "      <td>제주특별자치도 서귀포시 성산읍 신산리 1960번지</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2008-09-29</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1638</th>\n",
       "      <td>1639</td>\n",
       "      <td>2021-04-30</td>\n",
       "      <td>가시일 태양광발전소</td>\n",
       "      <td>398.39</td>\n",
       "      <td>제주특별자치도 서귀포시 표선면 가시리 677번지</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2023-04-27</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1639</th>\n",
       "      <td>1640</td>\n",
       "      <td>2021-08-03</td>\n",
       "      <td>태양7호태양광발전소</td>\n",
       "      <td>198.88</td>\n",
       "      <td>제주특별자치도 서귀포시 안덕면 상천리 764-4</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2021-12-10</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1640</th>\n",
       "      <td>1641</td>\n",
       "      <td>2021-08-03</td>\n",
       "      <td>종달2호태양광발전소</td>\n",
       "      <td>99.00</td>\n",
       "      <td>제주특별자치도 제주시 구좌읍 종달리 3785번지 .3787.3785-3</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2023-12-26</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1641</th>\n",
       "      <td>1642</td>\n",
       "      <td>2021-09-15</td>\n",
       "      <td>흥산태양광발전소</td>\n",
       "      <td>999.63</td>\n",
       "      <td>제주특별자치도 제주시 구좌읍 행원리 2686번지 .2694</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2022-04-25</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1642</th>\n",
       "      <td>1643</td>\n",
       "      <td>2021-10-15</td>\n",
       "      <td>진영태양광발전소</td>\n",
       "      <td>99.45</td>\n",
       "      <td>제주특별자치도 제주시 구좌읍 한동리 3825-2</td>\n",
       "      <td>사업개시</td>\n",
       "      <td>2023-07-25</td>\n",
       "      <td>2024-06-30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1643 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        NO        허가일자                상호  설비용량(KW)  \\\n",
       "0        1  2006-03-03              오복산전     59.87   \n",
       "1        2  2006-08-24           오복산전 3호     29.52   \n",
       "2        3  2007-01-05            민솔라에너지     90.72   \n",
       "3        4  2007-02-21  (주)도암엔지니어링건축사사무소      3.00   \n",
       "4        5  2007-02-21        제주에너지 주식회사    200.00   \n",
       "...    ...         ...               ...       ...   \n",
       "1638  1639  2021-04-30        가시일 태양광발전소    398.39   \n",
       "1639  1640  2021-08-03        태양7호태양광발전소    198.88   \n",
       "1640  1641  2021-08-03        종달2호태양광발전소     99.00   \n",
       "1641  1642  2021-09-15          흥산태양광발전소    999.63   \n",
       "1642  1643  2021-10-15          진영태양광발전소     99.45   \n",
       "\n",
       "                                         설치장소    상태       사업개시일     데이터기준일자  \n",
       "0                제주특별자치도 제주시 한경면 신창리 760번지 2호  사업개시  2006-07-11  2024-06-30  \n",
       "1                제주특별자치도 제주시 한경면 신창리 760번지 3호  사업개시  2006-09-25  2024-06-30  \n",
       "2                제주특별자치도 제주시 조천읍 대흘리 110번지 4호  사업개시  2007-04-04  2024-06-30  \n",
       "3                 제주특별자치도 제주시 한경면 일주서로 4716-8  사업개시  2007-02-27  2024-06-30  \n",
       "4                 제주특별자치도 서귀포시 성산읍 신산리 1960번지  사업개시  2008-09-29  2024-06-30  \n",
       "...                                       ...   ...         ...         ...  \n",
       "1638               제주특별자치도 서귀포시 표선면 가시리 677번지  사업개시  2023-04-27  2024-06-30  \n",
       "1639               제주특별자치도 서귀포시 안덕면 상천리 764-4  사업개시  2021-12-10  2024-06-30  \n",
       "1640  제주특별자치도 제주시 구좌읍 종달리 3785번지 .3787.3785-3  사업개시  2023-12-26  2024-06-30  \n",
       "1641         제주특별자치도 제주시 구좌읍 행원리 2686번지 .2694  사업개시  2022-04-25  2024-06-30  \n",
       "1642               제주특별자치도 제주시 구좌읍 한동리 3825-2  사업개시  2023-07-25  2024-06-30  \n",
       "\n",
       "[1643 rows x 8 columns]"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#사업개시일이 있는 데이터만 골라낸다.\n",
    "#사업개시일이 없는 데이터는 아직 인허가가 진행중이므로 drop한다.\n",
    "df = df.dropna(axis = 0)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "c1678bf9-2ed4-4cb8-9f65-7fe42158c8c4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>NO</th>\n",
       "      <th>허가일자</th>\n",
       "      <th>상호</th>\n",
       "      <th>설비용량(KW)</th>\n",
       "      <th>설치장소</th>\n",
       "      <th>상태</th>\n",
       "      <th>사업개시일</th>\n",
       "      <th>데이터기준일자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [NO, 허가일자, 상호, 설비용량(KW), 설치장소, 상태, 사업개시일, 데이터기준일자]\n",
       "Index: []"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 사업개시일이 기록되었는데 상태가 '공사진행', '인허가'인 경우\n",
    "df[df['상태'] != '사업개시']\n",
    "#모든 상태가 사업개시인 상태이므로 추가 수정 불필요"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "363eb782-c374-4f20-822d-e9632f903754",
   "metadata": {},
   "outputs": [],
   "source": [
    "#사업개시일을 시간순으로 정렬하기 위해 문자열타입에서 datetime타입으로 변경해준다.\n",
    "df['사업개시일'] = pd.to_datetime(df['사업개시일'])\n",
    "#sort_values함수를 이용해 사업개시일 컬럼값을 기준으로 정렬한다.\n",
    "df.sort_values(by = '사업개시일', inplace = True)\n",
    "\n",
    "#데이터프레임의 인데스를 새롭게 생성한다.\n",
    "df.reset_index(drop = True, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "b172d123-c423-4923-935b-b47a4564e34c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0          풍력\n",
       "1          풍력\n",
       "2          풍력\n",
       "3          풍력\n",
       "4          풍력\n",
       "        ...  \n",
       "1577    바이오가스\n",
       "1578    바이오가스\n",
       "1579    바이오가스\n",
       "1580    바이오가스\n",
       "1581       기타\n",
       "Name: 원동력종류, Length: 1582, dtype: object"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 파일명에는 태양광 발전소 현황이지만 태양광만이 아닌 다른 에너지 발전소 전체의 정보가 포함되어 있음\n",
    "# 상호만으로 태양광 정보를 걸러내기에는 무리가 있어보임.\n",
    "# 원동력종류가 표기된 파일을 추가로 다운받는다.\n",
    "\n",
    "df2 = pd.read_csv('제주특별자치도_신재생에너지발전시설현황_20221116.csv', encoding = 'cp949')\n",
    "df2['원동력종류']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "95251f35-76bd-405a-96ca-1d776016ae9b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>허가일자</th>\n",
       "      <th>상호</th>\n",
       "      <th>설비용량(KW)</th>\n",
       "      <th>설치장소</th>\n",
       "      <th>원동력종류</th>\n",
       "      <th>사업개시일</th>\n",
       "      <th>데이터기준일자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021-09-15</td>\n",
       "      <td>흥산태양광발전소</td>\n",
       "      <td>999.63</td>\n",
       "      <td>제주특별자치도 제주시 구좌읍</td>\n",
       "      <td>태양광</td>\n",
       "      <td>2022-04-25</td>\n",
       "      <td>2022-11-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021-08-03</td>\n",
       "      <td>태양7호태양광발전소</td>\n",
       "      <td>198.88</td>\n",
       "      <td>제주특별자치도 서귀포시 안덕면</td>\n",
       "      <td>태양광</td>\n",
       "      <td>2021-12-10</td>\n",
       "      <td>2022-11-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021-04-21</td>\n",
       "      <td>제주덕암 태양광발전소</td>\n",
       "      <td>99.18</td>\n",
       "      <td>제주특별자치도 서귀포시 표선면</td>\n",
       "      <td>태양광</td>\n",
       "      <td>2022-01-03</td>\n",
       "      <td>2022-11-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021-04-19</td>\n",
       "      <td>청춘 태양광발전소</td>\n",
       "      <td>662.48</td>\n",
       "      <td>제주특별자치도 서귀포시 안덕면</td>\n",
       "      <td>태양광</td>\n",
       "      <td>2022-01-03</td>\n",
       "      <td>2022-11-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021-04-19</td>\n",
       "      <td>에스원태양광발전소</td>\n",
       "      <td>458.64</td>\n",
       "      <td>제주특별자치도 서귀포시 안덕면</td>\n",
       "      <td>태양광</td>\n",
       "      <td>2022-01-03</td>\n",
       "      <td>2022-11-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1542</th>\n",
       "      <td>2007-02-21</td>\n",
       "      <td>제주에너지 주식회사</td>\n",
       "      <td>200.00</td>\n",
       "      <td>제주특별자치도 서귀포시 성산읍</td>\n",
       "      <td>태양광</td>\n",
       "      <td>2008-09-29</td>\n",
       "      <td>2022-11-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1543</th>\n",
       "      <td>2007-02-21</td>\n",
       "      <td>제주에너지 주식회사</td>\n",
       "      <td>200.00</td>\n",
       "      <td>제주특별자치도 제주시 애월읍</td>\n",
       "      <td>태양광</td>\n",
       "      <td>2008-04-18</td>\n",
       "      <td>2022-11-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1544</th>\n",
       "      <td>2007-01-05</td>\n",
       "      <td>민솔라에너지</td>\n",
       "      <td>90.72</td>\n",
       "      <td>제주특별자치도 제주시 조천읍</td>\n",
       "      <td>태양광</td>\n",
       "      <td>2007-04-04</td>\n",
       "      <td>2022-11-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1545</th>\n",
       "      <td>2006-08-24</td>\n",
       "      <td>오복산전 3호</td>\n",
       "      <td>29.52</td>\n",
       "      <td>제주특별자치도 제주시 한경면</td>\n",
       "      <td>태양광</td>\n",
       "      <td>2006-09-25</td>\n",
       "      <td>2022-11-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1546</th>\n",
       "      <td>2006-03-03</td>\n",
       "      <td>오복산전</td>\n",
       "      <td>59.87</td>\n",
       "      <td>제주특별자치도 제주시 한경면</td>\n",
       "      <td>태양광</td>\n",
       "      <td>2006-07-11</td>\n",
       "      <td>2022-11-16</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1547 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            허가일자           상호  설비용량(KW)              설치장소 원동력종류       사업개시일  \\\n",
       "0     2021-09-15     흥산태양광발전소    999.63   제주특별자치도 제주시 구좌읍   태양광  2022-04-25   \n",
       "1     2021-08-03   태양7호태양광발전소    198.88  제주특별자치도 서귀포시 안덕면   태양광  2021-12-10   \n",
       "2     2021-04-21  제주덕암 태양광발전소     99.18  제주특별자치도 서귀포시 표선면   태양광  2022-01-03   \n",
       "3     2021-04-19    청춘 태양광발전소    662.48  제주특별자치도 서귀포시 안덕면   태양광  2022-01-03   \n",
       "4     2021-04-19    에스원태양광발전소    458.64  제주특별자치도 서귀포시 안덕면   태양광  2022-01-03   \n",
       "...          ...          ...       ...               ...   ...         ...   \n",
       "1542  2007-02-21   제주에너지 주식회사    200.00  제주특별자치도 서귀포시 성산읍   태양광  2008-09-29   \n",
       "1543  2007-02-21   제주에너지 주식회사    200.00   제주특별자치도 제주시 애월읍   태양광  2008-04-18   \n",
       "1544  2007-01-05       민솔라에너지     90.72   제주특별자치도 제주시 조천읍   태양광  2007-04-04   \n",
       "1545  2006-08-24      오복산전 3호     29.52   제주특별자치도 제주시 한경면   태양광  2006-09-25   \n",
       "1546  2006-03-03         오복산전     59.87   제주특별자치도 제주시 한경면   태양광  2006-07-11   \n",
       "\n",
       "         데이터기준일자  \n",
       "0     2022-11-16  \n",
       "1     2022-11-16  \n",
       "2     2022-11-16  \n",
       "3     2022-11-16  \n",
       "4     2022-11-16  \n",
       "...          ...  \n",
       "1542  2022-11-16  \n",
       "1543  2022-11-16  \n",
       "1544  2022-11-16  \n",
       "1545  2022-11-16  \n",
       "1546  2022-11-16  \n",
       "\n",
       "[1547 rows x 7 columns]"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#원동력 종류에서 태양광만 추출하기\n",
    "df2 = df2[df2['원동력종류'] == '태양광']\n",
    "df2.reset_index(drop = True, inplace = True)\n",
    "df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "9a500e9a-509e-450b-b0c9-fde1bebd23a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['제주특별자치도 제주 구좌읍', '제주특별자치도 서귀포 안덕면', '제주특별자치도 서귀포 표선면', '제주특별자치도 서귀포 성산읍', '제주특별자치도 서귀포 법환동', '제주특별자치도 서귀포 대정읍', '제주특별자치도 제주 한림읍', '제주특별자치도 서귀포 남원읍', '제주특별자치도 서귀포 상예동', '제주특별자치도 서귀포 회수동', '제주특별자치도 제주 조천읍', '제주특별자치도 제주 도남동', '제주특별자치도 제주 애월읍', '제주특별자치도 서귀포 토평동', '제주특별자치도 서귀포 강정동', '제주특별자치도 서귀포 중문동', '제주특별자치도 제주 봉개동', '제주특별자치도 서귀포 월평동', '제주특별자치도 제주 용담이동', '제주특별자치도 제주 일도이동', '제주특별자치도 제주 회천동', '제주특별자치도 제주 해안동', '제주특별자치도 서귀포 호근동', '제주특별자치도 제주 오라삼동', '제주특별자치도 제주 한경면', '제주특별자치도 제주 아라이동', '제주특별자치도 제주 오라이동', '제주특별자치도 제주 용강동', '제주특별자치도 제주 외도일동', '제주특별자치도 제주 삼양일동', '제주특별자치도 서귀포 도순동', '제주특별자치도 서귀포 상효동', '제주특별자치도 서귀포 서홍동', '제주특별자치도 제주 이도일동', '제주특별자치도 제주 오등동', '제주특별자치도 서귀포 서호동', '제주특별자치도 제주 영평동', '제주특별자치도 서귀포 동홍동', '제주특별자치도 서귀포 하원동', '제주특별자치도 제주 이호이동', '제주특별자치도 제주 화북이동', '제주특별자치도 서귀포 색달동', '제주특별자치도 서귀포 서귀동', '제주특별자치도 제주 도련이동', '제주특별자치도 제주 오라일동', '제주특별자치도 서귀포 하효동', '제주특별자치도 제주 도평동', '제주특별자치도 서귀포 하예동', '제주특별자치도 제주 노형동', '제주특별자치도 제주 삼도이동', '제주특별자치도 제주 도련일동', '제주특별자치도 제주 아라일동']\n"
     ]
    }
   ],
   "source": [
    "#주소가 중복되는 경우 하나만 출력하기 위해 unique()함수를 사용합니다.\n",
    "geo_addr = df2['설치장소'].unique()\n",
    "\n",
    "geo_pos = []\n",
    "\n",
    "#위도와 경도로 변환시 주소에 '시'가 포함되어 있으면 정상작동 안하기에 '시'를 공백으로대체\n",
    "for addr in geo_addr:\n",
    "    geo_pos.append(addr.replace('시',''))\n",
    "\n",
    "print(geo_pos)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "id": "860284e2-3738-40ff-8233-5e6ab004c8f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#주소값을 geopy패키지를 활용하여 경도와 위도 값을 얻는 함수를 만든다.\n",
    "from geopy.geocoders import Nominatim\n",
    "\n",
    "unique_addr = []\n",
    "unique_lat = []\n",
    "unique_lng = []\n",
    "\n",
    "def geocoding(address):\n",
    "    geolocoder = Nominatim(user_agent = 'South korea', timeout = None)\n",
    "    geo = geolocoder.geocode(address)\n",
    "    if geo == None:\n",
    "        print('geo is null')\n",
    "        return 0, 0\n",
    "    else:\n",
    "        return geo.latitude, geo.longitude\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "855bb203-d32e-47b9-8996-4ee334117bfa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "제주특별자치도 제주 구좌읍\n",
      "33.51662 126.81055\n",
      "제주특별자치도 서귀포 안덕면\n",
      "33.27688 126.34925\n",
      "제주특별자치도 서귀포 표선면\n",
      "33.3504543 126.794049\n",
      "제주특별자치도 서귀포 성산읍\n",
      "33.41805 126.88147\n",
      "제주특별자치도 서귀포 법환동\n",
      "33.24113 126.51285\n",
      "제주특별자치도 서귀포 대정읍\n",
      "33.2218157 126.2529945\n",
      "제주특별자치도 제주 한림읍\n",
      "33.39344 126.26684\n",
      "제주특별자치도 서귀포 남원읍\n",
      "33.3076683 126.6907475\n",
      "제주특별자치도 서귀포 상예동\n",
      "33.26177 126.38678\n",
      "제주특별자치도 서귀포 회수동\n",
      "33.26549 126.44363\n",
      "제주특별자치도 제주 조천읍\n",
      "33.50888 126.66305\n",
      "제주특별자치도 제주 도남동\n",
      "33.4905148 126.5239964\n",
      "제주특별자치도 제주 애월읍\n",
      "33.45079 126.3752\n",
      "제주특별자치도 서귀포 토평동\n",
      "33.2705286 126.5841149\n",
      "제주특별자치도 서귀포 강정동\n",
      "33.24695 126.48927\n",
      "제주특별자치도 서귀포 중문동\n",
      "33.262002 126.4288617\n",
      "제주특별자치도 제주 봉개동\n",
      "33.484188 126.5993497\n",
      "제주특별자치도 서귀포 월평동\n",
      "33.24501 126.46294\n",
      "제주특별자치도 제주 용담이동\n",
      "33.50742 126.50615\n",
      "제주특별자치도 제주 일도이동\n",
      "33.50864 126.53795\n",
      "제주특별자치도 제주 회천동\n",
      "33.4956 126.61479\n",
      "제주특별자치도 제주 해안동\n",
      "33.44899 126.46036\n",
      "제주특별자치도 서귀포 호근동\n",
      "33.25632 126.53351\n",
      "제주특별자치도 제주 오라삼동\n",
      "33.49487 126.50508\n",
      "제주특별자치도 제주 한경면\n",
      "33.3305 126.21066\n",
      "제주특별자치도 제주 아라이동\n",
      "33.48148 126.55055\n",
      "제주특별자치도 제주 오라이동\n",
      "33.47081 126.50991\n",
      "제주특별자치도 제주 용강동\n",
      "33.47017 126.58934\n",
      "제주특별자치도 제주 외도일동\n",
      "33.4855847 126.4284514\n",
      "제주특별자치도 제주 삼양일동\n",
      "33.52345 126.599\n",
      "제주특별자치도 서귀포 도순동\n",
      "33.2569662 126.4731036\n",
      "제주특별자치도 서귀포 상효동\n",
      "33.2896254 126.5945088\n",
      "제주특별자치도 서귀포 서홍동\n",
      "33.25965 126.55175\n",
      "제주특별자치도 제주 이도일동\n",
      "33.5059 126.5278\n",
      "제주특별자치도 제주 오등동\n",
      "33.46148 126.53087\n",
      "제주특별자치도 서귀포 서호동\n",
      "33.25759 126.51916\n",
      "제주특별자치도 제주 영평동\n",
      "33.4812 126.57106\n",
      "제주특별자치도 서귀포 동홍동\n",
      "33.26184 126.56804\n",
      "제주특별자치도 서귀포 하원동\n",
      "33.2626587 126.4600239\n",
      "제주특별자치도 제주 이호이동\n",
      "33.498551 126.4565213\n",
      "제주특별자치도 제주 화북이동\n",
      "33.50469 126.5648\n",
      "제주특별자치도 서귀포 색달동\n",
      "33.2640931 126.4120002\n",
      "제주특별자치도 서귀포 서귀동\n",
      "33.24679 126.56396\n",
      "제주특별자치도 제주 도련이동\n",
      "33.51279 126.59604\n",
      "제주특별자치도 제주 오라일동\n",
      "33.49611 126.51699\n",
      "제주특별자치도 서귀포 하효동\n",
      "33.2582539 126.6179833\n",
      "제주특별자치도 제주 도평동\n",
      "33.47875 126.4515\n",
      "제주특별자치도 서귀포 하예동\n",
      "33.24016 126.3806\n",
      "제주특별자치도 제주 노형동\n",
      "33.4781247 126.4754867\n",
      "제주특별자치도 제주 삼도이동\n",
      "geo is null\n",
      "제주특별자치도 제주 도련일동\n",
      "33.5059 126.5869\n",
      "제주특별자치도 제주 아라일동\n",
      "33.46882 126.54574\n"
     ]
    }
   ],
   "source": [
    "for addr in geo_pos:\n",
    "    print(addr)\n",
    "    lat, lng = geocoding(addr)\n",
    "    if lat == 0 or lng == 0:\n",
    "        continue\n",
    "    unique_addr.append(addr)\n",
    "    unique_lat.append(lat)\n",
    "    unique_lng.append(lng)\n",
    "    print(lat, lng)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "728cfb5e-5056-4506-ab52-b71b2f2170e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>주소</th>\n",
       "      <th>경도(x)</th>\n",
       "      <th>위도(y)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>제주특별자치도 제주 구좌읍</td>\n",
       "      <td>126.810550</td>\n",
       "      <td>33.516620</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>제주특별자치도 서귀포 안덕면</td>\n",
       "      <td>126.349250</td>\n",
       "      <td>33.276880</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>제주특별자치도 서귀포 표선면</td>\n",
       "      <td>126.794049</td>\n",
       "      <td>33.350454</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>제주특별자치도 서귀포 성산읍</td>\n",
       "      <td>126.881470</td>\n",
       "      <td>33.418050</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>제주특별자치도 서귀포 법환동</td>\n",
       "      <td>126.512850</td>\n",
       "      <td>33.241130</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                주소       경도(x)      위도(y)\n",
       "0   제주특별자치도 제주 구좌읍  126.810550  33.516620\n",
       "1  제주특별자치도 서귀포 안덕면  126.349250  33.276880\n",
       "2  제주특별자치도 서귀포 표선면  126.794049  33.350454\n",
       "3  제주특별자치도 서귀포 성산읍  126.881470  33.418050\n",
       "4  제주특별자치도 서귀포 법환동  126.512850  33.241130"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_unique = pd.DataFrame({'주소':unique_addr,\n",
    "                          '경도(x)':unique_lng,\n",
    "                          '위도(y)':unique_lat})\n",
    "df_unique.head()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "576617bb-4342-4941-a864-abcd9a3f3aec",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Folium을 사용하여 marker 표시하기\n",
    "import pandas as pd\n",
    "import folium\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "jeju_map = folium.Map(location=[33.38, 126.55], zoom_start=11)\n",
    "\n",
    "for i in range(len(df_unique)):\n",
    "    pos_list = [df_unique.iloc[i]['위도(y)'], df_unique.iloc[i]['경도(x)']]\n",
    "    folium.Marker(pos_list, popup=df_unique.iloc[i]['주소']).add_to(jeju_map)\n",
    "    \n",
    "jeju_map.save('jeju.html')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8209af5e-3eee-411e-b2ea-c73aaa3c173a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
