import { Button } from "antd";
import Wrapper from "./style";
import { Link } from "react-router-dom/dist";
import pic from "../../assets/images/me.jpg"
const SideBar = () => {
  return (
    <Wrapper className="glass">
      <img src={pic} className="glass" />
      <Link to="/dashboard">Dashboard</Link>
      <Link to="/">Driver</Link>
      <Link to="/">Health</Link>
      <Link to="/">Finance</Link>
      <Link to="/">Passport</Link>
    </Wrapper>
  );
};

export default SideBar;
