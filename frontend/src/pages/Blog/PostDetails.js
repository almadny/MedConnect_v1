import React from 'react'

const PostDetails = ({ match }) => {
  const postId = match.params.id;

  return (
    <div>
      <h2>Post Details</h2>
      <p>Post ID: {postId}</p>
      <p>{match.params.content}</p>
    </div>
  );
};
export default PostDetails
