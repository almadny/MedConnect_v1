import React from 'react'
import Header from '../../components/Header'
import blogImage from '../../assets/Login-image.jpg'
import Footer from '../../components/Footer'

const Blog = () => {
  return (
    <div>
      <section>
        <Header />
      </section>
      <section className="md:mt-20 mt-10">
        <h1 className="text-center text-2xl py-8 mb-3 md:border md:border-b-4 md:text-3xl font-bold">Health Information Hub</h1><br/>
      </section>
      <section className='px-10 md:mx-auto md:max-w-8xl'>
        <p class="mb-5 md:text-2xl text-justify"><strong>Popular Posts</strong></p>
        <div className='grid md:grid-cols-4 gap-3'>
          <div className='border border-white p-5 drop-shawdow-md'>
            <img src={blogImage}/>
            <p>Date</p>
            <p>Title</p>
          </div>
          <div className='border border-white p-5 drop-shawdow-md'>
            <img src={blogImage}/>
            <p>Date</p>
            <p>Title</p>
          </div>
          <div className='border border-white p-5 drop-shawdow-md'>
            <img src={blogImage}/>
            <p>Date</p>
            <p>Title</p>
          </div>
          <div className='border border-white p-5 drop-shawdow-md'>
            <img src={blogImage}/>
            <p>Date</p>
            <p>Title</p>
          </div>
        </div>
      </section>
      <section className='px-10 md:mx-auto md:max-w-8xl'>
        <p class="mb-5 md:text-2xl text-justify"><strong>Latest Posts</strong></p>
        <div className='grid md:grid-cols-4 gap-3'>
          <div className='border border-white p-5 drop-shawdow-md'>
            <a href='' className='cursor-pointer'>
              <img src={blogImage}/>
              <p>Date</p>
              <p>Title</p>
            </a>
          </div>
          <div className='border border-white p-5 drop-shawdow-md'>
            <img src={blogImage}/>
            <p>Date</p>
            <p>Title</p>
          </div>
          <div className='border border-white p-5 drop-shawdow-md'>
            <img src={blogImage}/>
            <p>Date</p>
            <p>Title</p>
          </div>
          <div className='border border-white p-5 drop-shawdow-md'>
            <img src={blogImage}/>
            <p>Date</p>
            <p>Title</p>
          </div>
        </div>
      </section>
      <section>
        <Footer/>
      </section>
    </div>
  )
}

export default Blog
