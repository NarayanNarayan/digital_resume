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
import Preview from "./preview";

const url = "http://127.0.0.1:8000/core/applicant/";
const initialData={results:[{
  id:"1",
  name: "Narayan Gupta",
  headline:" Google | Microsoft | Meta | Ribrik",
  email: "narayan1011g@gmail.com",
  github: "https://github.com/NarayanNarayan",
  linkedin: "https://www.linkedin.com/in/narayan-gupta-539470205/",
  experience:[{position:"Principle Engineer",institutionName:"Google"}],
  education:[{degreeName:"PhD",major:"Physics",collegeName:"MIT"}]
}]}
export default function HomePage() {
  const [res, setRes] = useState(initialData);
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
  }, [search]);

  return (
    <>
      {res.results.map(Preview)}
      {/* <Preview {...(res.results[0])}></Preview> */}
      <p>{JSON.stringify(res)}</p>
    </>
  );
}
{/* <Preview
        {...{
          id:"1",
          name: "Narayan Gupta",
          headline:" Google | Microsoft | Meta | Ribrik",
          email: "narayan1011g@gmail.com",
          github: "https://github.com/NarayanNarayan",
          linkedin: "https://www.linkedin.com/in/narayan-gupta-539470205/",
          experience:[{position:"Principle Engineer",institutionName:"Google"}],
          education:[{degreeName:"PhD",major:"Physics",collegeName:"MIT"}]
        }}
      ></Preview> */}