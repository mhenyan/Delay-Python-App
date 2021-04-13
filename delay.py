import time
import requests
import threading
from flask import Flask, request, Response, abort


app = Flask(__name__)

@app.route('/delay', methods=['POST'])


def webhook():
    data = request.get_json()
    
    if request.method == "POST":
        event = request.json['event']
        delay = request.json['delay']
        key = request.json['key']
        print(request.json)
        print ("Starting my_delay")
        def my_delay(**kwargs):
            your_params = kwargs.get('post_data', {})
            print('your_params:', your_params)
            event = your_params['event']
            delay = your_params['delay']
            key = your_params['key']
            print('Waiting for ' + str(delay) + ' seconds')
            time.sleep(delay)
            print("waiting completed")
            webhook_url = "https://maker.ifttt.com/trigger/" + event + "/with/key/" + key
            print("posting to " + webhook_url)
            r = requests.post(webhook_url)

        thread = threading.Thread(target=my_delay, kwargs={'post_data': data})
        thread.start()

        #print('Waiting for ' + str(delay) + ' seconds')
        #time.sleep(delay)
        #print("waiting completed")
        #webhook_url = "https://maker.ifttt.com/trigger/" + event + "/with/key/" + key
        #print("posting to " + webhook_url)
        #r = requests.post(webhook_url)
        
        return 'success', 200
    else:
        abort(400)
    


if __name__ == '__main__':
    app.run()