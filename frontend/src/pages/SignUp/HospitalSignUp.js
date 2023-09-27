import React, { useState } from 'react'
import Logo from '../../components/Logo'
import LoginImg from '../../assets/Login-image.jpg'
import { useNavigate } from 'react-router-dom'

const HospitalSignUp = (e) => {

  const [hname, setHname] = useState("")
  const [email, setEmail] = useState("")
  const [add, setAdd] = useState("")
  const [contact, setContact] = useState("")
  const [password, setPassword] = useState("")
  const navigate = useNavigate()

  const handleSignUp = async () => {
    let data = {hname, email, add, password, contact}
    console.log(data)

    const apiUrl = '/api/users/healthcares'

    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name: hname, address: add, email_address: email, password: password }),
    });

    if (response.status === 200) {
      navigate('/Login')
      e.preventDefault()
    }
  }

  return (
    <div className='grid grid-cols-1 sm:grid-cols-2 h-screen w-full'>
        <div className='hidden sm:block' style={{
            background: `url(${LoginImg})`,
            backgroundSize: "cover",
            backgroundPosition: "center",
            backgroundRepeat: "no-repeat"
            }}
        >
          <div className='w-full h-full backdrop-brightness-75'>
            <Logo />
          </div>
        </div>
      <div className='bg-slate-100 flex flex-col justify-center'>
        <form className= 'mx-12 bg-slate-200 px-8 p-8 rounded-lg'>
          <h2 className='text-4xl dark:text-white font-bold text-center'>REGISTER YOUR HOSPITAL</h2>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Hospital Name </label>
            <input value={hname} onChange={(e)=> setHname(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="text"/>
          </div>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Email </label>
            <input value={email} onChange={(e)=> setEmail(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="email"/>
          </div>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Address </label>
            <input value={add} onChange={(e)=> setAdd(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="text"/>
          </div>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Contact Number </label>
            <input value={contact} onChange={(e)=> setContact(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="tel"/>
          </div>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Password </label>
            <input value={password} onChange={(e)=> setPassword(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="password"/>
          </div>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Confirm Password </label>
            <input className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="password"/>
          </div>
          <div className='border-2 border-slate-500 rounded w-full my-5 py-2 bg-slate-500 text-slate-100 shadow-lg hover:shadow-slate-600 font-semibold'>
            <input onClick={handleSignUp} className='cursor-pointer w-full mx-auto' type="submit" value="Sign Up"/>
          </div>
        </form>
      </div>
    </div>
  )
}

export default HospitalSignUp
