import sys
sys.path.append('c:/flyai/chatbot')
from utils.Preprocess import Preprocess
from models.intent.intentModel import IntentModel




p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.tsv')

intent = IntentModel(model_name='../models/intent/intent_model.h5', proprocess=p)

query = "씨벌 전화좀 받아라"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(f'query : {query}')
print(f'predict : {predict}')
print(f'predict_label : {predict_label}')