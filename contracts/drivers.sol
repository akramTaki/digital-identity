
pragma solidity >=0.4.2 <0.9.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract DriversRegistry is ERC721Full {
    constructor() public ERC721Full("DriverRegistryToken", "DRV") {}

    struct Drivers {
        string username; 
        string password; 
        string customertName; 
        string customerAddress; 
        string customerDOB; 
        uint256 customerIDNumber;
        }

    mapping(uint256 => Drivers) public driversCollection;

    event DriversID(uint256 tokenId, uint256 customerIDNumber);

    function registerDrivers(
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

        driversCollection[tokenId] = Drivers(
            username,
            password,
            customerName, 
            customerAddress, 
            customerDOB,
            initialcustomerIDNumber);

        return tokenId;
        }

    function updateLicenseIDNumber(
        uint256 tokenId,
        uint256 updatecustomerIDNumber
    ) public returns (uint256) {
        driversCollection[tokenId].customerIDNumber = updatecustomerIDNumber;

        emit DriversID(tokenId, updatecustomerIDNumber);

        return driversCollection[tokenId].customerIDNumber;
    }


}
