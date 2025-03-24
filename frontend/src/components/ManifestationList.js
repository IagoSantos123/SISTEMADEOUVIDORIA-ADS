import { useEffect, useState } from "react";
import axios from "axios";
import "./ListStyles.css"; // Arquivo CSS para estilos

function ManifestationList() {
    const [manifestacoes, setManifestacoes] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:5000/manifestacoes")
            .then(response => setManifestacoes(response.data));
    }, []);

    return (
        <div className="list-container">
            <h2 className="list-title">Lista de Manifestação</h2>
            <ul className="manifestation-list">
                {manifestacoes.map((m, index) => (
                    <li key={index} className="manifestation-item">
                        <div className="manifestation-item-header">
                            <strong>{m[1]}</strong>
                        </div>
                        <p>{m[2]}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default ManifestationList;
