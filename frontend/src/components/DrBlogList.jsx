import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const DrBlogList = () => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
      fetch('/api/blog/posts')
        .then((response) => response.json())
        .then((data) => {
  
          data.posts.forEach((post) => {
            articles.push(post)
          });
          console.log(articles)
        })
        .catch((error) => console.error('Error fetching posts:', error));
    }, []);

  return (
    <div className='grid md:grid-cols-3 gap-3'>
      {articles.map((post) => (
        <div className='border border-white p-5 drop-shadow-md bg-white' key={post.id}>
          <Link to={`/post/${post.id}`} className='cursor-pointer'>
            <p>Date: {post.date_posted}</p>
            <p>Title: {post.title}</p>
          </Link>
        </div>
      ))}
    </div>
  );
};

export default DrBlogList;
