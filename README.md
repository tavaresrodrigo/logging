# Demo Flask App for Logging

This repository contains a simple Python app that demonstrates Containers logging using the built-in Python `logging` library. The app logs structured JSON messages to stdout for successful and failed requests, and logs a non-structured message for requests that generate a server error.

## Usage

To run the app locally:

1. Install Python 3.9 or later.
2. Clone this repository to your local machine.
3. Open a terminal and navigate to the repository directory.
4. Run `pip install -r requirements.txt` to install the app's dependencies.
5. Run `python app.py` to start the app.
6. Open a web browser and navigate to `http://localhost:5000`.

## Endpoints

The app has currently four endpoints:

### /

Displays links to all endpoints available. 

### /success

Simulates a successful request by returning a JSON response with a 200 status code. Logs a structured JSON message to stdout for each successful request.

### /failure

Simulates a failed request by returning a JSON response with a 400 status code. Logs a structured JSON message to stdout for each failed request.

### /syslog

Simulates system log messages with a severity level of INFO or higher to be sent to the containers stdout for each syslog request. 

## Logging

The app logs messages using the built-in Python `logging` library. The logger is configured to log messages at the `DEBUG` level by default. You can modify the logger level by changing the `app.logger.setLevel(logging.DEBUG)` line in the `app.py` file.

## Contributing

Contributions are welcome! If you find a bug or want to suggest a new feature, please open an issue or submit a pull request.

## License

This app is licensed under the MIT license. See `LICENSE` for more information.


