import React, { Component } from 'react';
import { Link } from "react-router-dom";
import logo from "../img/logo-white.png";
import Cookies from 'js-cookie';

const API_AUTH_ENDPOINT = "http://127.0.0.1:8000/api/users/rest/login";

class Login extends Component {

    state = {
        credentials: {
            email: '',
            password: ''
        },
        errors: false
    }
    
    componentDidMount() {
        document.body.style.backgroundColor = "#121212";
        document.body.style.overflow = "hidden";
    }

    sendData = event => {
        event.preventDefault();

        let formData = new FormData();

        formData.append('username', this.state.credentials.email);
        formData.append('password', this.state.credentials.password);

        fetch(API_AUTH_ENDPOINT, {
            method: 'POST',
            body: formData
        }).then(
            res => res.json()
        ).then(
            data => {
                if(data.token) {
                    if(Cookies.get('token') === undefined || Cookies.get('token') === '')
                        Cookies.set('token', data.token);
                    window.location.replace('http://127.0.0.1:3000/main');
                } else {
                    this.setState({
                        credentials:
                        {
                            email: '',
                            password: ''
                        }
                    });
                    //Cookies.set('token', '');
                    this.setState({errors: true});
                }
            }
        )
    }

    inputChanged = event => {
        const creds = this.state.credentials;

        creds[event.target.name] = event.target.value;

        this.setState({credentials: creds});
    }

    render() {
        return (
            <div className="centered-flex">
                <img style={{ width: '29vh', height: '25vh', margin: '0'}} src={logo} alt="Logo" />
                    <form onSubmit={this.sendData}>
                        <input className="input-field" type="email" placeholder="example@org.co" name="email"
                                value={this.state.credentials.email}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="input-field" type="password" placeholder="Password" name="password"
                                value={this.state.credentials.password}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="ui green inverted button btn-centered" type='submit' value='LOGIN' />
                    </form>
                {this.state.errors && <p style={{ color: "red" }}>Invalid credentials.</p>}
                <p className="text-normal">Don't have an account yet? <Link to="/register" className="text-link">Register!</Link></p>
                <p style={{ fontSize: '2vh' }} >Or go to <Link to="/main" className="text-link">main page</Link></p>
            </div>
        );
    }
}

export default Login;
