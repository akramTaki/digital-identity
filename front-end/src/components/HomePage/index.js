import { Button } from "antd";
import HeroImage from "../../assets/images/hero.png";
import Wrapper from "./style";
import { Link } from "react-router-dom/dist";
import KYC from "../../assets/images/kyc.png";

const HomePage = () => {
  return (
    <Wrapper>
      <div className="menu">
        <span>Home</span>
        <span>Services</span>
        <span>How it works</span>
        <span>Contact</span>
      </div>
      <img src={HeroImage} />
      <h1 className="heroText">
        Know your Customer <br />
        <br /> The importance of KYC when it comes to international numbers
        <br />
        <br />
        <Button type="primary" size="large">
          <Link to="/dashboard">Get started</Link>
        </Button>
      </h1>
      
      <hr />
      <h1 className="kycText">How it works</h1>
      <img src={KYC} className="kyc" />
    </Wrapper>
  );
};

export default HomePage;
