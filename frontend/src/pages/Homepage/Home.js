import React from 'react'
import Header from '../../components/Header'
import Hero from '../../assets/AboutImg.jpg'
import Footer from '../../components/Footer'
import VC from '../../assets/virtual-consultation.jpg'

const Home = () => {
  return (
    <div className=''>
      <section className='fixed'>
        <Header />
      </section>
      <section>
        <div className='md:mt-20 md:max-w-8xl mx-auto' style={{
            background: `url(${Hero})`,
            backgroundSize: "cover",
            backgroundRepeat: "no-repeat"
            }}
        >
          <div className='px-6'>
            <div className='py-40 font-bold'>
              <p className='pb-3 md:text-5xl'>Empowering Health at Your Fingertips</p>
              <p className='md:text-5xl pb-6'>Experience Care Without Boundaries</p>
              <a href='/PSignUp' className='text-white text-2xl cursor-pointer bg-cyan-600 p-2 rounded-md'>Get Started</a>
            </div>
            <div className=''>
              <h3 className='lg:text-2xl font-bold mb-2'>Need to find a hospital urgently?</h3>
              <a href='/FindHospital'>
                <button className='text-white font-bold text-xl cursor-pointer bg-cyan-600 p-2 rounded-md md:mb-32'>Find nearest hospital</button>
              </a>
            </div>
          </div>
        </div>
      </section>
      <section id='services'>
        <div>
          <h2 className='md:text-3xl font-bold flex justify-center my-10'>Our core sevices</h2>
          <div className='grid grid-cols-4 gap-5 max-w-7xl mx-auto mb-10'>
            <div>
              <img src={VC} className='mb-6 rounded-md'/>
              <p>Virtual consultations</p>
            </div>
            <div>
              <img src={VC} className='mb-6 rounded-md'/>
              <p>Find closest hospital</p>
            </div>
            <div>
              <img src={VC} className='mb-6 rounded-md' />
              <p>Health Information hub</p>
            </div>
            <div>
              <img src={VC} className='mb-6 rounded-md'/>
              <p>Specialist Doctors</p>
            </div>
          </div>
        </div>
      </section>
      <section className='my-10'>
        <p className='text-3xl font-bold flex justify-center'>How it works</p>
      </section>
      <Footer />
    </div>
  )
}

export default Home