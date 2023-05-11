import React, { useState } from "react";
import "./logreg.css";
import univalle from "./Univalle.svg.png";

const Recovery = (props) => {
  const [codeid, setCodeId] = useState("");
  const [numeroid, setNumeroId] = useState("");
  const [pass, setPass] = useState("");
  const [repass, setRePass] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!codeid || !numeroid || !pass || !repass) {
      setError("Todos los campos son obligatorios");
      return;
    }
    if (pass !== repass) {
      setError("Las contraseñas no coinciden");
      return;
    }
    try {
      const requestOptions = {
        //mode: "cors",
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: codeid,
          identification: numeroid,
          new_password: pass,
          repeat_password: repass,
        }),
      };
      console.log(requestOptions);
      let data = await fetch(
        `https://saraendpoint.azurewebsites.net/user/change_password/`,
        requestOptions
      );
      let dataJson = await data.json();
      console.log(dataJson);
      // mostrar mensaje de éxito al usuario
    } catch (error) {
      console.error(error);
      setError("No se pudo cambiar la contraseña");
    }
    console.log(error);
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
          <div className="row border rounded-5 p-3 bg-white shadow box-area">
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
                Recuerda Que
              </label>
              <small
                className="text-red text-wrap text-center"
                style={{
                  width: "17rem",
                  fontFamily: '"Courier New", Courier, monospace',
                }}
              >
                Aqui podras realizar adiciones y cancelaciones de asignaturas.
              </small>
            </div>
            {/*------------------ ------ Right Box --------------------------*/}
            <div className="col-md-6 right-box">
              <div className="row align-items-center">
                <div className="header-text mb-4">
                  <h2>¿Ayuda con la contraseña?</h2>
                  <p>
                    Escribe el codigo asociado a tu cuenta de la Universidad del
                    Valle.
                  </p>
                </div>
                <div className="input-group mb-3">
                  <input
                    //pattern="[0-9]*"
                    value={codeid}
                    onChange={(e) => setCodeId(e.target.value)}
                    id="code"
                    name="code"
                    type="code"
                    className="form-control form-control-lg bg-light fs-6"
                    placeholder="Codigo de identificacion"
                  />
                </div>
                <div className="input-group mb-3">
                  <input
                    //pattern="[0-9]*"
                    value={numeroid}
                    onChange={(e) => setNumeroId(e.target.value)}
                    id="number"
                    name="number"
                    type="code"
                    className="form-control form-control-lg bg-light fs-6"
                    placeholder="Numero de identificacion"
                  />
                </div>
                <div className="input-group mb-1">
                  <input
                    value={pass}
                    onChange={(e) => setPass(e.target.value)}
                    id="password"
                    name="password"
                    type="password"
                    className="form-control form-control-lg bg-light fs-6"
                    placeholder="Nueva Contraseña"
                  />
                </div>

                <div className="input-group mb-1">
                  <input
                    value={repass}
                    onChange={(e) => setRePass(e.target.value)}
                    id="repassword"
                    name="repassword"
                    type="password"
                    className="form-control form-control-lg bg-light fs-6"
                    placeholder="Repetir Contraseña"
                  />
                </div>

                <div className="input-group mt-3">
                  <button
                    className="btn btn-lg btn-danger w-100 fs-6"
                    type="submit"
                  >
                    Cambiar
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

export default Recovery;
