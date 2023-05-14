import styled from "styled-components";

const Wrapper = styled.div`
  padding-top: 100px;
  .heroText {
    width: 35%;
    float: left;
    margin-left: 100px;
    margin-top: 150px;
    font-size: 50px;
    color: #fff;
  }
  img {
    width: 50%;
    float: right;
    margin-right: 100px;
  }

  button {
    clear: both;
  }

  .kyc {
    margin: auto;
    display: block;
    float: none;
  }

  .kycText {
    clear: both;
    float: none;
    text-align: center;
    font-size: 50px;
    color: #fff;
    margin: 100px;
  }
`;

export default Wrapper;
