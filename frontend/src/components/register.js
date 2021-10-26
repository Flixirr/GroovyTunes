import React, { Component } from 'react'
import { Link } from 'react-router-dom';
import logo from "../img/logo-white.png";
import Cookies from 'js-cookie';

const API_AUTH_ENDPOINT = "http://127.0.0.1:8000/api/v1/users/auth/register/";

class Register extends Component {

    state = {
        credentials: {
            email: '',
            username: '',
            first_name: '',
            last_name: '',
            password: '',
            password2: ''
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

        for(const key in this.state.credentials) {
            formData.append(key, this.state.credentials[key]);
        }

        fetch(API_AUTH_ENDPOINT, {
            method: 'POST',
            body: formData
        }).then(
            res => res.json()
        ).then(
            data => {
                if(data.token) {
                    Cookies.set('token', '');
                    Cookies.set('token', data.token);
                    window.location.replace('http://127.0.0.1:3000/main');
                } else {
                    this.setState({ credentials: {
                        email: '',
                        password: '',
                        confirmPassword: ''
                    }});
                    Cookies.set('token', '');
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
                <img style={{ width: '29vh', height: '25vh' }} src={logo} alt="Logo" />
                    <form onSubmit={this.sendData}>
                        <input className="input-field" type="email" placeholder="example@org.co" name="email"
                                value={this.state.credentials.email}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="input-field" type="text" placeholder="Username" name="username"
                                value={this.state.credentials.username}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="input-field" type="text" placeholder="First name" name="first_name"
                                value={this.state.credentials.first_name}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="input-field" type="text" placeholder="Last name" name="last_name"
                                value={this.state.credentials.last_name}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="input-field" type="password" placeholder="Password" name="password"
                                value={this.state.credentials.password}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input className="input-field" type="password" placeholder="Confirm password" name="password2"
                                value={this.state.credentials.password2}
                                onChange={this.inputChanged}></input>
                        <br />
                        {this.state.errors && <p style={{ color: "red" }}>Passwords do not match.</p>}
                        <input className="input-submit" type='submit' value='REGISTER' />
                    </form>
                <p class="text-normal">Already have an account? <Link to="/" className="text-link">Go back to login.</Link></p>
            </div>
        );
    }
}

export default Register;
