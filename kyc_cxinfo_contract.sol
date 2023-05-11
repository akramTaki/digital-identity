// SPDX-License-Identifier: GPL-3.0
pragma experimental ABIEncoderV2;
pragma solidity >=0.4.25 <0.9.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
contract KYC is ERC721 {
    struct Customer {
        string name;
        string cxaddress;
        string idDocument;
        bool verified;
    }
    mapping(address => Customer) public users;
    constructor() ERC721("KYC", "KYC") {}
    function registerUser(string memory _name, string memory _address, string memory _idDocument) public {
        require(users[msg.sender].verified == false, "User already registered");
        users[msg.sender] = Customer(_name, _address, _idDocument, false);
        uint256 tokenId = uint256(keccak256(abi.encodePacked(msg.sender)));
        _mint(msg.sender, tokenId);
    }
    function verifyUser(address _userAddress) public {
        require(msg.sender == ownerOf(uint256(keccak256(abi.encodePacked(_userAddress)))), "Not authorized");
        users[_userAddress].verified = true;
    }
    function revokeUser(address _userAddress) public {
        require(msg.sender == ownerOf(uint256(keccak256(abi.encodePacked(_userAddress)))), "Not authorized");
        delete users[_userAddress];
        _burn(uint256(keccak256(abi.encodePacked(_userAddress))));
    }
}