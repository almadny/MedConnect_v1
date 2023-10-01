import React, { useState } from 'react'
import Logo from '../../components/Logo'
import LoginImg from '../../assets/Login-image.jpg'
import { useNavigate } from 'react-router-dom'

const PatientSignUp = () => {

  const [fname, setFname] = useState("")
  const [lname, setLname] = useState("")
  const [email, setEmail] = useState("")
  const [dob, setDob] = useState("")
  const [password, setPassword] = useState("")
  const navigate = useNavigate()

  const handleSignUp = async (e) => {
    let data = { fname, lname, email, dob, password };
    console.log(data);
    console.log(dob);
    
    e.preventDefault()

    try {
      const response = await fetch('/api/users/regPatient', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email_address: email,
          hashed_password: password,
          first_name: fname,
          last_name: lname,
          other_name: '',
          dob_str: dob,
          gender: '',
          phone_number: '',
          date_of_birth: dob,
        }),
      });

      if (response.status=== 200) {
        navigate('/Login')
      }
  
      if (!response.ok) {
        throw new Error('Error sending data');
      }
  
      const responseData = await response.json();
      console.log('Response from API:', responseData);
    } catch (error) {
      console.error('Error sending data:', error);
    }
  };
  

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
          <h2 className='text-4xl dark:text-white font-bold text-center'>SIGN UP</h2>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>First Name </label>
            <input value={fname} onChange={(e)=> setFname(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="text"/>
          </div>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Last Name </label>
            <input value={lname} onChange={(e)=> setLname(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="text"/>
          </div>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Email </label>
            <input value={email} onChange={(e)=> setEmail(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="email"/>
          </div>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Date of Birth </label>
            <input value={dob} onChange={(e)=> setDob(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="date"/>
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
          <div>
            <p>Want to register a hospital instead? <a href='/HSignUp'>Click here</a></p>
          </div>
        </form>
      </div>
    </div>
  )
}

export default PatientSignUp

