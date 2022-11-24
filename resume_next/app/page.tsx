"use client";
import axios from "axios";
import { useEffect, useState } from "react";
import { getConstantValue } from "typescript";
import "./(resume)/resume.css";
import "./(resume)/experiance";
import Intro from "./(resume)/intro";
import Experience from "./(resume)/experiance";
import Skills from "./(resume)/skill";
import { useSearchParams } from "next/navigation";
import Head from "next/head";

const url = "http://127.0.0.1:8000/core/applicant/";

export default function HomePage() {
  const [res, setRes] = useState(null);
  const searchParams = useSearchParams();
  const search = searchParams.get("search");

  function getCV() {
    axios
      .get(url, { params: { search: search } })
      .then((response) => setRes(response.data))
      .catch((error) => console.log(error));
  }
  useEffect(() => {
    getCV();
  }, []);

  return (
    <main>
      {/* <Head>
      <link key="9986" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia"/>
      <title key="99986" >Hello</title>
      </Head> */}
      <Intro
        {...{
          name: "Narayan Gupta",
          email: "narayan1011g@gmail.com",
          gitHub: "https://github.com/NarayanNarayan",
          linkedIn: "https://www.linkedin.com/in/narayan-gupta-539470205/",
        }}
      ></Intro>
      <Experience
        {...{
          topic: "Software Engineering 2 @ Citrix",
          fromDate: "Aug22",
          toDate: "Aug22",
          description: "No Work",
          line: ["Some work", "Some work", "Some work", "Some work"],
        }}
      ></Experience>
      <Skills></Skills>
      <p>{JSON.stringify(res)}</p>
      <button onClick={getCV}>Click me</button>
    </main>
  );
}
