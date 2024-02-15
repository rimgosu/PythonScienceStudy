from pathlib import Path
from openai import OpenAI
import time
from tqdm import tqdm

voices = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']

# 시간 측정 시작
start_time = time.time()

for voice in tqdm(voices, desc="Generating Speech Files"):
    client = OpenAI()
    speech_file_path = Path(__file__).parent / f"voices2/{voice}_speech.mp3"
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice=voice,
        input="안녕 동욱아! 지우야! 동재야! 반가워!"
    )

    # 파일로 스트리밍하는 부분은 예제 코드에 포함되어 있지 않으므로 이 부분은 가정입니다.
    response.stream_to_file(speech_file_path)

# 시간 측정 종료
end_time = time.time()

# 전체 실행 시간 계산 (초 단위)
total_time = end_time - start_time

print(f"작업을 완료하는 데 걸린 시간: {total_time}초")
