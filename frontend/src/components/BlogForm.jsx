import React, { useState } from "react";

const BlogForm = () => {
  const [formData, setFormData] = useState({
    title: "",
    image: null,
    body: "",
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleImageChange = (e) => {
    const imageFile = e.target.files[0];
    setFormData({
      ...formData,
      image: imageFile,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Implement the publish/save logic here
  };

  return (
    <div className="container mx-auto mt-8">
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="title" className="block text-gray-700 font-bold">
            Title
          </label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleInputChange}
            className="w-full p-2 border rounded"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="image" className="block text-gray-700 font-bold">
            Image
          </label>
          <input
            type="file"
            id="image"
            name="image"
            accept="image/*"
            onChange={handleImageChange}
            className="w-full p-2 border rounded"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="body" className="block text-gray-700 font-bold">
            Body
          </label>
          <textarea
            id="body"
            name="body"
            value={formData.body}
            onChange={handleInputChange}
            className="w-full p-2 border rounded"
            rows="6"
            required
          />
        </div>
        <div className="flex justify-end">
          <button
            type="submit"
            className="bg-blue-500 text-white px-4 py-2 rounded mr-2"
          >
            Publish
          </button>
          <button
            type="button"
            className="bg-gray-400 text-gray-700 px-4 py-2 rounded"
          >
            Save
          </button>
        </div>
      </form>
    </div>
  );
};

export default BlogForm;
