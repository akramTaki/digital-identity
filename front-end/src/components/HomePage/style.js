import styled from "styled-components";

const Wrapper = styled.div`
  padding-top: 100px;

  .heroText {
    width: 35%;
    float: left;
    margin-left: 100px;
    margin-top: 50px;
    font-size: 50px;
  }
  img {
    width: 35%;
    float: right;
    margin-right: 200px;
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
    margin: 100px;
  }

  hr {
    clear: both;
    width: 80%;
    opacity: 0.5;
  }

  .menu {
    
    position: absolute;
    right: 100px;
    top: 30px;

    span {
      margin-left: 50px;
    }
  }
`;

export default Wrapper;
