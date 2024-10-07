import json
import subprocess

def get_orphan_txs():
    # Run bitcoin-cli command to get orphan transactions
    command = ["bitcoin-cli", "getorphantxs", "0"]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return
        
        orphan_txs = json.loads(result.stdout)
        if not orphan_txs:
            print("No orphan transactions found.")
        else:
            print(f"Orphan transactions: {orphan_txs}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_orphan_txs()
