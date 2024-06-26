"""
XMLEdit GUI-onafhankelijke code
"""

import os
import pathlib

# import sys
# import shutil
# import copy
import logging

# from axe.gui import Gui

ELSTART = "<>"
axe_iconame = str(pathlib.Path(__file__).parent / "axe.ico")
# always log in program directory
LOGFILE = pathlib.Path("/tmp/logs/axe_qt.log")
LOGPLEASE = "DEBUG" in os.environ and os.environ["DEBUG"] != "0"
if LOGPLEASE:
    if not LOGFILE.parent.exists():
        LOGFILE.parent.mkdir()
    if not LOGFILE.exists():
        LOGFILE.touch()
    logging.basicConfig(
        filename=str(LOGFILE),
        level=logging.DEBUG,
        format="%(asctime)s %(message)s",
    )


def log(message):
    """if enabled, write a line to the log"""
    if LOGPLEASE:
        logging.info(message)
