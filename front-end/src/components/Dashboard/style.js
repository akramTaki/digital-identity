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
    width: 200px;
    height: 200px;
    float: left;
    margin: 40px;
    box-shadow: 0 0 20px #aaa;
    text-decoration: none;
    color: #000;
    text-align: center;
    display: flex;
    
    align-content: center;
    flex-wrap: wrap;
    justify-content: space-around;
    transition: all .2s ease;
    flex-direction: column;

    &:hover {
      background: #fff;
      box-shadow: 0 10px 30px #aaa;
    }

    img {
      width: 150px;
      display: block;
    }
  }

  .licenceImg {
    float: right;
    width: 500px;
    margin: 50px;
  }

  hr {
    opacity: 0.3;
  }


`;

export default Wrapper;
