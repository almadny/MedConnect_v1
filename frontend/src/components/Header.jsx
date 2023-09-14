import { useState } from "react";
import {GiHamburgerMenu} from 'react-icons/gi';
import {MdClose} from 'react-icons/md';
import Logo from "./Logo";

function Header() {
  const [navBar, setNavBar] = useState(false)
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <main>
        <nav  className={`w-full bg-white fixed top-0 left-0 right-0 z-50`}>
          <div className="justify-between px-10 md:mx-auto md:max-w-8xl items-center md:flex">
            <div className="flex items-center justify-between py-3 md:py-6 md:block">
              <a href="/">
                <h1>
                  <Logo />
                </h1>
              </a>
              <div className="md:hidden">
                <button className="p-2 right-0 text-cyan-200 rounded-md outline-none focus:border-cyan-400" onClick={() => setNavBar(!navBar)}
                >
                  {navBar ? (
                    <MdClose width={30} height={30} className="text-cyan-200"/>
                  ) : (
                    <GiHamburgerMenu width={30} height={30} className="focus:border-none active:border-none" />
                  )}
                </button>
              </div>
            </div>
            <div className={`pb-3 mt-8 md:block md:pb-0 md:mt-0 ${
                  navBar ? 'p-12 md:p-0 block' : 'hidden'
                }`}>
              <div>
                <ul className="h-screen md:h-auto items-center justify-center md:flex lg:pt-3 ">
                  <li className="pb-6 text-lg dark:text-white py-2 md:px-6 text-center border-b-2 md:border-b-0  hover:bg-cyan-900  border-cyan-200  md:hover:text-cyan-600 md:hover:bg-transparent">
                    <a href="/" onClick={() => setNavBar(!navBar)}>
                      Home
                    </a>
                  </li>
                  <li className="pb-6 text-lg dark:text-white py-2 px-6 text-center border-b-2 md:border-b-0  hover:bg-cyan-600  border-cyan-200  md:hover:text-cyan-600 md:hover:bg-transparent">
                    <a href="" onClick={() => setNavBar(!navBar)}>
                      About
                    </a>
                  </li>
                  <li className="pb-6 text-lg dark:text-white py-2 px-6 text-center border-b-2 md:border-b-0  hover:bg-cyan-600  border-cyan-200  md:hover:text-cyan-600 md:hover:bg-transparent">
                    <a href="" onClick={() => setNavBar(!navBar)}>
                      Services
                    </a>
                  </li>
                  <li className="pb-6 text-lg dark:text-white py-2 px-6 text-center border-b-2 md:border-b-0  hover:bg-cyan-600  border-cyan-200  md:hover:text-cyan-600 md:hover:bg-transparent">
                    <a href="" onClick={() => setNavBar(!navBar)}>
                      Bookings
                    </a>
                  </li>
                  <li className="pb-6 text-lg dark:text-white py-2 px-6 text-center border-b-2 md:border-b-0  hover:bg-cyan-600  border-cyan-200  md:hover:text-cyan-600 md:hover:bg-transparent">
                    <a href="/Blog" onClick={() => setNavBar(!navBar)}>
                      Blog
                    </a>
                  </li>
                  <li className="pb-6 text-lg dark:text-white py-2 px-6 text-center border-b-2 md:border-b-0  hover:bg-cyan-600  border-cyan-200  md:hover:text-cyan-600 md:hover:bg-transparent">
                    <a href="" onClick={() => setNavBar(!navBar)}>
                      FAQs
                    </a>
                  </li>
                  {isLoggedIn ? (
                  <>
                    <li className="pb-6 text-lg py-2 px-6 text-center border-b-2 md:border-b-0 hover:bg-cyan-600 border-cyan-200 md:hover:text-cyan-600 md:hover-bg-transparent">
                      <a href="/patient_dashboard" onClick={() => setNavBar(!navBar)}>
                        Dashboard
                      </a>
                    </li>
                  </>
                ) : (
                  <>
                    <li className="pb-6 text-lg py-2 px-6 text-center border-b-2 md:border-b-0 hover:bg-cyan-600 border-cyan-200 md:hover:text-cyan-600 md:hover-bg-transparent">
                      <a href="/Login" onClick={() => setNavBar(!navBar)}>
                        Log In
                      </a>
                    </li>
                    <li className="pb-6 text-lg py-2 px-6 text-center border-b-2 md:border-b-0 hover:bg-cyan-600 border-cyan-200 md:hover:text-cyan-600 md:hover-bg-transparent">
                      <a
                        className="lg:border-2 lg:border-cyan-600 lg:px-4 lg:py-2 rounded-md"
                        href="/PSignUp"
                        onClick={() => setNavBar(!navBar)}
                      >
                        Sign Up
                      </a>
                    </li>
                  </>
                )}
                </ul>
              </div>
            </div>
          </div>
        </nav>
    </main>
  )
}

export default Header;