'use client';
import { useState } from "react";
import { useSearchParams } from 'next/navigation';

export default function Intro(profile:any) {

  return (
    <div className="hcontainer">
    <div className="h1">{profile.name}</div>
    <div className="links">
    <div className="link"><a href={`mailto:${profile.email}`}>Email</a></div>
    <div className="link"><a href={profile.githubid}>GitHub:{profile.github}</a></div>
    <div className="link"><a href={profile.linkedInid}>LinkedIn</a></div>

    </div>
    
    </div>
  );
}
