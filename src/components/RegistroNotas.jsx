import React from "react";
import Table from "react-bootstrap/Table";
import { useState, useEffect } from "react";
import { Modal, Button, Form } from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';

import "styles/table.css";

const estudiantes = [
  {
    codigo: "00001C",
    nombre: "Santiago",
    nota: 4.5,
  },
  {
    codigo: "00003C",
    nombre: "carlos",
    nota: 4.5,
  },
  {
    codigo: "00002C",
    nombre: "daniel",
    nota: 4.5,
  },
];

const RegistroNotas = () => {
  const [showModal, setShowModal] = useState(false);
  const [selectedEstudiante, setSelectedEstudiante] = useState(null);

  const handleUpdateNota = (estudiante) => {
    setSelectedEstudiante(estudiante);
    setShowModal(true);
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };

  const handleGuardarCambios = () => {
    // TODO: guardar cambios en la base de datos
    
    handleCloseModal();
  };

  return (
    <div>
      <Table striped bordered hover className="table">
        <thead className="table-header">
          <tr className="table-row">
            <th className="table-header codigo">Código</th>
            <th className="table-header nombre">Nombre</th>
            <th className="table-header nota">Nota</th>
            <th className="table-header Actualizar Nota">Actualizar Nota</th>
          </tr>
        </thead>
        <tbody>
          {estudiantes.map((estudiante) => (
            <tr className="table-row" key={estudiante.codigo}>
              <td className="table-data codigo">{estudiante.codigo}</td>
              <td className="table-data nombre">{estudiante.nombre}</td>
              <td className="table-data nota">{estudiante.nota}</td>
              <td className="table-data Actualizar Nota">
                <div>
                  <button
                    className="button"
                    onClick={() => handleUpdateNota(estudiante)}
                  >
                    Actualizar Nota
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
      {selectedEstudiante && (
        <Modal show={showModal} onHide={handleCloseModal}>
          <Modal.Header closeButton>
            <Modal.Title>
              Editar nota de {selectedEstudiante.nombre}
            </Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <Form>
              <Form.Group className="mb-3">
                <Form.Label>Nueva nota:</Form.Label>
                <Form.Control
                  type="number"
                  defaultValue={selectedEstudiante.nota}
                  onChange={(e) =>
                    setSelectedEstudiante({
                      ...selectedEstudiante,
                      nota: e.target.value,
                    })
                  }
                />
              </Form.Group>
            </Form>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleCloseModal}>
              Cancelar
            </Button>
            <Button variant="primary" onClick={handleGuardarCambios}>
              Guardar cambios
            </Button>
          </Modal.Footer>
        </Modal>
      )}
    </div>
  );
};

export default RegistroNotas;
