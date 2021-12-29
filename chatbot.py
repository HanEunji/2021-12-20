# https://needjarvis.tistory.com/639?category=887223 의 코드를 따라 공부합니다.
# Rule-Based 챗봇 만들기
import pandas as pd

chatbot_data = pd.read_excel("C:/Workspace/04.project/chatbot_data.xlsx")
print(chatbot_data)

# rule 저장
chat_dic = {}
row = 0
for rule in chatbot_data['rule']:
    chat_dic[row] = rule.split('|')
    row += 1

print(chat_dic)

# 챗봇 함수
def chat(request):
    for k, v in chat_dic.items():
        index = -1
        for word in v:
            try:
                if index == -1:
                    index = request.index(word)
                else:
                    if index < request.index(word, index):
                        index = request.index(word, index):
                    else:
                        index = -1
                        break
            except ValueError:
                index = -1
                break
        if index > -1:
            return chatbot_data['response'][k]
    return '무슨 말인지 모르겠어요.'

while True:
    req = input('대화를 시작해 보세요!')
    if req == 'exit':
        break
    else:
        print('jarvis : ', chat(req))
