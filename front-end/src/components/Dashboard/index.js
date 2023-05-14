import { Button, Modal } from "antd";
import Wrapper from "./style";
import { Link } from "react-router-dom/dist";
import SideBar from "../SideBar";
import { useState } from "react";


const Dashboard = () => {
  const [modalOpen, setModalOpen] = useState(false);

  const closeModal = () => {
    setModalOpen(false);
  };
  return (
    <Wrapper>
      <SideBar />
      <div className="glass content">
        <Link to="/dashboard/driver" className="glass box">Driver</Link>
        <Link className="glass box">Passport</Link>
        <Link className="glass box">Health</Link>
        <Link className="glass box">Finance</Link>
        <Link className="glass box" onClick={() => setModalOpen(true)}>
          +
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
