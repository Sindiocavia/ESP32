from flask import Flask, request

app = Flask(__name__)

data = []

@app.route('/sensor/data', methods=['POST'])
def post():
    kelembapan = request.form.get("kelembapan")
    print(f"Received kelembapan: {kelembapan}")
    if kelembapan is not None:
        subData = [kelembapan]
        data.append(subData)
        return 'berhasil disimpan ke server', 200
    else:
        return 'Failed to receive data', 400

@app.route('/sensor/data', methods=['GET'])
def get():
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
