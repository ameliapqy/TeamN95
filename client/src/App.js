import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import Success from './pages/Success';
import DonorForm from './pages/blog/DonorForm';
import SeekerForm from './pages/blog/SeekerForm';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state={
      apiResponse: "",
    };
  }

  // callAPI(){
  //   fetch("http://localhost:9000/")
  //   .then(res => res.text())
  //   .then(res => this.setState({apiResponse: res}));

  // }
  // componentDidMount(){
  //   this.callAPI();
  // }

  render(){
    const App = () => (
      <div>
        <Switch>
          <Route exact path='/' component={Home}/>
          <Route path='/success' component={Success}/>
          <Route path='/seekerform' component={SeekerForm}/>
          <Route path='/donorform' component={DonorForm}/>
        </Switch>
      </div>
    )
    return (
      <Switch>
        <App/>
      </Switch>
    );
  }
  
}

export default App;
