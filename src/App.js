import React, { useState } from "react";
import './App.css'
import Login from './login-register/Login';
//import { Navbar } from "./bars/Navbar";
import { BrowserRouter as Router, Routes, Route, BrowserRouter } from "react-router-dom";
import Profile from "./pages/profile";
import Statistics from "./pages/statistics";
import { Home, Layout } from "./components";
import Recovery from "./login-register/recoverpass.jsx"

function App() {
  // const [currentForm, setCurrentForm] = useState('login')//useState('page') or useState('login')

  // const toggleForm = (formName) => {
  //   setCurrentForm(formName);
  // }

  return (

    // <div className = {(currentForm === 'login') ? 'App-login' : 'App-page'}>
    //   {
    //     // currentForm === 'login' ? <Login onFormSwitch={toggleForm} /> :
    <>
      {/* <Navbar /> */}
      <Routes>
        <Route path='/' exact element={<Login />} />
        <Route path='/home' exact element={<Layout> <Home /> </Layout>} />
        <Route path='/profile' exact element={<Profile />} />
        <Route path='/statistics' exact element={<Statistics />} />
        <Route path='/recover' exact element={<Recovery />} />
      </Routes>
    </>

    //   }
    //</div>




  );


}

export default App;
