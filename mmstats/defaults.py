import ctypes
import os
import tempfile


BUFFER_IDX_TYPE = ctypes.c_byte
SIZE_TYPE = ctypes.c_ushort
WRITE_BUFFER_UNUSED = 255
DEFAULT_PATH = os.getenv('MMSTATS_PATH', tempfile.gettempdir())
DEFAULT_FILENAME = os.getenv('MMSTATS_FILES', 'mmstats-%PID%-%TID%')
DEFAULT_STRING_SIZE = 255
