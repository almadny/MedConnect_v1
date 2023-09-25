import React, { useEffect, useState } from 'react';
import Video from 'twilio-video';

const VideoChat = () => {
  const [room, setRoom] = useState(null);
  const [localVideoTrack, setLocalVideoTrack] = useState(null);
  const [remoteParticipants, setRemoteParticipants] = useState([]);

  useEffect(() => {
    const getTokenFromServer = async () => {
      const response = await fetch('/api/video/generateAccessToken');
      const data = await response.json();
      const token = String(data.token);

      Video.connect(token, {
        name: 'my-room-name',
      }).then(room => {
        setRoom(room);

        Video.createLocalVideoTrack().then(track => {
          setLocalVideoTrack(track);
          const localMediaContainer = document.getElementById('local-media-container');
          localMediaContainer.appendChild(track.attach());
        });

        room.on('participantConnected', participant => {
          setRemoteParticipants(prevParticipants => [...prevParticipants, participant]);
        });

        room.on('participantDisconnected', participant => {
          setRemoteParticipants(prevParticipants =>
            prevParticipants.filter(p => p !== participant)
          );
        });
      });
    };

    getTokenFromServer();
  }, []);

  useEffect(() => {
    return () => {
      if (room) {
        room.disconnect();
      }
      if (localVideoTrack) {
        localVideoTrack.stop();
      }
    };
  }, [room, localVideoTrack]);

  return (
    <div>
      <div id="local-media-container"></div>
      <div id="remote-media-container">
        {remoteParticipants.map(participant => (
          <div key={participant.sid}>{participant.tracks[1]?.attach()}</div>
        ))}
      </div>
    </div>
  );
};

export default VideoChat;
