from flask import Flask, render_template, send_from_directory
from random import choice

import webview
import click
import os
import threading
import sys


app = Flask(__name__, instance_path=os.getcwd())


@app.route('/')
@app.route('/<refresh>')
def hello():
    files = os.listdir(os.getcwd())
    image = choice([f for f in files if f[-4:] == '.jpg'])
    return render_template('img.html', image=image)


@app.route('/image/<path:imgname>')
def random_image(imgname):
    return send_from_directory(os.getcwd(), imgname, as_attachment=True)


@click.command()
@click.option('--port', default=5000, help='Port number')
@click.option('--host', default='localhost', help='Host name')
@click.option('--refresh', default=5, help='Refresh time (seconds)')
def start_server(port, host, refresh):
    # Architected this way because my console_scripts entry point is at
    # start_server.

    kwargs = {'host': host, 'port': port}
    t = threading.Thread(target=app.run, daemon=True, kwargs=kwargs)
    t.start()

    webview.create_window("PiPhoto Display",
                          "http://127.0.0.1:{0}".format(port, refresh))

    sys.exit()


if __name__ == '__main__':

    start_server()
