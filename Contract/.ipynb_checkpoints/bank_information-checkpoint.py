import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache_resource
def load_contract():
    with open(Path("C:/Users/ycola/Contract/compiled/bankInfo.json")) as f:
        bank_information_abi = json.load(f)
        
    contract_address =  "0xB4eD662b858637d0fc0AdF30c0d6475e946488A5"

   
        
    contract = w3.eth.contract(address=contract_address, abi=bank_information_abi)
    return contract


# Load the contract
contract = load_contract()






#Set up endpoint URL
#url = "http://localhost:7545"
#headers = {"Content-type": "application/json"}




# Define Streamlit app

#st.set_page_config(page_title="Bank Info", page_icon=":money_with_wings:")
st.title("Bank Info")

    # Get wallet address and store it in session state
#if "wallet_address" not in st.session_state:
    #st.session_state.wallet_address = st.text_input("Enter wallet address")

    # Store bank info
st.header("Store Bank Info")

#accounts = w3.eth.accounts
address ="0xB4eD662b858637d0fc0AdF30c0d6475e946488A5"


bank_name = st.text_input("Bank name")
account_type = st.text_input("Account type")
balance = st.number_input("Balance", min_value=0, value=0, step=1)
account_name = st.text_input("Account name")
account_number = st.text_input("Account number")

if st.button("Store Bank Info"):
    tx_hash = contract.functions.storeBankInfo(bank_name, account_type, balance, account_name, account_number).transact({'from': address, 'gas': 1000000})
    token_id = contract.functions.bankInfo(address).call()[-1]['tokenId']
    st.success(f"Bank info stored with token ID {token_id}")

st.markdown("---")   
    
