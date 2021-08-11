import { useState } from "react";
// import axios from "axios";

import { apiCalls } from "./funcs";

function SportsBetting() {
  const [data, setData] = useState("");
  const [urlValue, setUrlValue] = useState("");
  const [value, setValue] = useState("");
  const [selectedValue, setSelectedValue] = useState("get");

  const submitForm = (e) => {
    e.preventDefault();
    apiCalls[selectedValue](urlValue, value, setData);
  };

  return (
    <div className="container rounded border p-4 my-5">
      <h1 className="display-5 mb-5">Sports Betting API</h1>
      <div className="row mb-5">
        <div className="col-2">
          <select
            name="apiMethods"
            className="form-select"
            value={selectedValue}
            onChange={(e) => setSelectedValue(e.target.value)}
          >
            <option value="get" defaultValue>
              GET
            </option>
            <option value="post">POST</option>
            <option value="put">PUT</option>
            <option value="delete">DELETE</option>
          </select>
        </div>
        <form className="row col-10" onSubmit={submitForm}>
          <div className="col-10">
            <div className="input-group">
              <span className="input-group-text">/api</span>
              <input
                type="text"
                className="form-control"
                value={urlValue}
                onChange={(e) => setUrlValue(e.target.value)}
              />
            </div>
          </div>
          <button className="col-2 btn btn-primary text-nowrap">Send</button>
        </form>
      </div>
      <div className="row mb-5">
        <h2 className="lead text-black-50">Data</h2>
        <textarea
          rows="10"
          className="form-control"
          value={value}
          onChange={(e) => setValue(e.target.value)}
        ></textarea>
      </div>
      <div className="row">
        <h2 className="lead text-black-50">Response Data</h2>
        <div className="border rounded p-3">
          {data && <p className="lead">{JSON.stringify(data, null, 2)}</p>}
        </div>
      </div>
    </div>
  );
}

export default SportsBetting;
