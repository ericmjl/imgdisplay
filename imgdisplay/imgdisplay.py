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
@app.route('/<height>')
def hello(height=600):
    files = [f for f in os.listdir(os.getcwd()) if f[-4:] == '.jpg']
    if files:
        image = choice(files)
        return render_template('img.html', image=image, maxheight=height)
    else:
        return render_template('img.html', error='No images in directory')


@app.route('/image/<path:imgname>')
def random_image(imgname):
    return send_from_directory(os.getcwd(), imgname, as_attachment=True)


@click.command()
@click.option('--port', default=5000, help='Port number')
@click.option('--host', default='localhost', help='Host name')
@click.option('--height', default=700)
@click.option('--width', default=900)
def start_server(port, host, height, width):
    # Architected this way because my console_scripts entry point is at
    # start_server.

    kwargs = {'host': host, 'port': port}
    t = threading.Thread(target=app.run, daemon=True, kwargs=kwargs)
    t.start()

    webview.create_window("PiPhoto Display",
                          "http://127.0.0.1:{port}/{height}".format(
                              port=port, height=height),
                          height=height*1.1,
                          width=width,
                          )

    sys.exit()


if __name__ == '__main__':

    start_server()
