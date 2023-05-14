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
              height: 410
            }}
          >
            <div style={{ float: "left", paddingTop: 20 }}>
              <h2>Samuel L. Jackson</h2>
              <br />
              <div>
                <b>Lincese#:</b> TU-PF-01 <br />
                <b>Date of birth:</b> 1948-12-21 <br />
                <b>Class:</b> G <br />
                <br />
                805 W Pulp Fiction St. <br />
                Inglewood, CA 90301 <br />
                <br />
                <b>Sex:</b> M<br />
                <b>Height:</b> 6'2" <br />
                <b>Weight:</b> 207 Lbs. <br />
                <b>Hair:</b> Black <br />
                <b>Eyes:</b> Brown
              </div>
            </div>
            <img
              src="https://i.ebayimg.com/images/g/FXQAAOSwgZxgpJbD/s-l1600.jpg"
              className="licenceImg"
            />
          </div>
          <hr />
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
