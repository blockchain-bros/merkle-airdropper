import json
import base58

json_file_path = 'source.json'
updated_json_file_path = 'data.json'


with open(json_file_path, 'r') as file:
    data = json.load(file)

converted_list = [
    {"account": account, "amount": int(amount)}
    for account, amount in data.items()
]

data=converted_list

def is_valid_solana_address(address):
    try:
        # Decode the address from base58
        decoded = base58.b58decode(address)
        # Check if the decoded address has a length of 32 bytes
        return len(decoded) == 32
    except ValueError:
        # If decoding fails, it's not a valid base58 string
        return False
    
sum = 0
valid_accounts = []

for item in data:
    try:
        print(item)
        if is_valid_solana_address(item['account']):
            sum += item['amount']
            item['amount'] = item['amount']

            try: 
                claimed = item['claimed']
            except KeyError:
                item['claimed'] = False

            if item['claimed'] == False:
                valid_accounts.append({"account":item['account'], "amount": item['amount']})
        else:
            print(f"Invalid Solana address: {item['account']}")
    except KeyError:
        # If there's a character that's not in the base58 alphabet
        print(f"Invalid Key: {item}")

# Save the updated data back to a new JSON file
with open(updated_json_file_path, 'w') as file:
    json.dump(valid_accounts, file, indent=4)

print(f"Total amount: {sum} tokens")
print(f"Saved to {updated_json_file_path}")
