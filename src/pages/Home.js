import React from "react";
import { useLocation } from "react-router-dom";
import { Tabulado, Calendar } from "../components";

import "styles/home.css";

const Home = () => {

    const userInfo = useLocation().state;

    //console.log("Home");
    //console.log(userInfo);

    const tabulado = userInfo.tabulado;
    const courses = getCourses(tabulado.courses);

    const appointments = getDates(courses);
    console.log(appointments);

    return (

        <div className="home-container background">

            <div className="home-header">
                <span className="home-title">¡Bienvenido {userInfo.name}!</span>
                <span className="home-subtitle">
                    Código de estudiante: {userInfo.username}<br></br>
                    Programa: {userInfo.program}
                    </span>
            </div>


            {/* </div> */}


            <div className="home-right">
                <span className="home-description">
                    Tu horario
                </span>
                <Calendar appointments={appointments}/>
            </div>

            <div className="home-left">
                <div>
                    <span className="home-description">Semestre actual: {tabulado.semester}</span>
                    <div>
                        <Tabulado courses={courses}/>
                    </div>

                </div>
            </div>
        </div>
    );
};

const getDates = (courses) => {
    let appointments = [];
    let appointment = {};
    let course = {};
    let startHour = 0;
    let endHour = 0;
    let counter = 0;

    const today = new Date();
    const week = {
        "lunes": 1 + today.getDate() - today.getDay(),
        "martes": 2 + today.getDate() - today.getDay(),
        "miercoles": 3 + today.getDate() - today.getDay(),
        "jueves": 4 + today.getDate() - today.getDay(),
        "viernes": 5 + today.getDate() - today.getDay(),
        "sabado": 6 + today.getDate() - today.getDay(),
        "domingo": 7 + today.getDate() - today.getDay(),
    }

    for (let i = 0; i < courses.length; i++) {
        console.log(courses[i]);
        course = courses[i];
        for (let j = 0; j < course.horario.date.length; j++) {
            startHour = course.horario.time[j].split("-")[0];
            endHour = course.horario.time[j].split("-")[1];

            appointment = {
                id: counter,
                title: course.name,
                startDate: new Date(today.getFullYear(), today.getMonth(), week[course.horario.date[j]], startHour.split(":")[0], startHour.split(":")[1]), //new Date(2021, 4, 10, 10, 0),
                endDate: new Date(today.getFullYear(), today.getMonth(), week[course.horario.date[j]], endHour.split(":")[0], endHour.split(":")[1]), //new Date(2021, 4, 10, 12, 0),
                location: course.horario.place[j],
            };

            appointments.push(appointment);
            counter++;
        }
    }
    return appointments;
}

const getCourses = (courses) => {
    let currentCourse = {};
    var coursesList = [];
    for (let i = 0; i < courses.length; i+=2) {
        currentCourse = courses[i];
        currentCourse.grade = courses[i+1];
        coursesList.push(currentCourse);
    }
    return coursesList;
}

export default Home;