'use client';
import { useState } from "react";
import { useSearchParams } from 'next/navigation';

function Achievement(acmt:any){
  return (
    <>
      <div>{acmt.point}</div>
    </>
  )
}

export default function Achievements(acmts:any) {

  return (
    <>
    <div className="contentHeading">Achievements</div>
    
    </>
  );
}
