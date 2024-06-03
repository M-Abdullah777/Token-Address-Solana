import requests

def get_token_mint_addresses(wallet_address):
    # Solana JSON RPC API endpoint
    endpoint = "https://api.mainnet-beta.solana.com"

    # Request payload to get token accounts by owner
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getTokenAccountsByOwner",
        "params": [
            wallet_address,
            {
                "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
            },
            {
                "encoding": "jsonParsed"
            }
        ]
    }

    # Make the HTTP request
    response = requests.post(endpoint, json=payload)
    response_data = response.json()

    # Check if the response contains any result
    if "result" in response_data:
        token_accounts = response_data["result"]["value"]

        # Extract the mint addresses
        mint_addresses = []
        for account in token_accounts:
            if "account" in account and "data" in account["account"]:
                mint_address = account["account"]["data"]["parsed"]["info"]["mint"]
                mint_addresses.append(mint_address)
        
        return mint_addresses
    else:
        raise Exception("Error fetching token accounts")

# Wallet address for which to get token mint addresses
wallet_address = "39azUYFWPz3VHgKCf3VChUwbpURdCHRxjWVowf5jUJjg"

# Get token mint addresses
try:
    mint_addresses = get_token_mint_addresses(wallet_address)
    print(f"Mint addresses of tokens created by wallet {wallet_address}:")
    for address in mint_addresses:
        print(address)
except Exception as e:
    print(e)
