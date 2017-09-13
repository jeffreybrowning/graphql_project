// src/components/App/index.js
import React, { PropTypes, Component } from 'react';
import './style.css';

class Loan extends Component {
  render() {
    const { url, value } = this.props;
    return (
      <div className='loan'>
        <div className="content">
          <a className="url" href={url} target="_blank">{url}</a><span className="value">{value}</span>
        </div>
      </div>
    );
  }
}

export default Loan;
