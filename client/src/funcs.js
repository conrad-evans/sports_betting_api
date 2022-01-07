import axios from "axios";

export const apiCalls = {
  post: async function (url, payload, func) {
    payload = JSON.parse(payload);
    try {
      const data = await axios.post(`/api${url}`, payload);
      func(data.data);
    } catch (error) {
      return error;
    }
  },
  get: async function (url, payload = null, func) {
    try {
      const data = await axios.get(`/api${url}`);
      func(data.data);
    } catch (error) {
      return error;
    }
  },
  put: async function (url, payload, func) {
    payload = JSON.parse(payload);
    try {
      const data = await axios.put(`/api${url}`, payload);
      func(data.data);
    } catch (error) {
      return error;
    }
  },
  delete: async function (url, payload, func) {
    payload = JSON.parse(payload);
    try {
      const data = await axios.delete(`/api${url}`, payload);
      func(data.data);
    } catch (error) {
      return error;
    }
  },
};
