from instrument import ByBitInstrument
from kline import ByBitKline


bybit_instrument = ByBitInstrument()
bybit_kline = ByBitKline()

print(bybit_instrument.response)
bybit_instrument.write_instrument_to_file()
bybit_instrument.print_instrument_from_file()

print(bybit_kline.response)
bybit_kline.write_kline_to_file()
bybit_kline.print_kline_from_file()