import React, { useState } from "react";
import './App.css'
import { Login } from './login-register/Login';
import { Navbar } from "./bars/Navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Profile from "./pages/profile";
import Statistics from "./pages/statistics";
import Home from "./pages/home";

function App() {
  const [currentForm, setCurrentForm] = useState('login')//useState('page') or useState('login')

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  return (
    
    <div className = {(currentForm === 'login') ? 'App-login' : 'App-page'}>
      {
        currentForm === 'login' ? <Login onFormSwitch={toggleForm} /> :
            <>
              <Navbar />
              <Routes>
                <Route path='/home' exact element={<Home />} />
                <Route path='/profile' exact element={<Profile />} />
                <Route path='/statistics' exact element={<Statistics />} />
              </Routes>
            </>
      }
    </div>
  );


}

export default App;
