import React from 'react';

import { Link } from 'react-router-dom';
import Blog from './blog/Blog';

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state={
      apiResponse: ""
    };
  }

  callAPI(){
    fetch("http://localhost:9000/")
    .then(res => res.text())
    .then(res => this.setState({apiResponse: res}));

  }
  componentDidMount(){
    this.callAPI();
  }

  render(){

    return (
      <>
      <Blog />
      <Link exact to="./success"> to success </Link>
      <p> {this.state.apiResponse} </p>
      </>
    );
  }
  
}

export default Home;
