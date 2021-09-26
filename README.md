# python_assignment1

## Title
python_coinGecko_assignment

### Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#lisense)

---

## Installation

PyPI

```python
pip install pycoingecko
``` 
or from source

```python
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

[Back To The Top](#python_assignment1)

## Usage

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```
[Back To The Top](#python_assignment1)
## Examples
```html
Enter count:3
1- id: bitcoin and other info
2- id: ethereum and other info
3- id: cardano and other info
```

```python
For instance: bitcoin
{'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 'current_price': 43163, 'market_cap': 825497257596, 'market_cap_rank': 1, 'fully_diluted_valuation': 920793657108, 'total_volume': 32383861477, 'high_24h': 44229, 'low_24h': 40890, 'price_change_24h': 638.9, 'price_change_percentage_24h': 1.50243, 'market_cap_change_24h': 17448364644, 'market_cap_change_percentage_24h': 2.15932, 'circulating_supply': 18826631.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 64805, 'ath_change_percentage': -33.12828, 'ath_date': '2021-04-14T11:54:46.763Z', 'atl': 67.81, 'atl_change_percentage': 63808.97317, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2021-09-26T11:35:54.041Z'}
```
[Back To The Top](#python_assignment1)

## License

MIT License

Copyright (c) 2021 Overexm

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#python_assignment1)
