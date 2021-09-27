import React  from 'react';
import './App.css';
import Login from './components/login';
import Register from './components/register';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
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
  );
}

export default App;
