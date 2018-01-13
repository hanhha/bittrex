# Bittrex API Python wrapper
A python wrapper for Bittrex's API.
## Supported APIs:
### v1.1 (officially documented on Bittrex website):
- Public APIs.
- Market APIs.
- Account APIs.

Please refer to their document [here](https://bittrex.com/home/api) for more detail.

### v2+ (unofficially):
There are some APIs detected by monitoring Bittrex website's requests and responses. They're not documented officially on their website. I decide to use some of Public APIs that's no need API key and secret.
- Get BTC price.
- Get candle sticks.

## Requirements:
- Python 3+.

## Usage guide:
### Install:
Download or clone the repository and run below command:
~~~
$python setup.py. install
~~~
Please be kindly noticed that python is python 3+.
### Usage examples:
~~~
import bittrex
~~~
#### Public APIs:
~~~
# v1.1
pAPI = bittrex.PublicAPI (bittrex.API_V1_1)
status0, result0   = pAPI.get_markets ()
status1, result1   = pAPI.get_currencies ()
status2, result2   = pAPI.get_ticker ('BTC-ETH')
status3a, result3a = pAPI.get_24h_sum ()
status3b, result3b = pAPI.get_24h_sum ('BTC-ETH')
status4, result4   = pAPI.get_order_book ('BTC-ETH') 
status5, result5   = pAPI.get_history ('BTC-ETH')

# v2.0
pAPIv2 = bittrex.PublicAPI (bittrex.API_V2_0)
status6, result6   = pAPIv2.get_btc_price ()

# second parameters must be in ['oneMin','fiveMin','thirtyMin','hour','day']
status7, result7   = pAPIv2.get_ticks ('BTC-ETH','oneMin')
status7, result7   = pAPIv2.get_ticks ('BTC-ETH','oneMin', True)
~~~
#### Market APIs:
~~~
# <your API key> and <your API secret> in below should be obtained from Bittrex website
mAPI = bittrex.MarketAPI (bittrex.API_V1_1, <your API key>, <your API secret>)
status0, result0   = mAPI.buy_limit ('BTC-ETH', quantity = 1, rate = 0.09)
status1, result1   = mAPI.sell_limit ('BTC_ETH', quantity = 1, rate = 0.1)
status2, result2   = mAPI.cancel (uuid = <uuid>) # <uuid> is uuid of opening order
status3a, result3a = mAPI.get_open_orders ()
status3b, result3b = mAPI.get_open_orders ('BTC-ETH')
~~~
#### Account APIs:
~~~
aAPI = bittrex.AccountAPI (bittrex.API_V1_1, <your API key>, <your API secret>)
status0a, result0a = aAPI.get_balance ()
status0b, result0b = aAPI.get_balance ('BTC')
status1, result1   = aAPI.get_deposit_addr ('BTC')
status2a, result2a = aAPI.withdraw ('BTC', qty = 10, addr = <my address>)
status2b, result2b = aAPI.withdraw ('BTC', qty = 10, addr = <my address>, pid = <payment id>)
status3, result3   = aAPI.get_order (uuid = <uuid>) # <uuid> is uuid of queried order
status4, result4   = aAPI.get_withdrawal_history ('BTC')
status5, result5   = aAPI.get_deposit_history ('BTC')
~~~

## License
The code is open-source under the terms of [MIT license](https://opensource.org/licenses/MIT).
