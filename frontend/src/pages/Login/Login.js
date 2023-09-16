import React, { useState } from 'react'
import Logo from '../../components/Logo'
import LoginImg from '../../assets/Login-image.jpg'
import { useAuth } from '../../context/UseAuth'

const Login = () => {

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const { login} = useAuth();

  const handleSignIn = async () => {
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email: 'your-email', password: 'your-password' }),
      });

      if (response.ok) {
        const userData = await response.json();
        login(userData);
      } else {
        console.error('Login failed');
      }
    } catch (error) {
      console.error('An error occurred during login:', error);
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
      {/* <img className='w-full h-full object-cover' src={LoginImg} alt="" /> */}
        </div>
      <div className='bg-slate-100 flex flex-col justify-center'>
        <form className= 'mx-12 bg-slate-200 px-8 p-8 rounded-lg'>
          <h2 className='text-4xl dark:text-white font-bold text-center'>SIGN IN</h2>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Email </label>
            <input value={email} onChange={(e) => setEmail(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="email"/>
          </div>
          <div className='flex flex-col text-slate-800 py-2'>
            <label>Password </label>
            <input value={password} onChange={(e) => setPassword(e.target.value)} className='rounded-lg mt-2 p-2 focus:border-slate-300 focus:bg-slate-100' type="password"/>
          </div>
          <div className='flex justify-between '>
            <p className='flex items-center'><input className='mr-2' type='checkbox'/>Remember me</p>
            <p>Forgot password?</p>
          </div>
          <div className='border-2 border-slate-500 rounded w-full my-5 py-2 bg-slate-500 text-slate-100 shadow-lg hover:shadow-slate-600 font-semibold'>
            <input onClick={handleSignIn} className='cursor-pointer w-full mx-auto' type="submit" value="Sign In"/>
          </div>
          <div>
            <p>You don't have an account? <a href=''>Sign Up</a></p>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Login
