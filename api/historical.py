from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import yfinance as yf

_cache = {}

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        ticker = params.get('ticker', [None])[0]
        period = params.get('period', ['5y'])[0]

        if not ticker:
            self.send_error(400, 'Missing ticker')
            return

        ticker = ticker.upper().strip()

        cache_key = f"{ticker}_{period}"
        if cache_key in _cache:
            data = _cache[cache_key]
        else:
            try:
                df = yf.download(ticker, period=period, auto_adjust=True, progress=False)
                if df.empty:
                    self.send_error(404, 'Ticker not found')
                    return

                # New yfinance version MultiIndex column
                if isinstance(df.columns, type(df.columns)) and hasattr(df.columns, 'levels'):
                    df.columns = df.columns.get_level_values(0)

                closes = df['Close'].dropna()

                data = {
                    'ticker': ticker,
                    'dates': closes.index.strftime('%Y-%m-%d').tolist(),
                    'closes': [round(float(x), 4) for x in closes.values.tolist()]
                }
                _cache[cache_key] = data
            except Exception as e:
                self.send_error(500, str(e))
                return

        body = json.dumps(data).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)
