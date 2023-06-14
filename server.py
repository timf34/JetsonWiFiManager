from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ssid = request.form['ssid']
        password = request.form['password']

        # save the SSID and password to a file
        with open('/path/to/file', 'w') as f:
            f.write(f"{ssid}\n{password}")

        return 'OK'

    return '''
        <form method="POST">
            SSID: <input type="text" name="ssid"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
