from flask import Flask, render_template, send_from_directory, make_response
from random import choice

import webview
import click
import os
import threading
import sys

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'templates')
app = Flask(__name__, template_folder=tmpl_dir)


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


@app.route('/close')
def close():
    """
    Adds a rudimentary "close window" function to the UI.
    """
    response = make_response('Closing window...')
    webview.destroy_window()
    return response


@click.command()
@click.option('--port', default=5432, help='Port number')
@click.option('--host', default='localhost', help='Host name')
@click.option('--width', default=None, help='Max image width.')
@click.option('--height', default=None, help='Max image height.')
def start_server(port, host, height, width):
    # Architected this way because my console_scripts entry point is at
    # start_server.

    kwargs = {'host': host, 'port': port}
    t = threading.Thread(target=app.run, daemon=True, kwargs=kwargs)
    t.start()

    fullscreen = False
    if not height and not width:
        fullscreen=True

    webview.create_window("PiPhoto Display",
                          "http://127.0.0.1:{port}/{height}".format(
                              port=port, height=height),
                          height=int(height) + 10,
                          fullscreen=fullscreen,
                          )

    sys.exit()


if __name__ == '__main__':

    start_server()
