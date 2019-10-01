from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Willzinh')
bot = ChatBot(
    'Willzinh',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

conversa = ListTrainer(bot)
vetor=[
    'Oi?',
    'Eae',
    'Qual o seu nome?',
    'Willzinh, seu amiguinho',
    'Muito prazer ',
    'Igualmente meu consagrado',
    'Coe',
    'will',
    'fala',
    'kd tu',
    'wilber',
    'fala cria',

]
conversa.train(vetor)
while True:
    try:
        entrada=input("Usuário: ")
        resposta = bot.get_response(entrada)

        if float(resposta.confidence) > 0.5:
            print("Willzinh: ", resposta)

        else:
            
            if(len(entrada)==6):
                print('.')
                print('.')
                print('.')
                resposta='petigatou'
        
                #confidence = 0.51
                print(entrada)
                print(vetor)
                print(vetor[0])
                vetor.append(entrada)
                vetor.append(resposta)
                conversa.train(vetor)

            else:
                print("No puedo responder :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
