import React from 'react';
import { NavLink } from 'react-router-dom';
import Logo from '../../components/Logo';
import { useAuth } from '../../context/UseAuth'
import { useNavigate } from 'react-router-dom';

const NavData = [
    { name: 'Book Appointment', link: '/patient_dashboard/find_a_doctor' },
    { name: 'Appointments', link: '/patient_dashboard/appointment' },
    { name: 'Room', link: '/patient_dashboard/patient_room' },
    { name: 'Logout', link: '/logout'}
];

const DashboardSidebar = () => {
    const {logout} = useAuth()
    const navigate = useNavigate()
    const handleLogout = () => {
        logout()
        navigate('/')
    }
    return (
        <aside className="flex flex-col pt-3 min-h-screen w-full">
            <a className="hidden md:block py-4 pb-20 w-full text-center text-slate-100" href="/">
                <Logo />
            </a>
            <nav className="flex flex-col gap-12">
                <div className="flex flex-col gap-0 justify-center">
                    {NavData.slice(0, -1).map(({ name, link }, index) => {
                        return (
                            <NavLink
                                key={index}
                                to={link}
                                end={link === "/patient_dashboard" && true}
                                activeClassName="text-blue-500"
                                className="text-slate-100 hover:text-blue-500 py-6 px-20 border-t-2"
                            >
                                <span>{name}</span>
                            </NavLink>
                        );
                    })}
                </div>
                <div className='flex justify-center border-t-2 py-2 text-slate-100'>
                    {NavData.slice(-1).map(({ name }, index) => {
                        return (
                            <button onClick={(e)=> handleLogout(e.preventDefault())} className="border-0" key={index}>
                                <span>{name}</span>
                            </button>
                        );
                    })}
                </div>
            </nav>
        </aside>
    );
};

export default DashboardSidebar;
