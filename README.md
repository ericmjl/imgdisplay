# imgdisplay

A simple Python app to display images in a standalone window.

## design goals:

1. Built by a hacker for other hackers. End-user is comfortable with running command line programs.
1. Cross-platform (Mac (tested), Linux (not yet tested), Windows (not yet tested))
1. Easily installable with minimal dependencies.
1. Executable from any directory.
1. Does one thing and only one thing well.
1. Not intended to be used as a library.

## purpose

I created this command-line app to enable anybody to display images in a random order when run from a given directory. It does nothing but this. Feel free to hack it to do something else!

## intended use cases

- Raspberry Pi photo display.

## philosophy

We should be hacking our own solutions where possible. Reduce dependency on closed-source tools.

## features

The app effectively keeps monitoring the folder it was run from for new images. This means that if you dump in a new folder, it'll be automatically be added to the list of images that can be displayed. Likewise, if you remove it from the folder, it'll automatically be removed from the list of images that can be displayed. Empty folders also won't cause problems, it'll just display a note "No images in directory.", and continue refreshing every 5 seconds until you put in new images there.

# installation

Via `pip`:

```bash
$ pip install imgdisplay
```

It's currently not `conda`-installable, because [`pywebview`][pywebview] depends on [`pyobjc`][pyobjc], and both have no conda packages available on `conda-forge`. I'm sure other `conda` users would appreciate PRs to make them available!

[pywebview]: https://github.com/r0x0r/pywebview
[pyobjc]: http://pythonhosted.org/pyobjc/

# usage

To run:

```bash
$ cd /path/to/images/
$ imgdisplay
```

To view help & options:

```bash
$ imgdisplay --help
 ```

To close/exit: close the terminal window, or close the app window. Both will do just fine.

# roadmap & future improvements

- add ability to control time between refresh.
- add auto-resize to window width and
