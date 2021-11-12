

from base64 import *
from typing import Union

"""
a wrapper for the base64 library.
every class implements some base function.
every method takes in a byte-like object so basically, don't 
pass a string. or int.
"""


class base64:

	def __init__(self, data: Union[bytes, str]):
		self.data = data
	def _encode(self) -> str:
		if isinstance(self.data, bytes):
			return b64encode(self.data).decode()
		else:
			return b64encode(self.data.encode()).decode()
	def _decode(self) -> str:
		if isinstance(self.data, bytes):	
			return b64decode(self.data).decode()
		else:
			return b64decode(self.data.encode()).decode()
	def __str__(self):
		return str(self.__class__.__name__)


class base32:
	def __init__(self, data: Union[bytes, str]):
		self.data = data
	def _encode(self, bytes=False):
		return b32encode(self.data)
	def _decode(self):
		return b32decode(self.data)
	def __str__(self):
		return str(self.__class__.__name__)


class base16:
	def __init__(self, data: Union[bytes, str]):
		self.data = data
	def _encode(self, bytes=False):
		return b16encode(self.data)
	def _decode(self):	
		return b16decode(self.data)
	def __str__(self):
		return str(self.__class__.__name__)


class a85:

	def __init__(self, data: Union[bytes, str]):
		self.data = data.decod
	def _encode(self, bytes=False):
		return a85encode(self.data)
	def _decode(self):	
		return a85decode(self.data)
	def __str__(self):
		return str(self.__class__.__name__)

class b85:
	def __init__(self, data: Union[bytes, str]):
		self.data = data
	def _encode(self, bytes=False):
		return b85encode(self.data)
	def _decode(self):	
		return b85decode(self.data)
	def __str__(self):
		return str(self.__class__.__name__)
# testing

if __name__ == '__main__':
	for i in [base16, b85, base32, base64]:
		ins = i(b'hello')
		print(f"{str(ins)} => ",ins._encode().decode("utf-8"))