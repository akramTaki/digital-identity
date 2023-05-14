import styled from "styled-components";

const Wrapper = styled.div`
  float: left;
  width: 200px;
  height: calc(100vh - 42px);
  padding: 20px;
  border-radius: 0;
  img {
    border-radius: 50%;
    width: 150px;
    margin: auto;
    display: block;
    margin-bottom: 40px;
  }
  h1 { 
    text-align: center;
    margin-bottom: 60px;
  }

  a {
    display: block;
    text-decoration: none;
    color: #000;
    padding: 20px;
    margin-top: 20px;
    background: rgba(255,255,255,0.7);
    border: 1px solid #fff;
    box-shadow: 0 0 10px #aaa;
    border-radius: 5px;
  }
`;

export default Wrapper;
