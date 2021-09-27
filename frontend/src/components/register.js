import React, { Component } from 'react'
import {Link} from 'react-router-dom';

class Register extends Component {

    state = {
        credentials: {
            username: '',
            password: '',
            email: '',
            passwordMatches: false,
            name: '',
            surname: ''
        }
    }

    register = event => {
        console.log(this.state.credentials);
    }

    inputChanged = event => {
        const creds = this.state.credentials;

        if(event.target.name != "confrirmPassword")
            creds[event.target.name] = event.target.value;
        else
            creds['passwordMatches'] = creds['password'] == event.target.value;

        this.setState({credentials: creds});
    }

    render() {
        return (
            <div className="App">
                <h1>Login</h1>

                <input type="text" placeholder="Username" name="username" 
                        value={this.state.credentials.username}
                        onChange={this.inputChanged}></input> 
                <br />
                <input type="email" placeholder="example@org.co" name="email"
                        value={this.state.credentials.password}
                        onChange={this.inputChanged}></input>
                <br />
                <input type="password" placeholder="Password" name="password"
                        value={this.state.credentials.password}
                        onChange={this.inputChanged}></input>
                <br />
                <input type="password" placeholder="Confirm password" name="confrirmPassword"
                        value={this.state.credentials.password}
                        onChange={this.inputChanged}></input>
                <br />
                <button onClick={ this.login }>Register</button>
                <p class="text-normal">Already have an account? <Link to="/">Go back to login.</Link></p>
            </div>
        );
    }
}

export default Register;
