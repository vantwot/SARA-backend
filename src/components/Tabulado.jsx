import React from "react";
import Table from "react-bootstrap/Table";

import "styles/table.css";

const MATERIAS = [
    {
        "codigo": "750020C",
        "grupo": "01",
        "asignatura": "ANÁLISIS Y DISEÑO DE ALGORITMOS II",
        "nota": 4.5,
        "creditos": 3
    },
    {
        "codigo": "750021C",
        "grupo": "01",
        "asignatura": "DESARROLLO DE SOFTWARE II",
        "nota": 4.5,
        "creditos": 3
    },
    {
        "codigo": "750018C",
        "grupo": "01",
        "asignatura": "PROYECTO INTEGRADOR I",
        "nota": 4.5,
        "creditos": 4
    },
    {
        "codigo": "750022C",
        "grupo": "01",
        "asignatura": "INTELIGENCIA ARTIFICIAL",
        "nota": 4.5,
        "creditos": 4
    },
    {
        "codigo": "750023C",
        "grupo": "01",
        "asignatura": "INFRAESTRUCTURAS PARALELAS Y DISTRIBUIDAS",
        "nota": 4.5,
        "creditos": 3
    },
]

const Tabulado = () => {
    return (
        <div>
            <Table striped bordered hover className="table">
                <thead className="table-header">
                    <tr className="table-row">
                        <th className="table-header codigo">Código</th>
                        <th className="table-header grupo">Grupo</th>
                        <th className="table-header asignatura">Asignatura</th>
                        <th className="table-header nota">Nota</th>
                        <th className="table-header creditos">Creditos</th>
                    </tr>
                </thead>
                <tbody>
                    {MATERIAS.map((materia) => (
                        <tr className="table-row" key={materia.codigo}>
                            <td className="table-data codigo">{materia.codigo}</td>
                            <td className="table-data grupo">{materia.grupo}</td>
                            <td className="table-data asignatura">{materia.asignatura}</td>
                            <td className="table-data nota">{materia.nota}</td>
                            <td className="table-data creditos">{materia.creditos}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </div>
    )
}

export default Tabulado;