import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import hashlib

from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))


################################################################################
# Creates the Block and PyChain data classes

@dataclass
class Block:
    data: Any
    creator_id: int
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    prev_hash: str = "0"
    nonce: int = 0

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        creator_id = str(self.creator_id).encode()
        sha.update(data)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()

################################################################################

@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4

    def proof_of_work(self, block):

        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):

            block.nonce += 1

            calculated_hash = block.hash_block()

        print("Wining Hash", calculated_hash)
        return block

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

    def is_valid(self):

        block_hash = self.chain[0].hash_block()

        for block in self.chain[1:]:

            if block_hash != block.prev_hash:
                print("Blockchain is invalid!")
                return False

            block_hash = block.hash_block()

        print("Blockchain is Valid")
        return True
    
################################################################################

# Adds the cache decorator for Streamlit

@st.cache_resource
def setup():
    print("Initializing Chain")
    return PyChain([Block(data="Genesis", creator_id=0)])

pychain = setup()

################################################################################
# Streamlit Code

st.title("Know Your Customer Registry")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
owner = st.selectbox("Select Account", options=accounts)
st.markdown("---")

st.markdown("## Provide Identity Information")

username = st.text_input("Enter Username")
password = st.text_input("Enter Password")
customerFirstName = st.text_input("Enter First Name")
customerLastName = st.text_input("Enter Last Name")
customerAddress = st.text_input("Enter complete Address")
customerDOB = st.text_input("Enter Date of Birth")
customerIDType = st.text_input("Enter ID Type (Drivers License, Passport, Health Card, Other)")
customerIDNumber = st.text_input("Enter ID Number")


input_data = ("-".join([owner, 
              username, 
              password, 
              customerFirstName, 
              customerLastName, 
              customerAddress, 
              customerDOB, 
              customerIDType, 
              customerIDNumber]))

################################################################################    
# Adding block for Winning Hash

if st.button("Add Block"):
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    new_block = Block(data=input_data, creator_id=42, prev_hash=prev_block_hash)

    pychain.add_block(new_block)

    st.write("Winning Hash", new_block.hash_block())

st.markdown("## PyChain Ledger")
pychain_df = pd.DataFrame(pychain.chain)

st.write(pychain_df)


################################################################################
# Sidebar includes difficulty and Block Review

difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 4)

pychain.difficulty = difficulty

st.sidebar.write("# Block Review")
selected_block = st.sidebar.selectbox(
    "Which block would you like to see?", pychain.chain
)

st.sidebar.write(selected_block)

################################################################################
# Add a button with the text “Validate Blockchain” to your Streamlit interface.

if st.button("Validate Blockchain"):

    # Call the `is_valid` method of the `PyChain` data class and `write` the
    # result to the Streamlit interface
    st.write(pychain.is_valid())

################################################################################
# To run the script type:  "streamlit run digital_id.py"



