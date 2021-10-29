import React  from 'react';
import './App.css';
import Login from './components/login';
import Register from './components/register';
import Dashboard from './components/dashboard';

import "./styles/profile-styles.css";
import "./styles/main-theme.css";
import "./styles/search-styles.css";
import "./styles/animated-styles.css";
import "./styles/playlist-styles.css";
import 'semantic-ui-css/semantic.min.css';

import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";

function App() {
  return (
    <div className="background-main-theme">

      <div className="background-tilted-rect-red"></div>
      <div className="background-tilted-rect-green"></div>

      <div className="route-content">
        <Router>
          
            <Switch>

              <Route path="/playlist/:id">
                <Dashboard />
              </Route>
             <Route path="/main/spotify/redirect">
                <Dashboard />
              </Route>
              
              <Route path="/users/me">
                <Dashboard />
              </Route>

              <Route path="/users/data/change">
                <Dashboard />
              </Route>

              <Route path="/users/data/change/password">
                <Dashboard />
              </Route>

              <Route path="/main">
                <Dashboard />
              </Route>

              <Route path="/register">
                <Register />
              </Route>

              <Route path="/">
                <Login />
              </Route>
              
            </Switch>
        </Router>
      </div>
    </div>
  );
}

export default App;
