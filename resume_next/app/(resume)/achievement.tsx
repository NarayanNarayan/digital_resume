'use client';
import { useState } from "react";
import { useSearchParams } from 'next/navigation';

function point(s:string){
  return (
    <div>{s}</div>
  )
}

function Achievement(acmt:any){
  return (
    <>
      <div className="hcontainer">
      {acmt.achievements.map(point)}
        </div>
      
    </>
  );
}

export default function Achievements(acmts:any) {

  return (
    <>
    <div className="h2">Achievements</div>
    <Achievement {...acmts}></Achievement>
    </>
  );
}
