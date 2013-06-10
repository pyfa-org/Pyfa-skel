from distutils.core import setup
import matplotlib
import numpy
import py2exe

setup(windows=[
        {
        "script": "pyfa.py" ,
        "icon_resources": [(1, "pyfa.ico")]
        }
    ],
    options= {
        "py2exe":{
            "packages": ["sqlalchemy.dialects.sqlite", "eos", "gui", "service", "matplotlib"],
            "excludes": ["_backend_gdk", "_gtkagg", "_tkagg", "_agg2", "_cairo", "_cocoaagg","_fltkagg", "_gtk", "_gtkcairo",
                         'bsddb', 'curses', 'email', 'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
                         'Tkconstants', 'Tkinter'],
            "dll_excludes": ["libgdk-win32-2.0-0.dll", "libgobject-2.0-0.dll",
                             "libgdk_pixbuf-2.0-0.dll"],
            "skip_archive": True,
            "optimize": 2
        }
    }
    ,data_files=matplotlib.get_py2exe_datafiles()
      )
