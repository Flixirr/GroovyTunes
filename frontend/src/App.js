import React  from 'react';
import './App.css';
import Login from './components/login';
import Register from './components/register';

//import "./styles/main-theme.css";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <div style={{ background: "#FFFFFF" }} id="main">
      <Router>
        
          <Switch>

            <Route path="/register">
              <Register />
            </Route>

            <Route path="/">
              <Login />
            </Route>
            
          </Switch>
      </Router>
    </div>
  );
}

export default App;
