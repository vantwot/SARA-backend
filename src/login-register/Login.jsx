import React, { useState } from "react";
import "./logreg.css";
import univalle from "./Univalle.svg.png";
import { useNavigate } from "react-router-dom";
const Login = (props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();
// si el usuario esta registrado status codigo 200 y enviarlo al dashboard
// si el usuario no esta registrado status codigo diferente de 200 y mostrar mensaje de error
const handleSubmit = async (e) => {
  e.preventDefault();
  if (!username || !password) {
    setError("Todos los campos son obligatorios");
    return;
  }
  try {
    const requestOptions = {
      mode: "cors",
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: username,
        password: password,
      }),
    };
    console.log(requestOptions);
    const response = await fetch('https://saraendpoint.azurewebsites.net/login/', requestOptions);
    if (!response.ok) {
      throw new Error('Error en la solicitud');
    }
    const data = await response.json();
    console.log(data);
    
    navigate("home/"); 
  } catch (error) {
    console.log(error);
    setError("Ha ocurrido un error al iniciar sesión");
  }
};

  return (
    <div className="background">
      <meta charSet="UTF-8" />
      <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
        crossOrigin="anonymous"
      />
      <link rel="stylesheet" href="style.css" />
      {/*--------------------- Main Container ------------------------*/}
      <form onSubmit={handleSubmit}>
      <div className="container d-flex justify-content-center align-items-center min-vh-100">
        {/*--------------------- Login Container ------------------------*/}
        <div className="row border rounded-5 p-3 bg-white shadow box-area" >
          {/*------------------------- Left Box ---------------------------*/}
          <div
            className="col-md-6 rounded-4 d-flex justify-content-center align-items-center flex-column left-box"
            style={{ background: "#ffffff" }}
          >
            <div className="featured-image mb-3">
              <img
                src={univalle}
                className="img-fluid"
                style={{ width: 250 }}
                alt=""
              />
            </div>
            <label
              className="text-red fs-2"
              style={{
                fontFamily: '"Courier New", Courier, monospace',
                fontWeight: 600,
              }}
            >
              Bienvenido
            </label>
            <small
              className="text-red text-wrap text-center"
              style={{
                width: "17rem",
                fontFamily: '"Courier New", Courier, monospace',
              }}
            >
              Recuerda si estas aqui eres de lo mejor por eso perteneces a la
              mejor
            </small>
          </div>
          {/*------------------ ------ Right Box --------------------------*/}
          <div className="col-md-6 right-box">
            <div className="row align-items-center">
              <div className="header-text mb-4">
                <h2>Sistema Avanzado de Registro Academico</h2>
                <p>Estamos felices que estes de vuelta</p>
              </div>
              <div className="input-group mb-3">
                <input
                  //pattern="[0-9]*"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  id="code"
                  name="code"
                  type="code"
                  className="form-control form-control-lg bg-light fs-6"
                  placeholder="Codigo de identificacion"
                />
              </div>
              <div className="input-group mb-1">
                <input
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  id="password"
                  name="password"
                  type="password"
                  className="form-control form-control-lg bg-light fs-6"
                  placeholder="Contraseña"
                />
              </div>
              <div className="input-group mb-5 d-flex justify-content-between">
                <div className="forgot">
                  <small>
                    <a href="/recover" className="link-primary">
                      Recuperar contraseña
                    </a>
                  </small>
                </div>
              </div>
              <div className="input-group mb-3">
                <button className="btn btn-lg btn-danger w-100 fs-6" type="submit">
                  Iniciar
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      </form>
    </div>
  );
};

export default Login;
