from json import load

mylist = ['a','b','c']


def is_good():
    choice = input('Which option is correct?: ')

    if choice in mylist:

        if choice == mylist[0]:
            choice = question['answers'][0]['text']
            if question['answers'][0]['correct'] == True:
                print('You Win!')
            if question['answers'][0]['correct'] == False:
                print('You lost')

        elif choice == mylist[1]:
            choice = question['answers'][1]['text']
            if question['answers'][1]['correct'] == True:
                print('You Win!')
            if question['answers'][1]['correct'] == False:
                print('You lost')

        else:
            choice = question['answers'][2]['text']
            if question['answers'][2]['correct'] == True:
                print('You Win!')
            if question['answers'][2]['correct'] == False:
                print('You lost')
    
    else:
        print('There is no choice like this!')
        is_good()


with open('quiz.json') as file:
    questions = load(file)

    for question in questions:
        print()
        print(question['question'])
        print('A.', question['answers'][0]['text'])
        print('B.', question['answers'][1]['text'])
        print('C.', question['answers'][2]['text'])
        print('-----'*10)
        is_good()


