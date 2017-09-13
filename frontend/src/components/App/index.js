import React, { PropTypes, Component } from 'react';
import classnames from 'classnames';
import request from 'request';

import './style.css';
import Loan from "../Loan/Loan";

class App extends Component {
  state = {data: []};

  get_current_loans = () => {
    request.get(window.location.protocol + '/loans', (error, response, body) => {
      this.setState({data: JSON.parse(body)})
    })
  };

  render_loans = () => {
    if (this.state.data.length === 0) {
      return <div className="no-loans">...No loans loaded...</div>
    }

    return this.state.data.map(loan => {
      return (
        <Loan url={loan.url} value={loan.remaining_amount}/>
      )
    });
  };

  render() {
    const { className, ...props } = this.props;
    return (
      <div className={classnames('App', className)} {...props}>
        <div className="jumbotron">
          <div className="big-button" onClick={() => this.get_current_loans()}>Get current loans</div>
        </div>
        <div className="loans">
          {this.render_loans()}
        </div>
      </div>
    );
  }
}

export default App;
