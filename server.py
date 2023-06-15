from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data() -> str:
    jsdata = request.form['javascript_data']
    ssid, password = jsdata.split("|")
    with open('wifi_config.txt', 'w') as f:
        f.write(ssid + "\n" + password)

    connect_to_wifi()
    return jsdata


def connect_to_wifi() -> None:
    with open('wifi_config.txt', 'r') as f:
        lines = f.readlines()
        ssid = lines[0].strip()
        password = lines[1].strip()

    # stop the AP
    os.system('sudo systemctl stop dnsmasq')
    os.system('sudo systemctl stop hostapd')

    # restart NetworkManager
    os.system('sudo systemctl start NetworkManager')

    # try to connect to WiFi
    os.system(f'nmcli d wifi connect {ssid} password {password}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
