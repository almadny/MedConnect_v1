import React, { useState, useCallback, useEffect } from 'react';
import Room from './Room'

const VideoChat = () => {
  const [roomName, setRoomName] = useState('');
  const [token, setToken] = useState(null);

  useEffect(()=> {
    setToken(localStorage.getItem('video_token'))
    setRoomName(localStorage.getItem('room'))
    console.log(token)
    console.log(roomName)
  })

  // const handleRoomNameChange = useCallback(event => {
  //   setRoomName(event.target.value);
  // }, []);

  const endCall = useCallback(event => {
    setToken(null);
  }, []);

  let render;
  if (token) {
    render = (
      <Room roomName={roomName} token={token} endCall={endCall} />
    );
  }

  return render
};

export default VideoChat