from konlpy.tag import Komoran
import pickle

class Preprocess:
	# 생성자
	def __init__(self, word2index_dic="", userdic=None):
		# 단어 인덱스 사전 불러오기
		if word2index_dic != "":
			f = open(word2index_dic, "rb")
			self.word_index = pickle.load(f)
			f.close()
		else:
			self.word_index = None

		# 형태소 분석기 초기화
		self.komoran = Komoran(userdic=userdic)

		# 제외할 품사
		# 참조: https://docs.komoran.kr/firststep/postypes.html
		self.exclusion_tags = [
			"JKS", "JKC", "JKG", "JKO", "JKB", "JKV", "JKQ", "JX", "JC", # 관계언 제거
			"SF", "SP", "SS", "SE", "SO", # 기호 제거
			"EP", "EF", "EC", "ETN", "ETM", # 어미 제거
			"XSN", "XSV", "XSA", # 접미사 제거
		]

	# 형태소 분석기 POS tagger (래퍼 함수)
	def pos(self, sentence):
		return self.komoran.pos(sentence)

	# 불용어 제거 후 필요한 품사 정보만 가져오기
	def get_keywords(self, pos, without_tag=False):
		f = lambda x: x in self.exclusion_tags
		word_list = []
		for p in pos:
			if f(p[1]) is False: # 불용어 리스트에 없는 경우에만 저장
				word_list.append(p if without_tag is False else p[0])
		return word_list

	# 키워드를 단어 인덱스 시퀀스로 변환
	def get_wordidx_sequence(self, keywords):
		if self.word_index is None:
			return []
		w2i = []
		for word in keywords:
			try:
				w2i.append(self.word_index[word])
			except KeyError:
				# 해당 단어가 사전에 없는 경우 OOV 처리
				w2i.append(self.word_index["OOV"])
		return w2i