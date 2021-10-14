import React  from 'react';
import './App.css';
import Login from './components/login';
import Register from './components/register';
import Dashboard from './components/dashboard';




import "./styles/main-theme.css";
import "./styles/search-styles.css";

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
              
              <Route path="/users/me">
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
