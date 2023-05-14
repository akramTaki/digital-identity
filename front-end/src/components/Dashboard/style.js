import styled from "styled-components";

const Wrapper = styled.div`
  .content {
    padding: 20px;
    float: right;
    width: calc(100vw - 350px);
    height: calc(100vh - 100px);
    margin-right: 30px;
    margin-top: 30px;
  }

  .box {
    padding: 20px;
    width: 100px;
    height: 100px;
    float: left;
    margin-right: 20px;
    box-shadow: 0 0 20px #aaa;
    text-decoration: none;
    color: #000;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all .2s ease;
    &:hover {
      background: #fff;
      box-shadow: 0 10px 30px #aaa;
    }
  }
`;

export default Wrapper;
