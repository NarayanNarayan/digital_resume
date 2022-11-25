'use client';
import { useState } from "react";
import { useSearchParams } from 'next/navigation';
import Link from "next/link";

export default function Preview(profile:any) {

  return (
    
    <div className="card">
      <div className="hcontainer">
    <div>
    <Link href={`/${profile.id}`}>
    <div className="h3">{profile.name}</div>
    </Link>
    <div >{profile.headline}</div>
{/*     <div>{profile.experiance[0].position} @ {profile.experiance[0].institutionName}</div>
    <div>{profile.education[0].degreeName} in {profile.education[0].major}</div>
    <div>{profile.education[0].collegeName} {profile.education[0].cgpa?"cgpa:"+profile.education[0].cgpa:""}</div>
 */}
    </div>
    
    <div className="links">
    <div className="link"><a href={`mailto:${profile.email}`}>Email:</a>{profile.email}</div>
    <div className="link"><a href={profile.github}>GitHub:</a>{profile.github}</div>
    <div className="link"><a href={profile.linkedin}>LinkedIn</a></div>

    </div>
    
    </div>
    </div>
    
    
    
  );
}
