import {useEffect, useState} from 'react'
import './App.css'
import api from "./services/api.js";

function App() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        api.get("/")
            .then((response) => setMessage(response.data.message))
            .catch((error) => console.error("Error fetching data:", error));
    }, []);

    return (
        <div>
            <h1>React + Vite + FastAPI</h1>
            <p>{message}</p>
        </div>
    );
}

export default App
