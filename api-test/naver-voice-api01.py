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
def make_gif(text):
    client_id = '9pqbfiis28'
    client_secret = '5mcrIscYBSnTHudeCgDJ1wUKUcXu5Hq0dgPHZNms'
    encText = urllib.parse.quote(text)
    data = "speaker=nmammon&volume=0&speed=0&pitch=0&format=mp3&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
    request.add_header("X-NCP-APIGW-API-KEY", client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode == 200):
        print("TTS mp3 저장")
        response_body = response.read()
        # 파일 이름에서 물음표를 공백으로 대체
        safe_filename = text.replace('?', ' ')
        with open(f'{safe_filename}.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)

text = '앞으로도 재밌게 놀아보자!'
make_gif(text)


"""
이것으로 그리닷의 소개를 마치도록 하지.
그리닷은 아이에게 무한한 재미를 줄 거야.
앞으로도 재밌게 놀아보자!
"""

"""
이젠 생성형 AI를 이용해서 아이 그림을 업그레이드 시켜볼거야.
어떤 스타일로 업그레이드할 지만 정하면 돼
잠시 기다리고 네개의 그림중 원하는 걸 고르면 돼.
원하는 그림을 정해줘.
대단하군! 벌써 업그레이드 된 친구가 나왔어.
생성된 김에 인사나 해보지
안녕. 반갑군
"""

"""
아주 훌륭하군!
이제 나 마몬이 설명하겠다.
아이가 친구와 대화를 하면 기록이 남을 것이고,
부모들은 대화 내용이 궁금하겠지?
리포트 보기 버튼을 눌러 아이의 대화 기록을 살펴보도록 하지.
잠시 기다리면 아이의 감정 상태 분류를 볼 수 있고
각각 클릭하면 더 자세한 정보를 볼 수 있지
밑으로 내리면 전체 대화 내용과 
하루 대화 요약을 받아볼 수 있어
아이 정서 파악에 도움이 되겠군!
"""