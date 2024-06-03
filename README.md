# Solana Token Mint Address Fetcher

This Python script fetches and prints the mint addresses of tokens owned by a specified Solana wallet using the Solana JSON RPC API.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. **Clone the repository or download the script**:

    ```sh
    git clone https://github.com/your-repo/solana-token-fetcher.git
    cd solana-token-fetcher
    ```

    Or simply download the script `token_mint_addresses.py`.

2. **Install the required Python library**:

    ```sh
    pip install requests
    ```

## Usage

1. **Open the script `token_mint_addresses.py`** in your preferred text editor.

2. **Set the Solana wallet address** in the script:

    ```python
    # Wallet address for which to get token mint addresses
    wallet_address = "39azUYFWPz3VHgKCf3VChUwbpURdCHRxjWVowf5jUJjg"
    ```

3. **Run the script**:

    ```sh
    python token_mint_addresses.py
    ```

4. **View the output**, which will list the mint addresses of tokens owned by the specified wallet:

    ```plaintext
    Mint addresses of tokens created by wallet 39azUYFWPz3VHgKCf3VChUwbpURdCHRxjWVowf5jUJjg:
    <mint_address_1>
    <mint_address_2>
    ...
    ```

## Saving Mint Addresses to a File

If you want to save the mint addresses to a file during runtime:

1. **Run the script with an additional argument to save the addresses**:

    ```sh
    python main.py > mint_addresses.txt
    ```

2. **Check the output file** `mint_addresses.txt` in the script's directory to find the saved mint addresses.

## Troubleshooting

- **Ensure you have an active internet connection** as the script makes HTTP requests to the Solana JSON RPC API.
- If you encounter any issues, double-check the wallet address and ensure it is correctly set in the script.
- Make sure the `requests` library is installed and up to date.

## No License

