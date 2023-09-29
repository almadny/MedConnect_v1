import React, { useState, useEffect } from 'react';
import Video from 'twilio-video';

const PRoom = () => {
  const [roomName, setRoomName] = useState(''); // Initialize with the room name received from the backend
  const [token, setToken] = useState(''); // Initialize with the access token received from the backend
  const [isAudioEnabled, setIsAudioEnabled] = useState(true);
  const [isCameraEnabled, setIsCameraEnabled] = useState(true);

  const toggleAudio = () => {
    // Implement logic to toggle audio
    setIsAudioEnabled(!isAudioEnabled);
  };

  const toggleCamera = () => {
    // Implement logic to toggle camera
    setIsCameraEnabled(!isCameraEnabled);
  };

  const endCall = () => {
    // Implement logic to end the call
  };

  useEffect(() => {
    if (token && roomName) {
      Video.connect(token, {
        name: roomName,
        audio: isAudioEnabled,
        video: { enabled: isCameraEnabled },
      }).then((room) => {
        // Handle room events and UI updates here
      });
    }
  }, [token, roomName, isAudioEnabled, isCameraEnabled]);

  return (
    <div>
      <div className="flex justify-center mt-4">
        <Video />
      </div>
      <div className="flex justify-center mt-4">
        <button
          className={`mr-4 ${
            isAudioEnabled ? 'bg-green-500' : 'bg-red-500'
          } text-white px-4 py-2 rounded-lg`}
          onClick={toggleAudio}
        >
          {isAudioEnabled ? 'Mute' : 'Unmute'}
        </button>
        <button
          className={`mr-4 ${
            isCameraEnabled ? 'bg-green-500' : 'bg-red-500'
          } text-white px-4 py-2 rounded-lg`}
          onClick={toggleCamera}
        >
          {isCameraEnabled ? 'Turn Off Camera' : 'Turn On Camera'}
        </button>
        <button
          className="bg-red-500 text-white px-4 py-2 rounded-lg"
          onClick={endCall}
        >
          End Call
        </button>
      </div>
    </div>
  );
};


export default PRoom
