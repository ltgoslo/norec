# Copyright 2017 Eivind Alexander Bergem <eivinabe@ifi.uio.no>
# This file is part of norec.

# norec is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# norec is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with norec.  If not, see <http://www.gnu.org/licenses/>.

import tarfile
import os.path
import locale
import codecs
import time

from io import BytesIO
from contextlib import contextmanager
from collections import OrderedDict

class TarFile(tarfile.TarFile):
    """Subclass of TarFile adding som abstraction."""

    def __init__(self, name=None, mode='r', *args, **kwargs):
        tarfile.TarFile.__init__(self, name, mode, *args, **kwargs)

        if mode == "r":
            # Cache file list
            self.files = OrderedDict((m.path, m) for m in self.getmembers()
                                     if m.isfile())

    def list_files(self):
        """Return list of filenames of all files in archive."""

        return self.files.keys()

    def open_file(self, filename, mode="r", encoding=None):
        """Return file object for file in archive."""

        # Set default encoding if not provided
        if not "b" in mode and not encoding:
            encoding = locale.getpreferredencoding(False)

        if "w" in mode:
            return self.writefile(filename, encoding)
        else:
            return self.readfile(filename, encoding)

    def readfile(self, filename, encoding):
        """Provides a file object for writing to file in archive."""

        fd = self.extractfile(self.files[filename])

        if encoding:
            # File object from tarfile returns bytes, so wrap decoder
            # to read strings.
            return codecs.getreader(encoding)(fd)
        else:
            return fd

    @contextmanager
    def writefile(self, filename, encoding):
        """Provides a file object for writing to file in archive."""

        # Uses a buffer of bytes because tarfile doesn't handle
        # encoding.
        buf = BytesIO()

        if encoding:
            # Wrap bytes buffer in encoder
            yield codecs.getwriter(encoding)(buf)
        else:
            yield buf

        # Create tarinfo-object and add size
        info = tarfile.TarInfo(filename)
        info.size = buf.tell()
        info.mtime = time.time()

        # Seek to start of buffer and write to archive
        buf.seek(0)
        self.addfile(tarinfo=info, fileobj=buf)
        buf.close()
