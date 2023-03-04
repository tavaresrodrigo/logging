# Demo Flask App for Logging

This Flask web application provides a hands-on experience to understand how container logs work by logging jokes in various formats. The logs are displayed in a terminal-like interface in the browser and also sent to the container STDOUT for further analysis. This application utilizes Flask's logging capability to log each joke in JSON format and displays them on the web interface. 

Additionally, the application can be extended to log the jokes in other formats such as CSV, Apache, Nginx, Syslog, and dmesg to further demonstrate how different log formats can be used in containers.

## Usage

To run the app locally:

1. Install Python 3.9 or later.
2. Clone this repository to your local machine.
3. Open a terminal and navigate to the repository directory.
4. Run `pip install -r requirements.txt` to install the app's dependencies.
5. Run `python app.py` to start the app.
6. Open a web browser and navigate to `http://localhost:5000`.

To run the app in a Podman container:

1. Clone this repository to your local machine.
2. Open a terminal and navigate to the repository directory.
3. Build the container image `docker build -t [containerImageName]`.
4. Run the container mapping the port 5000 within the container to your localhost:80 `docker run -d -p 80:5000 --name [containerName] [containerImageName]`.
5. Open a web browser and navigate to `http://127.0.0.1`.


## Supported Formats
The application currently supports the following log formats:

JSON
CSV
Apache
Nginx
Syslog
Dmesg (kernel message buffer)

## Logging

The app logs messages using the built-in Python `logging` library. The logger is configured to log messages at the `DEBUG` level by default. You can modify the logger level by changing the `app.logger.setLevel(logging.DEBUG)` line in the `app.py` file.

## Contributing

Contributions are welcome! If you find a bug or want to suggest a new feature, please open an issue or submit a pull request.

## License

This app is licensed under the MIT license. See `LICENSE` for more information.


