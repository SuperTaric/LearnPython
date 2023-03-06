from datetime import datetime

def log(text):
    print(text)
    with open('./automatic.log', mode='a') as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': ' + text + '\n')