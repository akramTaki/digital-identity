pragma solidity ^0.8.0;

contract BankInfo {
    struct BankInfoStruct {
        string bankName;
        string accountType;
        uint256 balance;
        string accountName;
        string accountNumber;
    }

    struct DigitalAccountStruct {
        string accountName;
        string accountNumber;
    }

    mapping(address => BankInfoStruct[]) public bankInfo;
    mapping(address => DigitalAccountStruct[]) public digitalAccountInfo;

    function storeBankInfo(string memory bankName, string memory accountType, uint256 balance, string memory accountName, string memory accountNumber) public {
        bankInfo[msg.sender].push(BankInfoStruct(bankName, accountType, balance, accountName, accountNumber));
    }

    function storeDigitalAccount(string memory accountName, string memory accountNumber) public {
        digitalAccountInfo[msg.sender].push(DigitalAccountStruct(accountName, accountNumber));
    }

    function getBankInfo() public view returns (BankInfoStruct[] memory) {
        return bankInfo[msg.sender];
    }

    function getDigitalAccount() public view returns (DigitalAccountStruct[] memory) {
        return digitalAccountInfo[msg.sender];
    }

    
}
