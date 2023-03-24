import React, { useState } from "react";
import './logreg.css';

export const Register = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [nickname, setNickname] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        let check = await post_data(nickname,email,pass);
        
        if (check == true){
            props.onFormSwitch('login')
        }
    }

    return (
        <div className="auth-form-container">
            <h2>register</h2>
            <form className="register-form" onSubmit={handleSubmit}>
                <label htmlFor="nickname">Nickname</label>
                <input value={nickname} onChange={(e) => setNickname(e.target.value)} name="nickname" id="nickname" placeholder="awesomeNickname" />
                <label htmlFor="email">email</label>
                <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="youremail@email.com" id="email" name="email" />
                <label htmlFor="password">password</label>
                <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                <button type="submit" >REGISTER</button>
            </form>
            <button className="link-btn" onClick={() => props.onFormSwitch('login')}>Already have an account? Login here.</button>
        </div>
    )
}

async function post_data(nickname,email,pass) {
    // Simple POST request with a JSON body using fetch
    const requestOptions = {
        mode: 'cors',
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(
            { nickname: nickname,
              email: email,
              password: pass
            })
    }
    let data  = await fetch(`http://localhost:9000/register`,  requestOptions)
    //use string literals
    let dataJson = await data.json();
    console.log(dataJson)
    //logica de check
    // for (let i = 0; i < dataJson.length; i++){
    //     console.log(dataJson[i]);
    //     if (dataJson[i].email === email && dataJson[i].password === password)
    //         return true
    // }
    return true;
}
