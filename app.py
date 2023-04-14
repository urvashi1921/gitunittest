import boto3
from flask import Flask, jsonify

app = Flask(__name__)

s3 = boto3.resource('s3')
bucket_name = 'zeeurvashi'
file_name = 'test_file.json'

@app.route('/read_file')
def read_file():
    try:
        obj = s3.Object(bucket_name, file_name)
        content = obj.get()['Body'].read().decode('utf-8')
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
