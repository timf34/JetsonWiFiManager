import time

from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/')
def index() -> str:
    return '''
            <html>
            <head>
                <title>FOV WiFi</title>
            </head>
            <body>
                <h1>FOV WiFi Configuration</h1>
                <form method="POST">
                    SSID: <input type="text" name="ssid"><br>
                    Password: <input type="password" name="password"><br>
                    <input type="submit">
                </form>
            </body>
            </html>
        '''


@app.route('/', methods=['POST'])
def post() -> str:
    ssid = request.form.get('ssid')
    password = request.form.get('password')
    with open('wifi_config.txt', 'w') as f:
        f.write(ssid + "\n" + password)
    connect_to_wifi()
    return 'SSID and password submitted. Attempting to connect...'


def connect_to_wifi() -> None:
    with open('wifi_config.txt', 'r') as f:
        lines = f.readlines()
        ssid = lines[0].strip()
        password = lines[1].strip()

    # stop the AP
    os.system('sudo systemctl stop dnsmasq')
    os.system('sudo systemctl stop hostapd')

    time.sleep(10)

    # restart NetworkManager
    os.system('sudo systemctl start NetworkManager')
    os.system('nmcli device wifi list')

    time.sleep(10)

    os.system('nmcli device wifi list')

    # try to connect to WiFi
    os.system(f'nmcli d wifi connect {ssid} password {password}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
