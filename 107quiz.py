import json

dict = [{'question':'How do we print comunicates in Python?',
'answers':[{'text':'put', 'correct':False},{'text':'write', 'correct':False},{'text':'print', 'correct':True}]},
{'question':'Count 2+2?',
'answers':[{'text':'4', 'correct':True},{'text':'5', 'correct':False},{'text':'7', 'correct':False}]}]

x = json.dumps(dict, indent=4)

with open('quiz.json', 'w') as file:
    file.write(x)