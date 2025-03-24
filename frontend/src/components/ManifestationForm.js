import { useState } from "react";
import axios from "axios";
import "./FormStyles.css"; // Arquivo CSS para estilos

function ManifestationForm() {
    const [tipo, setTipo] = useState("");
    const [descricao, setDescricao] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post("http://127.0.0.1:5000/manifestacoes", { tipo, descricao });
        alert("Manifestação enviada!");
        setTipo("");
        setDescricao("");  // Limpar campos após envio
    };

    return (
        <div className="form-container">
            <h2 className="form-title">Envie sua Manifestação</h2>
            <form className="manifestation-form" onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Tipo da manifestação"
                    className="input-field"
                    value={tipo}
                    onChange={(e) => setTipo(e.target.value)}
                />
                <textarea
                    placeholder="Descrição detalhada"
                    className="input-field"
                    value={descricao}
                    onChange={(e) => setDescricao(e.target.value)}
                />
                <button type="submit" className="submit-button">Enviar</button>
            </form>
        </div>
    );
}

export default ManifestationForm;
