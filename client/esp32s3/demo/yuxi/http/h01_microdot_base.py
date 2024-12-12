# !/usr/bin/env python
# -*- coding: utf-8 -*-

from microdot import Microdot

app = Microdot()

@app.route('/')
def index(request):
    return 'Hello, World!'

@app.route('/data', methods=['POST'])
def receive_data(request):
    data = request.json
    return {'received': data}

@app.route('/status')
def status(request):
    return {'status': 'OK', 'device': 'ESP32-S3'}

if __name__ == '__main__':
    app.run(debug=True)