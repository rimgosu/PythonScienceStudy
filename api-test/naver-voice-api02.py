import os
import sys
import urllib.request

voice_lst = [
'nara', 'nara_call', 'nminyoung', 'nyejin', 'mijin', 'jinho', 'nminsang', 'nsinu', 'nhajun', 'ndain', 'njiyun',
'nsujin', 'njinho', 'njihun', 'njooahn', 'nseonghoon', 'njihwan', 'nsiyoon', 'ngaram', 'ngoeun', 'neunyoung', 'nsunkyung',
'nyujin', 'ntaejin', 'nyoungil', 'nseungpyo', 'nwontak', 'dara_ang', 'nsunhee', 'nminseo', 'njiwon', 'nbora', 'njonghyun',
'njoonyoung', 'njaewook', 'nes_c_hyeri', 'nes_c_sohyun', 'nes_c_mikyung', 'nes_c_kihyo', 'ntiffany', 'napple', 'njangj',
'noyj', 'neunseo', 'nheera', 'nyoungmi', 'nnarae', 'nyeji', 'nyuna', 'nkyunglee', 'nminjeong', 'nihyun', 'nraewon', 'nkyuwon',
'nkitae', 'neunwoo', 'nkyungtae', 'nwoosik', 'vara', 'vmikyung', 'vdain', 'vyuna', 'vhyeri', 'dara-danna', 'dsinu-matt', 'nsabina',
'nmammon', 'nmeow', 'nwoof', 'nreview', 'nyounghwa', 'nmovie', 'nsangdo', 'nshasha', 'nian', 'ndonghyun', 'vian', 'vdonghyun', 
'vgoeun', 'vdaeseong', 'ngyeongjun', 'ndaeseong', 'njonghyeok'
]

def make_mp3(voice, message, speed=5, pitch=5, alpha=5):
    client_id = os.getenv('NAVER_CLIENT_ID')
    client_secret = os.getenv('NAVER_CLIENT_SECRET')
    encText = urllib.parse.quote(message)
    data = f"speaker={voice}&volume=0&speed={speed}&pitch={pitch}&format=mp3&alpha={alpha}&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/tts-premium/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode==200):
        print(f"{voice} TTS mp3 저장")
        response_body = response.read()
        with open(f'./24-02-20/{voice}.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)

message = '성원아, 지우야, 동재야, 동욱아, 안녕? 반가워. 난 그리야. 잘부탁해!'
for voice in voice_lst:
    make_mp3(voice, message)