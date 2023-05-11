
pragma solidity >=0.4.2 <0.9.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract healthRegistry is ERC721Full {
    constructor() public ERC721Full("HealthRegistryToken", "HLT") {}

    struct Health {
        string username; 
        string password; 
        string customertName; 
        string customerAddress; 
        string customerDOB; 
        uint256 customerIDNumber;
        }

    mapping(uint256 => Health) public healthCollection;

    event HealthID(uint256 tokenId, uint256 customerIDNumber);

    function registerHealth(
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

        healthCollection[tokenId] = Health(
            username,
            password,
            customerName, 
            customerAddress, 
            customerDOB,
            initialcustomerIDNumber);

        return tokenId;
        }

    function updateHealthIDNumber(
        uint256 tokenId,
        uint256 updatecustomerIDNumber
    ) public returns (uint256) {
        healthCollection[tokenId].customerIDNumber = updatecustomerIDNumber;

        emit HealthID(tokenId, updatecustomerIDNumber);

        return healthCollection[tokenId].customerIDNumber;
    }


}
