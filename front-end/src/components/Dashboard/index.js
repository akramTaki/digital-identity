import { Button, Modal } from "antd";
import Wrapper from "./style";
import { Link } from "react-router-dom/dist";
import SideBar from "../SideBar";
import { useState } from "react";

import driver from "../../assets/images/driver.png";
import passport from "../../assets/images/passport.png";
import health from "../../assets/images/health.png";
import finance from "../../assets/images/finance.png";

const Dashboard = () => {
  const [modalOpen, setModalOpen] = useState(false);

  const closeModal = () => {
    setModalOpen(false);
  };
  return (
    <Wrapper>
      <SideBar />
      <div className="glass content">
        <Link to="/dashboard/driver" className="glass box">
          <img src={driver} />
          <div>Driver</div>
        </Link>
        <Link className="glass box">
          <img src={passport} />
          <div>Passport</div>
        </Link>
        <Link className="glass box">
          <img src={health} />
          <div>Health</div>
        </Link>
        <Link className="glass box">
          <img src={finance} />
          <div>Finance</div>
        </Link>
      </div>

      <Modal
        open={modalOpen}
        onCancel={closeModal}
        onOk={closeModal}
        title="Add a new identity"
      >
        the form for new identity goes here
      </Modal>
    </Wrapper>
  );
};

export default Dashboard;
