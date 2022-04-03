from algosdk import mnemonic

# TODO
PINATA_API_KEY = "	ee8a153acc33b2ee9766"
PINATA_API_SECRET = "9fea9798742c79c22415c1b3b460ba471a1e826ed283c54017a72b177c3f38dc"

# TODO
PURESTAKE_API_KEY = "your-purestake-key-here"

# TODO
account_mnemonic = "your-mnemonic-here" 
account_private_key = mnemonic.to_private_key(account_mnemonic)
account_address = mnemonic.to_public_key(account_mnemonic)

ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
ALGOD_HEADERS = {"X-API-Key": PURESTAKE_API_KEY}
