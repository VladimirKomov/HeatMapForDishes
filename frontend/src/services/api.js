import axios from "axios";

const api = axios.create({
    // base url FastAPI
    baseURL: "http://127.0.0.1:8000",
});

export default api;