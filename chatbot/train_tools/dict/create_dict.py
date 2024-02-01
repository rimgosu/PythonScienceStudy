import sys
sys.path.append('c:/flyai/chatbot')
from utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

# 말뭉치 데이터 읽어오기
def read_corpus_data(filename):
	with open(filename, "r", encoding='utf8') as f:
		data = [line.split("\t") for line in f.read().splitlines()]
		data = data[1:] # 헤더 제거
	return data

# 말뭉치 데이터 가져오기
corpus_data = read_corpus_data("./corpus.txt")

# 말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess()
dict = []
for c in corpus_data:
	pos = p.pos(c[1])
	for k in pos:
		dict.append(k[0])

# 사전에 사용될 단어 인덱스 딕셔너리(word_index) 생성
tokenizer = preprocessing.text.Tokenizer(oov_token="OOV")
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

# 사전 파일 생성
f = open("chatbot_dict.bin", "wb")
try:
	pickle.dump(word_index, f)
except Exception as e:
	print(e)
finally:
	f.close()