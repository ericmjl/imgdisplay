from flask import Flask, render_template, send_from_directory
from random import choice

import webview
import click
import os
import threading
import sys

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'templates')
app = Flask(__name__, template_folder=tmpl_dir)
# app = Flask(__name__)


@app.route('/')
def hello():
    files = [f for f in os.listdir(os.getcwd()) if f[-4:] == '.jpg']
    if files:
        image = choice(files)
        return render_template('img.html', image=image)
    else:
        return render_template('img.html', error='No images in directory')


@app.route('/image/<path:imgname>')
def random_image(imgname):
    return send_from_directory(os.getcwd(), imgname, as_attachment=True)


@click.command()
@click.option('--port', default=5000, help='Port number')
@click.option('--host', default='localhost', help='Host name')
def start_server(port, host):
    # Architected this way because my console_scripts entry point is at
    # start_server.

    kwargs = {'host': host, 'port': port}
    t = threading.Thread(target=app.run, daemon=True, kwargs=kwargs)
    t.start()

    webview.create_window("PiPhoto Display",
                          "http://127.0.0.1:{0}".format(port))

    sys.exit()


if __name__ == '__main__':

    start_server()
