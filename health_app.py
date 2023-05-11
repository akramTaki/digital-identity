import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache_resource

def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/health_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()


st.title("Health Card Registry")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

################################################################################
# Register New Health Card
################################################################################
st.markdown("## Register Health Card")

username = st.text_input("Enter Username")
password = st.text_input("Enter Password")
customerName = st.text_input("Enter First and Last Name")
customerAddress = st.text_input("Enter complete Address")
customerDOB = st.text_input("Enter Date of Birth")
initialcustomerIDNumber = st.text_input("Enter Health Card ID Number")

if st.button("Register Health Card"):
    tx_hash = contract.functions.registerHealth(
        address,
        username,
        password,
        customerName,
        customerAddress,
        customerDOB,
        int(initialcustomerIDNumber)
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")


################################################################################
# Update Health Card Number
################################################################################
st.markdown("## Update Health card Information")
tokens = contract.functions.totalSupply().call()
token_id = st.selectbox("Choose Iniital Health Card Token ID", list(range(tokens)))
updatecustomerIDNumber = st.text_input("Enter Updated Health Card ID Number")
if st.button("Update Health Card ID Number"):

    # Use the token_id to record the udpates to Drivers License
    tx_hash = contract.functions.updateHealthIDNumber(
        token_id,
        int(updatecustomerIDNumber)
    ).transact({"from": w3.eth.accounts[0]})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write(receipt)
st.markdown("---")

################################################################################
# Get Updated Drivers License History
################################################################################
st.markdown("## Get Health Card Registry History")
health_token_id = st.number_input("Health Card Token ID", value=0, step=1)
if st.button("Get Health Card History"):
    health_filter = contract.events.HealthID.createFilter(
        fromBlock=0,
        argument_filters={"tokenId": health_token_id}
    )
    
    nhealth = health_filter.get_all_entries()
    
    if nhealth:
        for health in nhealth:
            report_dictionary = dict(health)
            st.markdown("### Health Card Report Event Log")
            st.write(report_dictionary)
            st.markdown("### Health Card Report Details")
            st.write(report_dictionary["args"])
    else:
        st.write("There are no updates to Health Card ID")

################################################################################

# To run the script type:  "streamlit run health_app.py"