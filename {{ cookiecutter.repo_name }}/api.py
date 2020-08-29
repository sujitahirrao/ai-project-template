import os
from datetime import datetime
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

from src import config
from src.models.predict import predict
from src.response_handler import APIResponseHandler

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'xlsx'}

app = Flask('{{ cookiecutter.project_name }}')
app.config['UPLOAD_FOLDER'] = config.DATA_FOLDER
router = '/{{ cookiecutter.repo_name }}/' + config.ENV


def allowed_file(file_name):
    return '.' in file_name and \
           file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(request_id, request_file_part):
    # check if POST request has the file part
    if 'data_file' not in request_file_part:
        msg = "No file part: 'data_file' in POST request."
        print(msg)
        raise Exception(msg)
    file = request_file_part['data_file']
    if file.filename == '':
        msg = 'File name is empty.'
        print(msg)
        raise Exception(msg)
    if file and allowed_file(file.filename):
        print('Uploaded file:\t', file.filename)
        image_file_name = '_'.join([str(datetime.now()).replace(':', ''),
                                    '{}'.format(request_id),
                                    secure_filename(file.filename)])
        image_file_path = os.path.join(
            app.config['UPLOAD_FOLDER'], image_file_name)
        file.save(image_file_path)
        print('Image file is saved at {}'.format(image_file_path))
        return image_file_path


@app.route(router + '/hello', methods=['GET'])
def hello():
    return 'Hello from {{ cookiecutter.project_name }}!'


@app.route(router + '/predict', methods=['GET', 'POST'])
def _predict():
    try:
        if request.method == 'POST':
            print()
            print('request.form:\t', request.form)
            print('request.files:\t', request.files)
            request_id = request.form.get('request_id', -1)
            print('request_id:\t', request_id)
            uploaded_file_path = save_file(request_id, request.files)
            if uploaded_file_path:
                predictions = predict(uploaded_file_path)
                print('predictions:\t', predictions)
                return APIResponseHandler.api_success_response({
                    'request_id': request_id, 'predictions': predictions})
            else:
                msg = 'Failed to save data file.'
                return APIResponseHandler.api_failure_response(msg)
        else:
            msg = "POST the request. Don't GET it."
            return APIResponseHandler.api_bad_request_response(msg)
    except Exception as e:
        msg = str(type(e).__name__) + ': ' + str(e)
        return APIResponseHandler.api_failure_response(msg)


if __name__ == '__main__':
    app.run(debug=False)
