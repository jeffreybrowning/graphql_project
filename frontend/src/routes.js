// src/routes.js
import React from 'react';
import { Router, Route } from 'react-router';

import App from './components/App/index';

const Routes = (props) => (
  <Router {...props}>
    <Route path="/" component={App} />
  </Router>
);

export default Routes;
