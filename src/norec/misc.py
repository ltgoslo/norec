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
import locale
import codecs

from io import BytesIO

class TarFile(tarfile.TarFile):
    """Subclass of TarFile adding som abstraction."""

    def get_files(self, encoding=None):
        member = self.next()

        while member:
            with self.open_file(member, encoding=encoding) as fd:
                yield member.name, fd

            member = self.next()

    def open_file(self, member, mode="r", encoding=None):
        """Return file object for file in archive."""

        # Set default encoding if not provided
        if not "b" in mode and not encoding:
            encoding = locale.getpreferredencoding(False)

        return self.readfile(member, encoding)

    def readfile(self, member, encoding):
        """Provides a file object for writing to file in archive."""

        fd = self.extractfile(member)

        if encoding:
            # File object from tarfile returns bytes, so wrap decoder
            # to read strings.
            return codecs.getreader(encoding)(fd)
        else:
            return fd
