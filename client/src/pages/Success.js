import React from 'react';

import { Link } from 'react-router-dom';

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state={
        apiResponse: ""
    };
  }

  callAPI(){
    fetch("http://localhost:9000/success")
    .then(res => res.text())
    .then(res => this.setState({apiResponse: res}));

  }
  componentDidMount(){
    this.callAPI();
  }

  render(){
    return (
      <>
      <h1> this is success </h1>
      
       <Link exact path="./home"> back to home </Link> 
      <p> {this.state.apiResponse} </p>
      </>
    );
  }
  
}

export default Home;
