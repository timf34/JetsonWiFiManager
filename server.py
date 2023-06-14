from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        ssid = request.form.get('ssid')
        ssid = request.form.get('ssid')
        password = request.form.get('password')

        # Save the SSID and password to a file
        with open('wifi_credentials.txt', 'w') as f:
            f.write(f'{ssid}\n{password}')

        # Use the submitted SSID and password to connect to the new network
        # You would replace 'wlan0' with the actual interface you want to use to connect to the new network
        os.system(f'sudo nmcli dev wifi con "{ssid}" password "{password}" ifname wlan0')

        return 'Success! Attempting to connect...'

    # Serve the form
    return '''
        <form method="POST">
            SSID: <br>
            <input type="text" name="ssid"><br>
            Password: <br>
            <input type="password" name="password"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
