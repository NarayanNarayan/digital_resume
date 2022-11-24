import "./navbar.css";
import Link from "next/link";
import { useRouter } from "next/navigation";
import Image from "next/image";
import { useState } from "react";

/* (<Link
  href={{
    pathname: '/about',
    query: { name: 'test' },
  }}
>
  About
</Link>) */

export default function Navbar() {
  const [search, setSearch] = useState("");
  const router = useRouter();

  return (
    <nav>
      <ul className="navbar-nav">
        <li className="nav-item">
          <a className="nav-link" href="/">
            Home
          </a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="/">
            Home 2
          </a>
        </li>
        <li className="nav-item">
          <input
            className="searchbar"
            type="text"
            placeholder="Search"
            onChange={(e) => setSearch(e.target.value)}
            
            /* onSubmit={(e) => router.push(href: {
              pathname: "/",
              query: { search: search },
            })} */
          ></input>
        </li>
        <li className="nav-item">
          <Link
            id="searchbutton"
            href={
              search == ""
                ? {
                    pathname: "/",
                  }
                : {
                    pathname: "/",
                    query: { search: search },
                  }
            }
          >
            <span>
              <Image
                src="/search.svg"
                alt="Search Logo"
                width={30}
                height={30}
                //onClick={}
              />
            </span>
          </Link>
        </li>
        <li className="nav-item right-aligned">
          <div>
            <a className="nav-link" href="/">
              Print
            </a>
            
            <a className="nav-link" href="/">
              Log In
            </a>
          </div>
        </li>
      </ul>
    </nav>
  );
}
