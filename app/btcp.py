from btcpay import BTCPayClient
from btcpay.crypto import generate_privkey
from app.utils import save

btcpay_host = 'https://btcpay.vandrew.com'

def pairing(code):
    privkey = generate_privkey()
    btc_client = BTCPayClient(host=btcpay_host, pem=privkey)
    btc_token = btc_client.pair_client(code)
    btc_client = BTCPayClient(host=btcpay_host, pem=privkey, tokens=btc_token)
    save('btc_token', btc_token)
    save('btc_client', btc_client)
    save('privkey', privkey)