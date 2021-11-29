from matplotlib.pyplot import *
import yfinance as YF
import seaborn
import pandas as pd
from pandas_datareader import data as pdr
from colorama import Fore
from os import path, mkdir

"""
How to use:


	create the analyser instance:
		Analize = Analyzer(symbol, startData: str, endDate: str)

		data format: year-month-day
		to download:

		analize.downloadData()
from CurrencyAnalizer import Analyser



PYQT5 GUI for the currency analyzer.

Author: Moody0101
Github: gihub.com/Moody0101
Link: gihub.com/Moody0101/DataAnalysis/tree/main
branch: main

class GUI:
	pass

"""
analizerDOC = """
		
		a tool to plot Cryto currrncy closing stats.
		
		Usage: Crypto Currency_symbole start_date End date
		
		format: Currency_symbole year-month-day year-month-day 
		
		example: ETH 2021-11-10 2021-11-20

		to dump to a csv file:
			ETH 2021-11-10 2021-11-20 -S
		-S: stands for save and it dumps all the data to a file

		for now you can only plot one month stats.
		but you can download everythin.

"""

class SymbolNotSpecified(Exception):
	pass



class Analyser:
	def __init__(self, symbol: str, start: str, end: str) -> None:
		self.symbol = symbol
		self.start = start
		self.end = end
		self.data = pdr.get_data_yahoo(self.symbol, start=self.start, end=self.end)

	def downloadData(self):
		print(f"Downloading {self.symbol} stats from {self.start} to {self.end}..!")
		if not path.exists("./DownloadedStats"):
			mkdir('./DownloadedStats')

		self.data.to_csv(f"./DownloadedStats/{self.symbol}.csv")
		print(f"{Fore.GREEN}Downloaded to ./DownloadedStats!")
	def getClose(self, file=None) -> dict:
		if not file:
			if self.symbol:
				return self.data.Close.to_dict()

			else:
				raise SymbolNotSpecified("Specify the currency symbol !")
		else:
			self.data = pd.read_csv(file)
			return self.data.Close.to_dict()
	
	def getOpen(self, file=None) -> dict:
		if not file:
			if self.symbol:
				return self.data.Open.to_dict()
			else:
				raise SymbolNotSpecified("Specify the currency symbol !")
		else:
			self.data = pd.read_csv(file)
			return self.data.Close.to_dict().items()
	def Unzip(self, _dict) -> list:

		return [[str(i).split("-")[2].split(" ")[0] for i in _dict.keys()], [i for i in _dict.values()]]

	def PlotClose(self, file=None):
		if not file:
			if self.symbol:
				Items = self.Unzip(self.getClose())
				# print(Items)
				plot(Items[0], Items[1])
				if self.symbol:
					title(f"{self.symbol} {self.start}/{self.end}")
					xlabel("Day")
					ylabel("Price")
					show()

			else:
				raise SymbolNotSpecified("Specify the currency symbol !")
		else:
			Items = self.Unzip(self.getClose(file))
			plot(Items[0], Items[1])
			if self.symbol:
				title(f"Closing price {min(Items[0])}{max(Items[0])}")
				xlabel("Day")
				ylabel("Price")
				show()


if __name__ == "__main__":
	analize = Analyser("XRP-USD", "2021-11-01", "2021-11-24")
	analize.PlotClose()
# 'SOL'
# 'XRP'


