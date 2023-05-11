from web3 import Web3
import json

# Connect to the local Ganache blockchain
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the compiled contract ABI

    with open(r"C:\Users\ycola\bankInfo_frontend\contracts\compiled\bankInfo_abi.json") as f:
        abi = json.load(f)

# Get the contract address after deploying the contract
        contract_address = os.getev("SMART_CONTRACT_ADDRESS")

# Create a contract instance using the ABI and contract address
contract = w3.eth.contract(address="0x036c4F57c970E5eaB4A11fdA2621Af8A36fd6240", abi=abi)


# Define the function to store bank information
def store_bank_info():
    bank_name = input('Enter bank name: ')
    account_type = input('Enter account type: ')
    balance = input('Enter balance: ')
    account_name = input('Enter account name: ')
    account_number = input('Enter account number: ')
    
    # Call the storeBankInfo function in the contract
    tx_hash = contract.functions.storeBankInfo(
        bank_name, account_type, balance, account_name, account_number
    ).transact({'from': w3.eth.accounts[0]})
    
    # Wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print('Bank information stored successfully!')
    
# Define the function to store digital account information
def store_digital_account():
    account_name = input('Enter account name: ')
    account_number = input('Enter account number: ')
    
    # Call the storeDigitalAccount function in the contract
    tx_hash = contract.functions.storeDigitalAccount(
        account_name, account_number
    ).transact({'from': w3.eth.accounts[0]})
    
    # Wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    print('Digital account information stored successfully!')
    
# Define the function to get bank information
def get_bank_info():
    # Call the getBankInfo function in the contract
    bank_info = contract.functions.getBankInfo().call({'from': w3.eth.accounts[0]})
    
    # Print the bank information
    for info in bank_info:
        print('Bank Name:', info[0])
        print('Account Type:', info[1])
        print('Balance:', info[2])
        print('Account Name:', info[3])
        print('Account Number:', info[4])
        print('-----------------------')

# Define the function to get digital account information
def get_digital_account():
    # Call the getDigitalAccount function in the contract
    digital_account_info = contract.functions.getDigitalAccount().call({'from': w3.eth.accounts[0]})
    
    # Print the digital account information
    for info in digital_account_info:
        print('Account Name:', info[0])
        print('Account Number:', info[1])
        print('-----------------------')
        
if __name__ == '__main__':
    store_bank_info()
    get_bank_info()
    store_digital_account()
    get_digital_account()

