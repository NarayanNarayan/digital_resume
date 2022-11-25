'use client';
import axios from "axios"
import { useEffect, useState } from "react";

import { getConstantValue } from "typescript";
import "./resume.css"
import next from "next";


import Intro from "../(resume)/intro";
import Experience from "../(resume)/experiance";
import Projects from "../(resume)/project";
import Achievements from "../(resume)/achievement";
import Skills from "../(resume)/skill";
import Education from "../(resume)/education";




const url = "http://127.0.0.1:8000/core/applicant/"

export default function SomeResume({params}:any){
  const [res,setRes]=useState({});
  function getCV(){
    axios.get(url+`${params.id}`).then(response=>setRes(response.data)).catch(error=>console.log(error))
  }
    useEffect(()=>{
      getCV();
    },[]);
    
    return (
        <main>
            <Intro {...res}></Intro>
            <Education
            {...{collegeName:'IIT Kharagpur',
            fromDate: "Aug22",
          toDate: "Aug22",
          degreeName:"Bachelors",
          major:"Computer Science And Engineering",
          cgpa:8.03
          }}
            >

            </Education>
            <Experience
        {...{
          topic: "Software Engineering 2 @ Citrix",
          fromDate: "Aug22",
          toDate: "Aug22",
          description: "No Work",
          line: ["Some work", "Some work", "Some work", "Some work"],
        }}
      ></Experience>
      <Projects
        {...{
          topic: "eBPF Benchmark",
          fromDate: "Aug22",
          toDate: "Aug22",
          description: "No Work",
          line: ["Some work", "Some work", "Some work", "Some work"],
        }}
      ></Projects>
      <Achievements
      {...{
        achievements:["Got AIR 1 in JEE Advanced 2018"]
      }}
      ></Achievements>
            <p>{JSON.stringify(res)}</p>

        </main>
    )
}