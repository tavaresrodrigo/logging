import logging
import logging.handlers
import json
import syslog
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    #render a simple html page with all the links to the oder endpoints 
        return '''
    <html>
        <head>
            <title>Understanding containers logging</title>
        </head>
        <body>
            <h1>Go horse containers!</h1>
            <p>Please click on the links below to access the endpoints:</p>
            <ul>
                <li><a href="/success">/success</a></li>
                <li><a href="/failure">/failure</a></li>
                <li><a href="/error">/error</a></li>
                <li><a href="/syslog">/error</a></li>
            </ul>
        </body>
    </html>
    '''

# log a structured json message to stdout for each 200 request
@app.route('/success')
def success():
    data = {
        'message': 'success',
        'status_code': 200,
        'data': {
            'truth': 'Pele is the best football player of all time',
            'lie': 'I love Peanut butter'
        }
    }
    app.logger.info(json.dumps(data))
    return jsonify(data)


# log a structured json message to stdout for each 200 request
@app.route('/failure')
def failure():
    data = {
        'message': 'success',
        'status_code': 200,
        'data': {
            'truth': 'Brasilia is the most beautiful city in Distrito Federal.',
            'lie': 'I love to eat vegetables'
        }
    }
    app.logger.warning(json.dumps(data))
    return jsonify(data)

# log a non structured message to stdout for each 500 request
@app.route('/error')
def error():
    data = "You fool :). I'm a lazy developer who does not follow the structured logging pattern, I hate good practices. Go horse!!"
    app.logger.error(data)
    return data

@app.route('/syslog')
def syslog():
    logging.basicConfig(level=logging.INFO)
    logging.info("This is a SYSLOG System message and you have no power to structure it at the OS level.")
    return "Why did the container's STDOUT break up with STDERR? Because it couldn't handle the arguments!"

if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.run(debug=True, host='0.0.0.0')