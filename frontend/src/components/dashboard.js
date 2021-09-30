import React, { Component } from 'react';
import { Link, Route, Switch } from 'react-router-dom';
import { Button } from 'semantic-ui-react';
import { SearchList } from './searchList'

class Dashboard extends Component {

    state = {
        searchQuery: '',
        loggedUserCreds: {
            email: '',
            username: '',
            first_name: '',
            last_name: ''
        },
        searchResults: []
    };


    sendQuery = event => {
        event.preventDefault();

        fetch(`http://127.0.0.1:8000/search/${this.state.searchQuery.replaceAll(' ', '-')}`)
            .then(response => response.json())
            .then(data => {
                /* 
                First array:
                    -> Artist name
                    -> Artist genius link
                Second array:
                    -> Song title
                    -> Genius link
                    -> Release date
                    -> Featured artists
                    -> Producers
                */
                console.log(data)
                this.setState({ searchResults: data });
                console.log(this.state.searchResults);
            });
    };

    componentDidMount() {
        fetch('http://127.0.0.1:8000/api/v1/users/auth/user', {
            method: 'GET',
            headers: {
                Authorization: `Token ${localStorage.getItem('token')}`
            }
        }) 
            .then(res => res.json())
            .then(data => {
                console.log(data);
                this.setState(
                    {
                        loggedUserCreds: {
                            email: data.email,
                            username: data.username,
                            first_name: data.first_name,
                            last_name: data.last_name
                        }
                    }
                );
            });
    }

    logout = event => {
        event.preventDefault();

        fetch('http://127.0.0.1:8000/api/v1/users/auth/logout/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Token ${localStorage.getItem('token')}`
            }
        })
            .then(res => res.json())
            .then(data => {
                console.log(data);
                localStorage.clear();
                window.location.replace('http://127.0.0.1:3000/');
        });
    };

    inputChanged = event => {
        this.setState({searchQuery: event.target.value});
    };

    render() {

        return (
            <div>
                <div style={{ display: 'flex', flexDirection: 'column', background: '#121212', width: '10vw', height: '100vh', position: 'absolute', color: 'white'}}>
                    <Link to='/main'>
                        <Button>
                            Main page
                        </Button>
                    </Link>

                    <Link to='/users/me'>
                        <Button>
                            My profile
                        </Button>
                    </Link>

                    <Button onClick={this.logout.bind(this)}>
                        Logout
                    </Button>
                </div>
                    

                <Switch>
                    <Route path="/main">
                        <div style={{ display: 'flex', position: 'absolute', left: '10vw', width: '90vw', 
                                height: '10vh', alignItems:'center', justifyContent:'center', borderBottom: '1px solid black' }}>
                            <form onSubmit={this.sendQuery}>
                                    <input type="text" placeholder="Enter query" name="searchQuery"
                                            value={this.state.searchQuery}
                                            onChange={this.inputChanged}></input>
                                    <input type='submit' value='Search' />
                            </form>
                        </div>
                        
                        <div style={{ display: 'flex', flexDirection: 'column', position: 'absolute', 
                                        left: '10vw', top: '10vh', width: '90vw', height: '90vh', alignItems:'center', justifyContent:'center'}}>
                            <SearchList items={this.state.searchResults} />
                        </div>
                    </Route>
                    <Route path="/users/me">
                        <p>In progress!</p>
                    </Route>
                </Switch>
            </div>
        );
    }
}

export default Dashboard;
