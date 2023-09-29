import React, { useState, useEffect } from 'react';
import Video from 'twilio-video';

const Room = () => {
  const [roomName, setRoomName] = useState('');
  const [token, setToken] = useState('');
  const [isAudioEnabled, setIsAudioEnabled] = useState(true);
  const [isCameraEnabled, setIsCameraEnabled] = useState(true);
  const [activeRoom, setActiveRoom] = useState(null);
  const [participants, setParticipants] = useState([]);
  const [isConnected, setIsConnected] = useState(false);

  const toggleAudio = () => {
    setIsAudioEnabled(!isAudioEnabled);
  };

  const toggleCamera = () => {
    setIsCameraEnabled(!isCameraEnabled);
  };

  const endCall = () => {
    if (activeRoom) {
      activeRoom.disconnect();
    }
  };

  useEffect(() => {
    const fetchRoomData = async () => {
      try {
        const response = await fetch('/api/video/generateAccessToken');
        if (response.ok) {
          const data = await response.json();
          setRoomName(data.room);
          setToken(data.token);
        } else {
          console.error('Failed to fetch room data');
        }
      } catch (error) {
        console.error('Error fetching room data:', error);
      }
    };

    fetchRoomData();

    if (token && roomName) {
      Video.connect(token, {
        name: roomName,
        audio: isAudioEnabled,
        video: { enabled: isCameraEnabled },
      })
        .then((room) => {
          setActiveRoom(room);

          room.on('participantConnected', (participant) => {
            setParticipants((prevParticipants) => [...prevParticipants, participant]);
          });

          room.on('participantDisconnected', (participant) => {
            setParticipants((prevParticipants) =>
              prevParticipants.filter((p) => p !== participant)
            );
          });

          setIsConnected(true);
        })
        .catch((error) => {
          console.error('Error connecting to room:', error);
        });
    }

    return () => {
      if (activeRoom) {
        activeRoom.disconnect();
      }
    };
  }, [token, roomName, isAudioEnabled, isCameraEnabled, activeRoom]);

  return (
    <div>
      <div className="flex justify-center mt-4">
        {isConnected ? (
          <Video
            room={activeRoom}
            localParticipant={activeRoom.localParticipant}
          />
        ) : (
          <p>Connecting...</p>
        )}
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
      <div>
        <h3>Participants:</h3>
        <ul>
          {participants.map((participant) => (
            <li key={participant.sid}>{participant.identity}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Room;
