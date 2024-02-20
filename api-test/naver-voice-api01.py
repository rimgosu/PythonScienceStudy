import os
import sys
import urllib.request

"""음성 합성에 사용할 목소리 종류

nara : 아라: 한국어, 여성 음색
nara_call : 아라(상담원): 한국어, 여성 음색
nminyoung : 민영: 한국어, 여성 음색
nyejin : 예진: 한국어, 여성 음색
mijin : 미진: 한국어, 여성 음색
jinho : 진호: 한국어, 남성 음색
nminsang : 민상: 한국어, 남성 음색
nsinu : 신우: 한국어, 남성 음색
nhajun : 하준: 한국어, 아동 음색 (남)
ndain : 다인: 한국어, 아동 음색 (여)
njiyun : 지윤: 한국어, 여성 음색
nsujin : 수진: 한국어, 여성 음색
njinho : 진호: 한국어, 남성 음색
njihun : 지훈: 한국어, 남성 음색
njooahn : 주안: 한국어, 남성 음색
nseonghoon : 성훈: 한국어, 남성 음색
njihwan : 지환: 한국어, 남성 음색
nsiyoon : 시윤: 한국어, 남성 음색
ngaram : 가람: 한국어, 아동 음색 (여)
ngoeun : 고은: 한국어, 여성 음색
neunyoung : 은영: 한국어, 여성 음색
nsunkyung : 선경: 한국어, 여성 음색
nyujin : 유진: 한국어, 여성 음색
ntaejin : 태진: 한국어, 남성 음색
nyoungil : 영일: 한국어, 남성 음색
nseungpyo : 승표: 한국어, 남성 음색
nwontak : 원탁: 한국어, 남성 음색
dara_ang : 아라(화남):  한국어, 여성 음색
nsunhee : 선희:  한국어, 여성 음색
nminseo : 민서:  한국어, 여성 음색
njiwon : 지원:  한국어, 여성 음색
nbora : 보라:  한국어, 여성 음색
njonghyun: 종현:  한국어, 남성 음색
njoonyoung : 준영:  한국어, 남성 음색
njaewook: 재욱:  한국어, 남성 음색
nes_c_hyeri: 혜리: 한국어, 여성 음색
nes_c_sohyun: 소현: 한국어, 여성 음색
nes_c_mikyung: 미경: 한국어, 여성 음색
nes_c_kihyo: 기효: 한국어, 남성 음색
ntiffany: 기서: 한국어, 여성 음색
napple: 늘봄: 한국어, 여성 음색
njangj: 드림: 한국어, 여성 음색
noyj: 봄달: 한국어, 여성 음색
neunseo: 은서: 한국어, 여성 음색
nheera: 희라: 한국어, 여성 음색
nyoungmi: 영미: 한국어, 여성 음색
nnarae: 나래: 한국어, 여성 음색
nyeji: 예지: 한국어, 여성 음색
nyuna: 유나: 한국어, 여성 음색
nkyunglee: 경리: 한국어, 여성 음색
nminjeong: 민정: 한국어, 여성 음색
nihyun: 이현: 한국어, 여성 음색
nraewon: 래원: 한국어, 남성 음색
nkyuwon : 규원: 한국어, 남성 음색
nkitae: 기태: 한국어, 남성 음색
neunwoo: 은우: 한국어, 남성 음색
nkyungtae: 경태: 한국어, 남성 음색
nwoosik: 우식: 한국어, 남성 음색
vara: 아라(pro): 한국어, 여성 음색
vmikyung: 미경(pro): 한국어, 여성 음색
vdain: 다인(pro): 한국어, 여성 음색
vyuna: 유나(pro): 한국어, 여성 음색
vhyeri: 혜리(pro): 한국어, 여성 음색
dara-danna: 아라&안나: 한국어+영어(미국), 여성 음색
dsinu-matt: 신우&매트: 한국어+영어(미국), 남성 음색
nsabina : 마녀 사비나: 한국어, 여성 음색
nmammon : 악마 마몬: 한국어, 남성 음색
nmeow : 야옹이: 한국어, 아동 음색 (여)
nwoof : 멍멍이: 한국어, 아동 음색 (남)
nreview : 박리뷰: 한국어, 남성 음색
nyounghwa : 정영화: 한국어, 여성 음색
nmovie : 최무비: 한국어, 남성 음색
nsangdo : 상도: 한국어, 남성 음색
nshasha : 샤샤: 한국어, 여성 음색
nian : 이안: 한국어, 남성 음색
ndonghyun : 동현: 한국어, 남성 음색
vian : 이안(pro): 한국어, 남성 음색
vdonghyun : 동현(pro): 한국어, 남성 음색
vgoeun : 고은(pro): 한국어, 여성 음색
vdaeseong : 대성(pro): 한국어, 남성 음색
ngyeongjun : 경준: 한국어, 남성 음색
ndaeseong : 대성: 한국어, 남성 음색
njonghyeok : 종혁: 한국어, 남성 음색
"""

client_id = os.getenv('NAVER_CLIENT_ID')
client_secret = os.getenv('NAVER_CLIENT_SECRET')
encText = urllib.parse.quote("성원아 지우야 안녕?")
data = "speaker=nhajun&volume=0&speed=0&pitch=0&format=mp3&text=" + encText
url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
request = urllib.request.Request(url)
request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
request.add_header("X-NCP-APIGW-API-KEY",client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()
if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('1111.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)