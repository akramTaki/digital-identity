
pragma solidity >=0.4.2 <0.9.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract PassportRegistry is ERC721Full {
    constructor() public ERC721Full("PassportRegistryToken", "PPT") {}

    struct Passport {
        string username; 
        string password; 
        string customertName; 
        string customerAddress; 
        string customerDOB; 
        uint256 customerIDNumber;
        }

    mapping(uint256 => Passport) public passportCollection;

    event PassportID(uint256 tokenId, uint256 customerIDNumber);

    function registerPassport(
        address owner,
        string memory username,
        string memory password,
        string memory customerName,
        string memory customerAddress,
        string memory customerDOB,
        uint256 initialcustomerIDNumber) 
        public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);

        passportCollection[tokenId] = Passport(
            username,
            password,
            customerName, 
            customerAddress, 
            customerDOB,
            initialcustomerIDNumber);

        return tokenId;
        }

    function updatePassportIDNumber(
        uint256 tokenId,
        uint256 updatecustomerIDNumber
    ) public returns (uint256) {
        passportCollection[tokenId].customerIDNumber = updatecustomerIDNumber;

        emit PassportID(tokenId, updatecustomerIDNumber);

        return passportCollection[tokenId].customerIDNumber;
    }


}
