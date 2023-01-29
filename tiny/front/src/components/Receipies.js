import React, { Component } from "react";
import axios from "axios";
import {useEffect, useState} from 'react';
import Navbar from './Nav';
import { Outlet, Link } from "react-router-dom";

class Receipe extends React.Component{
  constructor(){
    super();
    this.state={
      data:[]
    };
  }

  fetchData(){
    fetch('/api/receipe/')
    .then(response=> response.json())
    .then((data)=>{
      this.setState({
        data:data.results
      });
      console.log(data.results);
    });
  }

  componentDidMount(){
    this.fetchData();
  }

  deleteReceipe(id){
      console.log(id);
      fetch('/api/receipe/'+id+'/',{
      method:'DELETE',
      body:JSON.stringify(this.state),
      })
      .then(response=>response)
      .then((data)=>{
        if(data){
          this.fetchData();
        }
    })
  }
  updateReceipe(id){
    console.log("Pakuj")
  }

  render(){

    const receipeData=this.state.data;
    const rows = receipeData.map((receipe)=>
    <tr key={receipe.id}>
      <td scope="row">{receipe.name}</td>
      <td>{receipe.alcohol}</td>
      <td>{receipe.text_receipe}</td>
      <td>{receipe.creation_date}</td>
      <td>
        <Link to={'update/' + receipe.id} className="btn btn-info">Update</Link>
        <button onClick={()=>this.deleteReceipe(receipe.id)} className="btn btn-danger">Delete</button>
        </td>
    </tr>
    )
    return(
  <div>
    <Navbar/>
  <table class="table">
    <thead>
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Alcohol</th>
        <th scope="col">Text</th>
        <th scope="col">Creation Date</th>
      </tr>
    </thead>
    <tbody>
      {rows}
    </tbody>
  </table>
  </div >
    )
  }

  }

  export default Receipe
  