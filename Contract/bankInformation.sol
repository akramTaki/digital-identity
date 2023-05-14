
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;
// import ERC721
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
// intialize a contract that stores bank ifo
contract BankInfo is ERC721 {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    // stores centralised bank info
    struct BankInfoStruct {
        uint256 cardNumber;
        string bankName;
        string accountType;
        uint256 balance;
        string accountName;
        string accountNumber;
    }
    //stores digital wallet info
    struct DigitalAccountStruct {
        string accountName;
        string accountNumber;
        uint256 balance;
    }

    mapping(address => BankInfoStruct[]) public bankInfo;
    mapping(address => DigitalAccountStruct[]) public digitalAccountInfo;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    function storeBankInfo(string memory bankName, string memory accountType, uint256 balance, string memory accountName, string memory accountNumber) public returns (uint256) {
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();

        bankInfo[msg.sender].push(BankInfoStruct(newItemId, bankName, accountType, balance, accountName, accountNumber));
        _mint(msg.sender, newItemId);

        return newItemId;
    }

    function storeDigitalAccount(string memory accountName, string memory accountNumber, uint256 balance) public returns (uint256) {
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();

        digitalAccountInfo[msg.sender].push(DigitalAccountStruct(accountName, accountNumber, balance));
        _mint(msg.sender, newItemId);

        return newItemId;
    }

    function getBankInfo(uint256 tokenId) public view returns (BankInfoStruct memory) {
        require(_exists(tokenId), "Token does not exist");
        return bankInfo[ownerOf(tokenId)][tokenId - 1];
    }

    function getDigitalAccount(uint256 tokenId) public view returns (DigitalAccountStruct memory) {
        require(_exists(tokenId), "Token does not exist");
        return digitalAccountInfo[ownerOf(tokenId)][tokenId - 1];
    }
}
