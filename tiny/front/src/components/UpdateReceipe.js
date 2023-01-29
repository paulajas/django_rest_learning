import React, { Component } from "react";

import Navbar from './Nav';
import { useParams } from 'react-router-dom';


const ReceipeId = () => {
  const routeParams = useParams();
};



class UpdateReceipe extends React.Component{

    constructor(){
        super();
        this.state={
            name:'',
            text_receipe:'',
            creation_date:'',
            alcohol:''
        }
        this.changeHandler=this.changeHandler.bind(this);
        this.submitForm=this.submitForm.bind(this);
    }

    changeHandler(event){
        this.setState({
            [event.target.name]:event.target.value
        });
    }

    submitForm(){
        let id = window.location.href.split('/')[5]
        fetch('/api/receipe/' + id+'/',{
            method:'PUT',
            body:JSON.stringify(this.state),
            headers:{
                'Content-type': 'application/json; charset=UTF-8'
            },
        })
        .then(response=>response.json())
        .then((data)=>console.log(data));
        this.setState({
            name:'',
            text_receipe:'',
            creation_date:'',
            alcohol:''
        });
    }

  fetchData(){
    let id = window.location.href.split('/')[5]
    fetch('/api/receipe/' + id)
    .then(response=> response.json())
    .then((data)=>{
      this.setState({
            name:data.name,
            text_receipe:data.text_receipe,
            creation_date:data.creation_date,
            alcohol:data.alcohol
      });
    });
  }

  componentDidMount(){
    this.fetchData();
  }


    render(){
        console.log(window.location.href.split('/')[5]);
    return(
        <div>
            <Navbar/>
        <table className="table table-bordered">
            <tr>
                <th>
                    Name of receipe
                </th>
                <td>
                    <input value={this.state.name} name="name" onChange={this.changeHandler} type="text" class="form-control" />
                </td>
            </tr>
            <tr>
                <th>Text of receipe</th>
                <td>
                    <input value={this.state.text_receipe} name="text_receipe" onChange={this.changeHandler} type="text" class="form-control" />
                </td>
            </tr>
            <tr>
                <th>
                    Date
                </th>
                <td>
                <input value={this.state.creation_date} name="creation_date" onChange={this.changeHandler} type="text" class="form-control" />
                </td>
                </tr>
            <tr>
                <th>
                    Alcohol
                </th>
                <td>
                    <input value={this.state.alcohol} name="alcohol" onChange={this.changeHandler} type="checkbox" class="form-control" />
                </td>
            </tr>
            <tr>
                <td colSpan="2">
                    <input type="submit" onClick={this.submitForm} className="btn btn-secondary" />
                </td>
            </tr>
        </table>
        </div>
    )}
}

export default UpdateReceipe;