import React, {useState} from "react";
import './logreg.css';

export const Login = (props) => {
    const [code, setcode] = useState('');
    const [pass, setPass] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        let check = await clientCredentials(code,pass);
        
        if (check){
            console.log("asiogvasdovfsdapvaosv")
            props.onFormSwitch('page');
        }
            
    }

    return (
        <div className="auth-form-container">
            <h2>login</h2>
            <form className="login-form" onSubmit={handleSubmit}>
                <label htmlFor="code">code</label>
                <input value={code} onChange={(e)=> setcode(e.target.value)} type="code" placeholder="yourcode" id="code" name="code" />
                <label htmlFor="password">password</label>
                <input value={pass} onChange={(e)=> setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                <button type="submit" >LOG IN</button>
            </form>
            <button className="link-btn">Don't have an account? Contact an administrator</button>
        </div>
    )
}

async function clientCredentials(code,password){
    let data  = await fetch(`https://saraendpoint.azurewebsites.net/user/`)
    //use string literals
    let dataJson = await data.json();
    console.log(dataJson)
    console.log("user name:",code,"pass: ", password)
    for (let i = 0; i < dataJson.length; i++){
        //console.log(`${i}`,dataJson[i].code,code,(dataJson[i].code).toString() === (code).toString())
        //console.log(`${i}`,dataJson[i].name,password,dataJson[i].name === password);
        if ((dataJson[i].code).toString() === code && (dataJson[i].name).toString() === password)
            return true
    }
    return false;
}