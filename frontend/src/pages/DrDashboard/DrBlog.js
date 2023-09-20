import React, { useState } from "react";
import DrBlogList from "../../components/DrBlogList";
import BlogForm from "../../components/BlogForm";
import { AiOutlinePlus } from "react-icons/ai";

function DrBlog() {
  const [isFormOpen, setIsFormOpen] = useState(false);

  const toggleForm = () => {
    setIsFormOpen(!isFormOpen);
  };

  return (
    <div className="bg-gray-100 min-h-screen">
      <div className="container mx-auto p-8">
        <h1 className="text-3xl font-bold">My Blog</h1>
        <div className="mt-8">
          <DrBlogList />
        </div>
        <div className="fixed bottom-4 right-4">
          <a onClick={toggleForm}>
            <AiOutlinePlus />
          </a>
        </div>
        {isFormOpen && <BlogForm />}
      </div>
    </div>
  );
}

export default DrBlog;
