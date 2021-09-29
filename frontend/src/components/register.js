import React, { Component } from 'react'
import {Link} from 'react-router-dom';

const API_AUTH_ENDPOINT = "http://127.0.0.1:8000/api/v1/users/auth/register/";

class Register extends Component {

    state = {
        credentials: {
            email: '',
            password: '',
            confirmPassword: ''
        },
        errors: false
    }

    sendData = event => {
        event.preventDefault();

        const dataDjangoModel = {
            email: this.state.credentials.email,
            password: this.state.credentials.password,
            password1: this.state.credentials.confirmPassword
        }

        fetch(API_AUTH_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dataDjangoModel)
        }).then(
            res => res.json()
        ).then(
            data => {
                if(data.key) {
                    localStorage.clear();
                    localStorage.setItem('token', data.key);
                    window.location.replace('http://127.0.0.1:3000/main');
                } else {
                    this.setState({ credentials: {
                        email: '',
                        password: '',
                        confirmPassword: ''
                    }});
                    localStorage.clear();
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
            <div className="App">
                <h1>Register</h1>
                    <form onSubmit={this.sendData}>
                        <input type="email" placeholder="example@org.co" name="email"
                                value={this.state.credentials.email}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input type="password" placeholder="Password" name="password"
                                value={this.state.credentials.password}
                                onChange={this.inputChanged}></input>
                        <br />
                        <input type="password" placeholder="Confirm password" name="confirmPassword"
                                value={this.state.credentials.confirmPassword}
                                onChange={this.inputChanged}></input>
                        <br />
                        {this.state.errors && <p style={{ color: "red" }}>Passwords do not match.</p>}
                        <input type='submit' value='Register' />
                    </form>
                <p class="text-normal">Already have an account? <Link to="/">Go back to login.</Link></p>
            </div>
        );
    }
}

export default Register;
