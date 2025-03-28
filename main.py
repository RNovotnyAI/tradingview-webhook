from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Webhook běží!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print('Přijatý webhook:', data)
    
    # Volitelně: uložit signál do souboru
    with open('signal.txt', 'w') as f:
        f.write(str(data))
    
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run()
