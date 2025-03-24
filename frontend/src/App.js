import { useState } from "react";
import { FaPlusCircle, FaList, FaVideo, FaCode } from "react-icons/fa";
import ManifestationForm from "./components/ManifestationForm";
import ManifestationList from "./components/ManifestationList";
import "./AppStyles.css";

// Importando as logos corretamente
import adsLogo from "./adslogo.png";
import facisaLogo from "./facisalogo.png";

function App() {
    const [view, setView] = useState(null);

    return (
        <div className="app-container">
            <header className="header">
                <img src={adsLogo} alt="Logo 1" className="logo" />
                <img src={facisaLogo} alt="Logo 2" className="logo logo-smaller" />
            </header>

            <section className="intro">
                <h1>Trabalho de Programação em Linguagem Estruturada</h1>
                <p><strong>Professor:</strong> Daniel Abella</p>
                <p><strong>Produzido por:</strong> Iago Edson Santos Lucena, Gustavo e Daniel</p>
            </section>

            <h2 className="title">Ouvidoria</h2>

            {!view && (
                <div className="card-container">
                    <div className="card" onClick={() => setView("form")}>
                        <FaPlusCircle className="icon" />
                        <p>Enviar Manifestação</p>
                    </div>
                    <div className="card" onClick={() => setView("list")}>
                        <FaList className="icon" />
                        <p>Ver Manifestações</p>
                    </div>
                    <div className="card">
                        <FaVideo className="icon" />
                        <p>Vídeo Explicativo do Projeto</p>
                    </div>
                    <a
                        href="https://github.com/IagoSantos123/Sistema-de-ouvidoria-ADS"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="card"
                    >
                        <FaCode className="icon" />
                        <p>Repositório do Projeto</p>
                    </a>
                </div>
            )}

            {view === "form" && <ManifestationForm />}
            {view === "list" && <ManifestationList />}
        </div>
    );
}

export default App;
