'use client';
import { useState } from "react";
import { useSearchParams } from 'next/navigation';

function point(s:string){
  return (
    <li>{s}</li>
  )
}

function Experience(exp:any){
  return (
    <>
    <div className="hcontainer"> 
    <div className="h3">{exp.topic}</div>
    <div >{exp.fromDate}-{exp.toDate}</div>
    </div>
    <p className="h4">{exp.description}</p>
    
    {exp.line.map(point)}
    </>
  );
}

export default function Experiences(exps:any) {

  return (
    <>
    <div className="h2">Experience</div>
    <Experience {...exps}></Experience>
    </>
  );
}

export function Projects(proj:any){
  return (
    <>
    <div className="h2">Project</div>
    <Experience {...proj}></Experience>
    </>
  )
}