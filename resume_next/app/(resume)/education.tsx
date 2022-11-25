'use client';
import { useState } from "react";
import { useSearchParams } from 'next/navigation';

function point(s:string){
  return (
    <li>{s}</li>
  )
}

function AEducation(aedu:any) {

  return (
    <>
    <span style={{ marginRight: "auto",fontWeight:"bold"}}>{aedu.collegeName}</span>
    {/* <span style={{ marginLeft: "auto",}}>{aedu.fromDate}-{aedu.toDate}</span> */}
    <span style={{ marginRight: "auto",}}>{aedu.degreeName}</span>
    <span style={{ marginRight: "auto",}}>{aedu.major}</span>
    <span style={{ marginRight: "auto",}}>{aedu.cgpa}</span>
    
    </>
  );
}

export default function Education(data:any) {

  return (
    <>
    <div className="h2">Education</div>
    {/* <AEducation {...data.education}></AEducation> */}
    {data.education.map(AEducation)}
    </>
  );
}
