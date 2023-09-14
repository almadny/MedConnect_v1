import React, { useState } from 'react';
import { Outlet } from 'react-router-dom';
import DashboardSidebar from '../pages/Dashboard/DashboardSidebar';
import Logo from '../components/Logo';
import {GiHamburgerMenu} from 'react-icons/gi';

const DashboardLayout = () => {
    const [navOpen, setNavOpen] = useState(false);

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
                <div>Hello World!</div>
                <Outlet />
            </main>
        </section>
    );
};

export default DashboardLayout;
