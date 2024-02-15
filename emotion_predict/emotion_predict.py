import torch
from torch import nn
import numpy as np
from torch.utils.data import Dataset, DataLoader
from kobert_tokenizer import KoBERTTokenizer
from transformers import BertModel

device = torch.device('cpu')

class BERTClassifier(nn.Module):
    def __init__(self, hidden_size=768, num_classes=6, dr_rate=0.5):
        super(BERTClassifier, self).__init__()
        self.bert = BertModel.from_pretrained('skt/kobert-base-v1')
        self.dropout = nn.Dropout(p=dr_rate) if dr_rate else None
        self.classifier = nn.Linear(hidden_size, num_classes)
        
    def forward(self, input_ids, attention_mask):
        output = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = output.pooler_output
        if self.dropout:
            pooled_output = self.dropout(pooled_output)
        return self.classifier(pooled_output)

class BERTDataset(Dataset):
    def __init__(self, dataset, tokenizer, max_len):
        self.tokenizer = tokenizer
        self.data = [
            self.tokenizer.encode_plus(
                text=sentence,
                add_special_tokens=True,
                max_length=max_len,
                padding='max_length',
                truncation=True,
                return_tensors="pt"
            ) for sentence, _ in dataset
        ]
        self.labels = [np.int32(label) for _, label in dataset]

    def __getitem__(self, idx):
        item = {key: val.squeeze(0) for key, val in self.data[idx].items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

def load_model(model_path, model, device):
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model

def predict(model, sentence, tokenizer, max_len=64):
    model.eval()
    with torch.no_grad():
        inputs = tokenizer.encode_plus(sentence, return_tensors="pt", max_length=max_len, padding='max_length', truncation=True)
        input_ids = inputs['input_ids'].to(device)
        attention_mask = inputs['attention_mask'].to(device)
        output = model(input_ids, attention_mask)
        _, prediction = torch.max(output, dim=1)
        emotions = ['기쁨', '당황', '분노', '불안', '상처', '슬픔']
        return emotions[prediction.item()]

# 모델 및 토크나이저 초기화
tokenizer = KoBERTTokenizer.from_pretrained('skt/kobert-base-v1')
model = BERTClassifier().to(device)
model = load_model('model_best_5.pth', model, device)

# 예측 실행
sentence = '오늘 하루 정말 최악이야...'
print(f'입력한 문장: {sentence}')
predicted_emotion = predict(model, sentence, tokenizer)
print(f"예측된 감정: {predicted_emotion}")
