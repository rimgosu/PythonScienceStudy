import time
import requests
import os
from tqdm import tqdm

# 시간 측정 시작
start_time = time.time()

url = "https://api.openai.com/v1/audio/speech"
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

voices = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']

for voice in tqdm(voices, desc="Generating Speech Files"):
    payload = {
        "model": "tts-1",
        "input": "안녕 동욱아! 안녕 지우야! 안녕 동재야! 안녕 성원아! 반가워!",
        "voice": voice
    }
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}", # OPENAI_API_KEY를 실제 키로 교체해야 합니다.
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    with open(f'voices/{voice}_speech.mp3', 'wb') as f:
        f.write(response.content)

# 시간 측정 종료
end_time = time.time()

# 전체 실행 시간 계산 (초 단위)
total_time = end_time - start_time

print(f"작업을 완료하는 데 걸린 시간: {total_time}초")