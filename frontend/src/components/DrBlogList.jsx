import React, { useState, useEffect } from "react";
import { getPublishedArticles } from "../api";

const DrBlogList = () => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getPublishedArticles()
      .then((response) => {
        setArticles(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching articles: ", error);
      });
  }, []);

  return (
    <div className="container mx-auto mt-8">
      {loading ? (
        <p>Loading...</p>
      ) : articles.length > 0 ? (
        <ul>
          {articles.map((article) => (
            <li key={article.id}>
              <h2>{article.title}</h2>
              <p>{article.body}</p>
              {/* Display image here */}
            </li>
          ))}
        </ul>
      ) : (
        <p>No published articles yet.</p>
      )}
    </div>
  );
};

export default DrBlogList;
