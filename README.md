# digital-identity
**Digital-Identity**
------
*This project is intended to incorporate KYC through Blockchain to ease the process, prevent fraud, save time and overall be more effective and efficient.*

---
**What is KYC:**
--

KYC stands for "Know Your Customer". It is a process used by companies and organizations to verify the identity of their customers or clients.The KYC process involves collecting personal information from the customer, such as their name, address, and government-issued identification. This information is then verified by a third-party service provider, who checks it against various databases to ensure its accuracy. Once the KYC process is complete, the customer is granted access to the company's products or services. KYC is an important aspect of regulatory compliance, and failure to comply with KYC requirements can result in legal and financial penalties.

**What is Blockchain:**
--

Blockchain is a digital ledger technology that enables secure and transparent online transactions. It is a decentralized, distributed database that is maintained by a network of computers, rather than a central authority. Each block in the chain contains a record of several transactions, which are validated by network participants and added to the ledger. The information in each block is encrypted and connected to the previous block, creating a chronological chain of blocks that cannot be altered or deleted without consensus from the network.

**KYC in Blockchain:**
--

KYC in blockchain refers to the process of verifying the identity of a customer or user on a blockchain network. KYC is an important aspect of blockchain security and compliance, and it helps to build trust among users and investors in the network. This is done to prevent fraud, money laundering, and other criminal activities on the network.

Here are the steps to create a smart contract for KYC in blockchain:


![Digital ID Blockchain](https://github.com/akramTaki/digital-identity/blob/main/image/Digital_ID_Blockchain.png)



  1. Define the KYC process: Define the steps involved in the KYC .process, such as collecting customer information, verifying the information, and storing it on the blockchain.
  2. Write the smart contract code: Use a programming language such as Solidity to write the smart contract code. The code should include functions for collecting customer information, verifying the information, and storing it on the blockchain.
 3. Define the data structure: Define the data structure for storing customer information on the blockchain. This can include fields such as name, address, date of birth, and identification number.Implement the verification process.blockchain.
4. Implement a verification process to ensure that the customer information is accurate and valid. This can include verifying the customer's identification documents and conducting background checks.
blockchain.
5. Deploy the smart contract: Deploy the smart contract on the blockchain network. Once deployed, the smart contract will automatically execute the KYC process when triggered by certain conditions.
6. Test the smart contract: Test the smart contract to ensure that it is functioning as intended and that customer information is being securely stored on the blockchain.

In blockchain, we have used smart contract for NFT - ERC-721 to automate the KYC process and ensure that customer information is securely stored on the blockchain. Below are the contracts cretaed which is then compiled and saved as backend source to facilitate the frontend app.
We have created the below contracts:
 - **Customer General Info Contract:** This includes creating, validating and storing basic information of the customer that includes name, age, gender, address etc.
 - **Customer Identification Contract:** This includes creating, validating and storing customer's identfication documents such as driving licence.
 - **Customer Health Information Contract:** This includes creating, validating and storing customer's health identfication documents such as vaccine reports.
 - **Customer Financial Information Contract:** This includes creating, validating and storing customer's financial documents such as banking information on debit/credit card, online tools such as PayPal etc.



*It's important to note that creating a smart contract for KYC requires a good understanding of blockchain technology and programming languages such as Solidity. It's also important to follow best practices for smart contract development to ensure that the contract is secure and free from vulnerabilities.

Tech Stats:
Backend - Solidity, Python, Ganache and Metamask
Frontend - React, Bootstrap

Sources:
https://techblog.geekyants.com/decentralized-kyc-on-blockchain-a-case-study#heading-please-find-the-full-source-code-herehttpsgithubcomgeekyantssample-decentralised-kyc-ethereum
