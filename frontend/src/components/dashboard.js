import React, { Component } from 'react';
import { Link, Route, Switch } from 'react-router-dom';
import { Button } from 'semantic-ui-react';
import { SearchList } from './searchList';
import { Profile } from './profile';

function LogoutButtonLogic(props) {
    const logout = event => {
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

    if(props.isLoggedIn) {
        return (
            <Button onClick={logout.bind(this)}>
                Logout
            </Button>
        );
    } else {
        return (
            <div style={{ display: 'flex', flexDirection: 'column'}}>
                <Link to='/'>
                    <Button>
                        Login
                    </Button>
                </Link>

                <Link to='/register'>
                    <Button>
                        Register
                    </Button>
                </Link>
            </div>
        );
    }
}

class Dashboard extends Component {

    state = {
        searchQuery: '',
        userLoggedIn: false,
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
                
                if(data.email)
                    this.setState(
                        {
                            userLoggedIn: true,
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

                    <LogoutButtonLogic isLoggedIn={this.state.userLoggedIn} />
                    
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
                        <div style={{ position: 'absolute', left: '10vw', width: '90vw', 
                                    height: '100vh', alignItems:'center', justifyContent: 'flex-start' }}>
                            <Profile profile={this.state.loggedUserCreds} isLoggedIn={this.state.userLoggedIn} />
                        </div>
                    </Route>
                </Switch>
            </div>
        );
    }
}

export default Dashboard;
