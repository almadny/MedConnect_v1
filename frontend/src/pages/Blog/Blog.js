import React, { useState, useEffect } from 'react';
import { BrowserRouter as Link } from 'react-router-dom';
import Header from '../../components/Header';
import blogImage from '../../assets/Login-image.jpg';
import Footer from '../../components/Footer';

const Blog = () => {
  const [popularPosts, setPopularPosts] = useState([]);
  const [latestPosts, setLatestPosts] = useState([]);

  useEffect(() => {
    fetch('/api/blog/posts')
      .then((response) => response.json())
      .then((data) => {
        const popular = [];
        const latest = [];

        data.posts.forEach((post) => {
          if (post.category === 'Popular') {
            popular.push(post);
          } else if (post.category === 'Latest') {
            latest.push(post);
          }
        });

        setPopularPosts(popular);
        setLatestPosts(latest);
      })
      .catch((error) => console.error('Error fetching posts:', error));
  }, []);

  return (
      <div>
        <section>
          <Header />
        </section>
        <section className="md:mt-20 mt-10">
          <h1 className="text-center text-2xl py-8 mb-3 md:border md:border-b-4 md:text-3xl font-bold">Health Information Hub</h1><br />
        </section>
        <section className='px-10 md:mx-auto md:max-w-8xl'>
          <p className="mb-5 md:text-2xl text-justify"><strong>Popular Posts</strong></p>
          <div className='grid md:grid-cols-4 gap-3'>
            {popularPosts.map((post) => (
              <div className='border border-white p-5 drop-shadow-md' key={post.id}>
                <Link to={`/post/${post.id}`} className='cursor-pointer'>
                  <img src={blogImage} alt={post.title} />
                  <p>Date: {post.date_posted}</p>
                  <p>Title: {post.title}</p>
                </Link>
              </div>
            ))}
          </div>
        </section>
        <section className='px-10 md:mx-auto md:max-w-8xl'>
          <p className="mb-5 md:text-2xl text-justify"><strong>Latest Posts</strong></p>
          <div className='grid md:grid-cols-4 gap-3'>
            {latestPosts.map((post) => (
              <div className='border border-white p-5 drop-shadow-md' key={post.id}>
                <Link to={`/post/${post.id}`} className='cursor-pointer'>
                  <img src={blogImage} alt={post.title} />
                  <p>Date: {post.date_posted}</p>
                  <p>Title: {post.title}</p>
                </Link>
              </div>
            ))}
          </div>
        </section>
        <section>
          <Footer />
        </section>
        
      </div>
  );
};

export default Blog;