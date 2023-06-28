import { useState } from "react";
import Modal from "./modal/Modal";
import axios from "axios";

function App() {
  const [isFemale, setIsFemale] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [details, setDetails] = useState({ height: "", weight: "", age: "" });
  const [goals, setGoals] = useState([]);

  const handleGender = () => {
    setIsFemale(true);
  };

  const handleDetails = (e) => {
    setDetails({ ...details, [e.target.name]: e.target.value });
  };

  const handleCheckBox = (e) => {
    const { value, checked } = e.target;
    if (checked) {
      setGoals([...goals, value]);
    } else {
      const newGoals = goals.filter((goal) => goal !== value);
      setGoals(newGoals);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post("http://127.0.0.1:8000/nutritional-advice/", { ...details, goals })
      .then(({ data }) => {
        console.log(data);
      })
      .catch((err) => console.log(err));
  };
  return (
    <div className="cont">
      <Modal isModalOpen={isModalOpen} />
      <div className="wrapper">
        <div className="left">
          <div className="img">
            <img src="./nutrition.png" alt="..." />
          </div>
        </div>
        <div className="right">
          <h4 className="title">
            Unlock Your Optimal Health with Personalized Nutritional Advisory
          </h4>
          <p className="description">
            Welcome to our platform, where we provide tailored guidance for your
            unique health needs. Our personalized nutritional advisory services
            empower you to make informed choices and optimize your well-being.
            Discover a customized approach that aligns with your goals,
            preferences, and dietary requirements. Take the first step towards a
            healthier, more vibrant you.
          </p>
        </div>
      </div>
      <div className="main">
        <h5 className="text-center">Get Nutritional Advice Today</h5>
        <form className="form" onSubmit={handleSubmit}>
          <div className="form-row">
            <div className="column">
              <h6>Height (Mtrs)</h6>
              <input
                type="number"
                className="form-control"
                name="height"
                value={details.height}
                onChange={handleDetails}
              />
            </div>
            <div className="column">
              <h6>Weight (Kg)</h6>
              <input
                type="number"
                className="form-control"
                name="weight"
                value={details.weight}
                onChange={handleDetails}
              />
            </div>
            <div className="column">
              <h6>Age</h6>
              <input
                type="number"
                className="form-control"
                name="age"
                value={details.age}
                onChange={handleDetails}
              />
            </div>
          </div>
          <div className="form-row mt-3">
            <div className="column-1">
              <h6>Gender</h6>
              <div className="radio-cont">
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="radio"
                    name="flexRadioDefault"
                    id="flexRadioDefault1"
                    onClick={() => setIsFemale(!isFemale)}
                  />
                  <label className="form-check-label" for="flexRadioDefault1">
                    Male
                  </label>
                </div>
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="radio"
                    name="flexRadioDefault"
                    id="flexRadioDefault2"
                    checked={isFemale}
                    onClick={handleGender}
                  />
                  <label className="form-check-label" for="flexRadioDefault2">
                    Female
                  </label>
                </div>
              </div>
            </div>
            <div className="column-1">
              <h6>Nutritional Goal</h6>
              <div className="checkbox-cont">
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    id="flexCheckDefault3"
                    value="bodybuilder"
                    onChange={handleCheckBox}
                  />
                  <label className="form-check-label" for="flexCheckDefault3">
                    Body Builder
                  </label>
                </div>
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    value="diabetic"
                    id="flexCheckDefault4"
                    onChange={handleCheckBox}
                  />
                  <label className="form-check-label" for="flexCheckDefault4">
                    Diabetic
                  </label>
                </div>
                {isFemale && (
                  <div className="form-check">
                    <input
                      className="form-check-input"
                      type="checkbox"
                      value="expectant"
                      id="flexCheckDefault5"
                      onChange={handleCheckBox}
                    />
                    <label className="form-check-label" for="flexCheckDefault5">
                      Expectant Mother
                    </label>
                  </div>
                )}
              </div>
            </div>
          </div>
          <div className="mt-3 d-flex justify-content-center">
            <button type="submit" className="btn-main">
              Get Advice
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default App;
