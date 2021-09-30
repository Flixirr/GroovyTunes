import React, { Component } from 'react';
import { Link } from "react-router-dom";


const API_SEARCH_ENDPOINT = "http://127.0.0.1:8000/api/v1/users/auth/login/";


class Dashboard extends Component {

    state = {
        searchQuery: ''
    };

    sendQuery = event => {
        event.preventDefault();

        fetch(`http://127.0.0.1:8000/search/${this.state.searchQuery}`)
            .then(response => response.json())
            .then(data => console.log(data));
    };

    inputChanged = event => {
        this.setState({searchQuery: event.target.value});
    };

    render() {
        return (
            <div className="App">
                <form onSubmit={this.sendQuery}>
                        <input type="text" placeholder="Enter query" name="searchQuery"
                                value={this.state.searchQuery}
                                onChange={this.inputChanged}></input>
                        <input type='submit' value='Search' />
                </form>
            </div>
        );
    }
}

export default Dashboard;
