import { useEffect, useState } from "react";

import axios from "axios";

function SportsBetting() {
  const [data, setData] = useState("");

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const data = await axios.get("/api/odds/read");
      setData((preData) => data);
    } catch (error) {
      console.log(error);
    }
  };

  console.log("hello");
  console.log(data);
  return (
    <>
      <h1>Welcome to the SportsBetting API</h1>
    </>
  );
}

export default SportsBetting;
