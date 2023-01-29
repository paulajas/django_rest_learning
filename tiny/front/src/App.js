import React, { Component } from "react"
import {render} from "react-dom"
import * as ReactDOM from 'react-dom';
import {Routes, Route} from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import Home from "./components/Home";
import Receipe from "./components/Receipies"
import ReceipeId from "./components/Receipe"
import AddReceipe from "./components/AddReceipe";
import CookReceipe from "./components/CookReceipe";
import Cookbook from "./components/Cookbook";
import UpdateReceipe from "./components/UpdateReceipe";

function App(props) {

    return (
      <div className="container">
        <Routes>
          <Route path='/' element="{<Home/>}"/>
          <Route path='/receipe/' element={<Receipe/>} />
          <Route path='/receipe/create' element={<AddReceipe/>} />
          <Route path='/receipe/update/:id' element={<UpdateReceipe/>} />
          <Route path='/cookbook/' element={<Cookbook/>} />
          <Route path='/cookbookreceipe/' element={<CookReceipe/>} />
        </Routes>
      </div>
    // <Router>
    //          <Routes>
    //              <Route path='/' element={<Home/>} />
    //              <Route path='/receipe/' element={<Receipe/>} />
    //              <Route path='/receipe/create' element={<AddReceipe/>} />
    //              <Route path="/receipe/:id" render={()=> <ReceipeId passDownSomething={this.id} />} />
    //          </Routes>      
         
    //      </Router>

  );
    // return (
    //     <Router>
    //         <Routes>
    //             <Route path='/api/receipes' element={<Home/>} />
    //         </Routes>      
         
    //     </Router>
    // );
  }
  
  export default App;

// const appDiv = document.getElementById("app");
// ReactDOM.render(
// <App />, appDiv);

const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);
root.render(<App name="Test" callback={() => console.log("Blog rendered")} />);
