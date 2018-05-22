import io, io_wrapper, unittest

class TestRawIOWrapper(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.reader = io_wrapper.RawIOWrapper(DuckTypedIO(support_read=True))
        self.writer = io_wrapper.RawIOWrapper(DuckTypedIO(support_write=True))
        self.file = io_wrapper.RawIOWrapper(open('/dev/zero', 'rb'))

    def tearDown(self):
        if not self.file.closed:
            self.file.close()

    def test_closed(self):
        self.assertFalse(self.reader.closed)

    def test_close(self):
        self.reader.close()
        self.assertTrue(self.reader.closed)

    def test_fileno(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.reader.fileno()
        self.assertTrue(self.file.fileno() > 0)

    def test_flush(self):
        self.reader.flush()
        self.writer.flush()
        self.file.flush()

    def test_isatty(self):
        self.assertFalse(self.reader.isatty())
        self.assertFalse(self.file.isatty())

    def test_readable(self):
        self.assertTrue(self.reader.readable())
        self.assertTrue(self.file.readable())

    def test_readline(self):
        self.assertEqual(b"xx\n", self.reader.readline())
        self.assertEqual(b"xx", self.reader.readline())
        self.assertEqual(b"", self.reader.readline())
        with self.assertRaises(io.UnsupportedOperation):
            self.writer.readline()

    def test_readlines(self):
        self.assertEqual([b"xx\n", b"xx"], self.reader.readlines())
        with self.assertRaises(io.UnsupportedOperation):
            self.writer.readlines()

    def test_seek(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.reader.seek(1, 0)
        self.file.seek(1, 0)

    def test_seekable(self):
        self.assertFalse(self.reader.seekable())
        self.assertTrue(self.file.seekable())

    def test_tell(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.reader.tell()
        self.assertEqual(0, self.file.tell())

    def test_truncate(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.reader.truncate()

    def test_writable(self):
        self.assertFalse(self.reader.writable())
        self.assertFalse(self.file.writable())

    def test_writelines(self):
        lines = [b"xx\n", b"xx"]
        with self.assertRaises(io.UnsupportedOperation):
            self.reader.writelines(lines)
        self.writer.writelines(lines)
            
    def test_read(self):
        self.assertEqual(b'xx', self.reader.read(2))
        self.assertEqual(b"\n", self.reader.read(1))
        self.assertEqual(b"\0", self.file.read(1))

    def test_readall(self):
        self.assertEqual(b"xx\nxx", self.reader.readall())
        with self.assertRaises(io.UnsupportedOperation):
            self.writer.readall()

    def test_readinto(self):
        b = bytearray(10)
        self.assertEqual(5, self.reader.readinto(b))
        self.assertEqual(b"xx\nxx", b[:5])

    def test_write(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.reader.write(b'xx')
        with self.assertRaises(io.UnsupportedOperation):
            self.file.write(b'xx')
        self.writer.write(b'xx')


class DuckTypedIO:
    """Mock reader/writer class for tests"""

    def __init__(self, support_read=False, support_write=False):
        self.support_read = support_read
        self.support_write = support_write
        self.content = b"xx\nxx"

    def read(self, size=1):
        if self.support_read:
            result = bytes()
            while size == -1 or size > 0:
                if len(self.content) == 0:
                    break
                result += self.content[:1]
                self.content = self.content[1:]
                if size > 0:
                    size -= 1
            return result
        else:
            raise io.UnsupportedOperation()

    def write(self, b):
        if self.support_write:
            return
        else:
            raise io.UnsupportedOperation()
