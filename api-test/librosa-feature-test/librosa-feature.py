import librosa
import numpy as np

frame_length = 2048

# 음성 파일 로드
file_path = 'dara_ang.mp3' # 음성 파일 경로를 지정하세요.
y, sr = librosa.load(file_path, sr=None)

# MFCC 추출
mfccs = librosa.feature.mfcc(y=y, sr=sr)

# Chroma feature 추출
chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

# Spectral Contrast 추출
spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)

# Zero Crossing Rate 추출
zero_crossing_rate = librosa.feature.zero_crossing_rate(y)

# Pitch 추출
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
pitch = np.mean(pitches, axis=1)

# Energy 추출
energy = np.array([
    np.sum(np.abs(y[i:i+frame_length]**2))
    for i in range(0, len(y), frame_length)
])

print("MFCCs:", mfccs.shape)
print("Chromagram:", chromagram.shape)
print("Spectral Contrast:", spectral_contrast.shape)
print("Zero Crossing Rate:", zero_crossing_rate.shape)
print("Pitch:", pitch.shape)
print("Energy:", energy.shape)
