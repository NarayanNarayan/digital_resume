"use client";
import axios from "axios";
import { useEffect, useState } from "react";

import { getConstantValue } from "typescript";
import "./resume.css";
import next from "next";

import Intro from "../(resume)/intro";
import Experience from "../(resume)/experiance";
import Projects from "../(resume)/project";
import Achievements from "../(resume)/achievement";
import Skills from "../(resume)/skill";
import Education from "../(resume)/education";

const url = {
  applicant: "http://127.0.0.1:8000/core/applicant/",
  education: "http://127.0.0.1:8000/core/education/",
  experience: "http://127.0.0.1:8000/core/experience/",
  project: "http://127.0.0.1:8000/core/project/",
  certicication: "http://127.0.0.1:8000/core/certicication/",
  achievement: "http://127.0.0.1:8000/core/achievement/",
};

const theData = {
  name: "",
  email: "narayan1011g@gmail.com",
  github: "https://github.com/NarayanNarayan",
  linkedin: "https://www.linkedin.com/in/narayan-gupta-539470205/",
  education: [
    {
      collegeName: "",
      fromDate: "",
      toDate: "",
      degreeName: "",
      major: "",
      /* cgpa: 9, */
    },
  ],
  experience: [
    {
      position: "",
      fromDate: "",
      toDate: "",
      description: "",
      line:[""],
    },
  ],
  project: [
    {
      topic: "",
      fromDate: "",
      toDate: "",
      description: "",
      line:[""],
    },
  ],
  achievement:[{
    name:""
  }]
};
/* theData.education[0]={
  collegeName: "IIT Kharagpur",
  fromDate: "Aug22",
  toDate: "Aug22",
  degreeName: "Bachelors",
  major: "Computer Science And Engineering",
  cgpa: 8.03,
} */
theData.experience[0]={
  position: "Software Engineering 2 @ Citrix",
  fromDate: "Aug22",
  toDate: "Aug22",
  description: "Developing Citrix Virtual Workspace",
  line: ["Some Innovation", "Some Implimentation", "Some work", "Some work"],
}
theData.project[0]={
  topic: "eBPF Benchmark",
  fromDate: "Aug22",
  toDate: "Aug22",
  description: "eBPF is like Javascrit for Kernel",
  line: ["Some Innovation", "Some Implimentation", "Some work", "Some work"],
}





export default function SomeResume({ params }: any) {
  const [res, setRes] = useState({});
  function getCV() {
    axios
      .get(url.applicant + `${params.id}`)
      .then((response) => setRes(response.data))
      .then(()=>getEducation())
      .catch((error) => console.log(error));
  }
  function saveEducation(data:any){
    theData.education.push({
      collegeName: data.collegeName,
      fromDate: data.fromDate,
      toDate: data.toDate,
      degreeName: data.degreeName,
      major: data.major,
      cgpa: data.cgpa,
    })
  }
  function getEducation(){
    for (var i of [1,2]){
      axios
      .get(url.education + `${i}`)
      .then((response) => saveEducation(response.data))
      .catch((error) => console.log(error));
    }
  }
  useEffect(() => {
    getCV();
  }, []);
  console.log(JSON.stringify(res));
  console.log(theData);
  return (
    <main id="printable">
      <Intro {...res}></Intro>
      <Education
        {...theData}
      ></Education>
      <Experience
        {...theData}
      ></Experience>
      <Projects
        {...theData}
      ></Projects>
      <Achievements
        {...{
          achievements: ["Got AIR 1 in JEE Advanced 2018"],
        }}
      ></Achievements>
    </main>
  );
}
