'use client';
import axios from "axios"
import { useEffect, useState } from "react";

import { getConstantValue } from "typescript";
import "./resume.css"
import next from "next";

const url = "http://127.0.0.1:8000/core/applicant/"

export default function SomeResume({params}:any){
  const [res,setRes]=useState(null);
  function getCV(){
    axios.get(url+`${params.id}`).then(response=>setRes(response.data)).catch(error=>console.log(error))
  }
    useEffect(()=>{
      getCV();
    },[]);
    
    return (
        <main>
            <h1>Resume</h1>
            <p>Some Cv</p>
            <p>Some Cv</p>
            <p>Some Cv</p>
            <p>Some Cv</p>
            <p>{JSON.stringify(res)}</p>

        </main>
    )
}