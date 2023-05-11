pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract MyContract is ChainlinkClient {
  bytes32 public chainlinkJobId;

  constructor() {
    setPublicChainlinkToken();
    chainlinkJobId = bytes32("my-chainlink-job-id");
  }

  function requestBankBalance(string memory _bankAccount) public {
    Chainlink.Request memory request = buildChainlinkRequest(chainlinkJobId, address(this), this.fulfillBankBalance.selector);
    request.add("bankAccount", _bankAccount);
    sendChainlinkRequestTo(chainlinkOracleAddress(), request, chainlinkFee);
  }

  function fulfillBankBalance(bytes32 _requestId, uint256 _balance) public {
    // handle the bank balance response here
  }
}
