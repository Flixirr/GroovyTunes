import React, { Component } from 'react';
import { Link, Route, Switch } from 'react-router-dom';
import { SearchList } from './searchList';
import { Profile } from './profile';
import { ProfileChangeData } from './profileDataChange';
import { PasswordChange } from './passwordChange';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHome, faUser, faSignInAlt, faSignOutAlt, faMusic } from '@fortawesome/free-solid-svg-icons'
import logo from "../img/logo-white.png";
import Cookies from 'js-cookie';
import { Playlists } from './playlists';
import { getTokenFromUrl } from './spotifyAuth';


function LogoutButtonLogic(props) {
    const logout = event => {
        event.preventDefault();

        fetch('http://127.0.0.1:8000/api/users/rest/logout', {
            method: 'POST',
            headers: {
                Authorization: `Token ${Cookies.get('token')}`
            }
        })
            .then(res => res.json())
            .then(data => {
                console.log(data);
                Cookies.remove('token');
                window.location.replace('http://127.0.0.1:3000/');
        });
    };

    if(props.isLoggedIn) {
        return (
            <Link onClick={logout.bind(this)}>
                <div className="icon-animated-group">
                    <div className="icon-animated">
                        <FontAwesomeIcon className="text-link" icon={faSignOutAlt} />
                    </div>
                    <span className="icon-animated-text">
                        Logout
                    </span>
                </div>
            </Link>
        );
    } else {
        return (
            <Link to='/'>
                <div className="icon-animated-group">
                    <div className="icon-animated">
                        <FontAwesomeIcon className="text-link" icon={faSignInAlt} />
                    </div>
                    <span className="icon-animated-text">
                        Login
                    </span>
                </div>
            </Link>
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
            last_name: '',
            pk: ''
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
                this.setState({ searchResults: data.results });
                console.log(this.state.searchResults);
            });
    };

    componentDidMount() {
        document.body.style.backgroundColor = "#121212";
        document.body.style.overflowX = "hidden";
        document.body.style.overflowY = "auto";

        const spotifyTokenData = getTokenFromUrl();

        if(spotifyTokenData.access_token) {
            Cookies.set('spotifyAuthToken', spotifyTokenData.access_token);
        }

        fetch('http://127.0.0.1:8000/api/users/rest/properties', {
            method: 'GET',
            headers: {
                Authorization: `Token ${Cookies.get('token')}`
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
                                last_name: data.last_name,
                                pk: data.pk
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
                <div className="navbar-wrapper">
                    <div className="navbar">
                        <Link to='/main'>
                            <div className="icon-animated-group">
                                <div className="icon-animated">
                                    <FontAwesomeIcon className="text-link" icon={faHome} />
                                </div>
                                <span className="icon-animated-text">
                                    Home page
                                </span>
                            </div>
                        </Link>

                        <Link to='/users/me'>
                            <div className="icon-animated-group">
                                <div className="icon-animated">
                                    <FontAwesomeIcon className="text-link" icon={faUser} />
                                </div>
                                <span className="icon-animated-text">
                                    My profile
                                </span>
                            </div>
                        </Link>

                        <Link to='/users/me/playlists'>
                            <div className="icon-animated-group">
                                <div className="icon-animated">
                                    <FontAwesomeIcon className="text-link" icon={faMusic} />
                                </div>
                                <span className="icon-animated-text">
                                    Playlists
                                </span>
                            </div>
                        </Link>

                        <LogoutButtonLogic isLoggedIn={this.state.userLoggedIn} />
                    </div>
                </div>

                <Switch>
                
                    <Route path="/main/spotify/redirect">
                        <Playlists pk={this.state.loggedUserCreds.pk} />
                    </Route>

                    <Route path="/main">
                        <div className="search-wrapper">
                            <img style={{ width: '24vh', height: '20vh', marginTop: '10px'}} src={logo} alt="Logo" />
                            <form onSubmit={this.sendQuery}>
                                    <input type="text" placeholder="Enter query" 
                                            className="search-input"
                                            name="searchQuery"
                                            value={this.state.searchQuery}
                                            onChange={this.inputChanged}></input>
                            </form>
                        </div>
                        
                        <div className="search-results">
                            <SearchList items={this.state.searchResults} />
                            
                        </div>
                    </Route>

                    <Route path="/users/me/playlists">
                        <Playlists pk={this.state.loggedUserCreds.pk} />
                    </Route>

                    <Route path="/users/me">
                        <Profile profile={this.state.loggedUserCreds} isLoggedIn={this.state.userLoggedIn} />
                    </Route>

                    <Route path="/users/data/change/password">
                        <PasswordChange />
                    </Route>

                    <Route path="/users/data/change/">
                        <ProfileChangeData profile={this.state.loggedUserCreds} />
                    </Route>
                </Switch>
            </div>
        );
    }
}

export default Dashboard;
