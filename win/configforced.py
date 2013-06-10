import os
import sys

# Flag indicating if stderr should be redirected to file
stderrToFile = True

# Get root folder of pyfa executable file
pyfaPath = unicode(os.path.dirname(sys.executable),
                   sys.getfilesystemencoding())

stdoutToFile = True
stderrToFile = True
