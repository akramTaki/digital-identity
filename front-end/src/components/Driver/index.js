import { Button, Timeline } from "antd";
// import Wrapper from "./style";
import Wrapper from "../Dashboard/style";
import SideBar from "../SideBar";

const Driver = () => {
  return (
    <Wrapper>
      <SideBar />
      <div className="glass content">
        <div>
          <div
            style={{
              height: 500,
            }}
          >
            general infos go here
          </div>
          <h2>History</h2>
          <Timeline
            items={[
              {
                children: "parking ticket - Mississauga",
              },
              {
                children: "parking ticket - Markham",
              },
              {
                children: "Added a few points",
              },
              {
                children: "Initial licence submitted",
              },
            ]}
          />
        </div>
      </div>
    </Wrapper>
  );
};

export default Driver;
