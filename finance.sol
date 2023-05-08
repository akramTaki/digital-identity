//SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract DigitalWallet {
    
    struct Account {
        string bankType;
        string accountType;
        uint balance;
        uint credit;
    }
    
    mapping(address => Account) public accounts;
    
    function addAccount(string memory _bankType, string memory _accountType, uint _balance, uint _credit) public {
        accounts[msg.sender] = Account(_bankType, _accountType, _balance, _credit);
    }
    
    function getAccount() public view returns (string memory, string memory, uint, uint) {
        Account memory account = accounts[msg.sender];
        return (account.bankType, account.accountType, account.balance, account.credit);
    }
    
}
/* This code defines a DigitalWallet contract that allows users to add an account and retrieve their account information. 
The Account struct stores the bank type, account type, balance, and credit information. 
The addAccount function allows the user to add their account information to the wallet by passing in the bank type, account type, balance, and credit as parameters.
 The getAccount function retrieves the account information for the user calling the function. */
