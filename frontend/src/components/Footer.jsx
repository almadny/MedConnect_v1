import React from 'react'
import Logo from './Logo'

const Footer = () => {
  return (
    <div className='bg-slate-700 text-gray-300'>
      <div className='flex justify-center py-10'>
        <Logo />
      </div>
      <div className='grid grid-cols-4 pb-10'>
        <div className='mx-auto'>
          <p className='font-bold'>Company</p>
          <p>About us</p>
        </div>
        <div className='mx-auto'>
          <p className='font-bold'>Resources</p>
          <p>FAQs</p>
          <p>Blog</p>
        </div>
        <div className='mx-auto'>
          <p className='font-bold'>Legal</p>
          <p>Privacy policy</p>
          <p>Terms of use</p>
          <p>Cookie Policy</p>
        </div>
        <div className='mx-auto'>
          <p className='font-bold'>Contact</p>
          <p>About us</p>
          <p>info@medconnect.org</p>
        </div>
      </div>
    </div>
  )
}

export default Footer
