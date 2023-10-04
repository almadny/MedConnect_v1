import React, { useState } from 'react';
import { Outlet } from 'react-router-dom';
import DashboardSidebar from '../pages/Dashboard/DashboardSidebar';
import Logo from '../components/Logo';
import {GiHamburgerMenu} from 'react-icons/gi';

const DashboardLayout = () => {
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
                <DashboardSidebar />
            </nav>
            <div className="md:hidden bg-cyan-700">
                {navOpen && <DashboardSidebar />}
            </div>
            <main className="flex-1">
                <section className='border-b-2 p-4'>
                    <div className="flex justify-between items-start">
                        <div className="">
                            <h1 className='md:text-4xl font-bold'>Welcome,<br/> John Doe</h1>
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

export default DashboardLayout;
