from flask import Flask, render_template, request
from web3 import Web3
import json

# Connect to the local Ganache blockchain
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

# Load the compiled contract ABI
with open('bankInfo_abi.json') as f:
    abi = json.load(f)

# Get the contract address after deploying the contract
contract_address = '0x....' # replace with your deployed contract address

# Create a contract instance using the ABI and contract address
contract = w3.eth.contract(address=contract_address, abi=abi)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    bank_name = request.form['bank_name']
    account_type = request.form['account_type']
    balance = int(request.form['balance'])
    account_name = request.form['account_name']
    account_number = request.form['account_number']
    digital_account_name = request.form['digital_account_name']
    digital_account_number = request.form['digital_account_number']
    
    # Store bank information
    tx_hash = contract.functions.storeBankInfo(
        bank_name, account_type, balance, account_name, account_number
    ).transact({'from': w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    
    # Store digital account information
    tx_hash = contract.functions.storeDigitalAccount(
        digital_account_name, digital_account_number
    ).transact({'from': w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
from web3 import Web3
import json

# Connect to the local Ganache blockchain
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

# Load the compiled contract ABI
with open('bankInfo_abi.json') as f:
    abi = json.load(f)

# Get the contract address after deploying the contract
contract_address = '0x....' # replace with your deployed contract address

# Create a contract instance using the ABI and contract address
contract = w3.eth.contract(address=contract_address, abi=abi)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    bank_name = request.form['bank_name']
    account_type = request.form['account_type']
    balance = int(request.form['balance'])
    account_name = request.form['account_name']
    account_number = request.form['account_number']
    digital_account_name = request.form['digital_account_name']
    digital_account_number = request.form['digital_account_number']
    
    # Store bank information
    tx_hash = contract.functions.storeBankInfo(
        bank_name, account_type, balance, account_name, account_number
    ).transact({'from': w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    
    # Store digital account information
    tx_hash = contract.functions.storeDigitalAccount(
        digital_account_name, digital_account_number
    ).transact({'from': w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
