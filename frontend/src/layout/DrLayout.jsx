import React, { useState } from 'react';
import { Outlet } from 'react-router-dom';
import DrSidebar from '../pages/DrDashboard/DrSidebar';
import Logo from '../components/Logo';
import {GiHamburgerMenu} from 'react-icons/gi';

const DrLayout = () => {
    const [navOpen, setNavOpen] = useState(false);
    const showDate = new Date();
    const displayTodaysDate = showDate.toDateString();

    return (
        <section className="md:flex min-h-screen">
            <header className="md:hidden flex items-center p-4 md:p-8 bg-cyan-700 z-10">
                <div className="md:hidden" onClick={() => setNavOpen((navOpen) => !navOpen)}>
                    <GiHamburgerMenu />
                </div>
                <div className="ps-20 text-slate-100">
                    <Logo />
                </div>
            </header>
            <nav className="hidden md:flex bg-cyan-700 z-10">
                <DrSidebar />
            </nav>
            <div className="md:hidden bg-cyan-700">
                {navOpen && <DrSidebar />}
            </div>
            <main className="flex-1">
                <section className='border-b-2 p-4'>
                    <div className="flex justify-between items-start">
                        <div className="">
                            <h1 className='md:text-4xl font-bold'>Welcome,<br/> Dr John Smith</h1>
                            <div className='md:text-xl'>
                                <p>{displayTodaysDate}</p>
                            </div>
                        </div>
                        {/* <div className="icon">
                        <NotificationBell />
                        </div> */}
                    </div>
                </section>
                <Outlet />
            </main>
        </section>
    );
};

export default DrLayout;
