import React, { useState, useEffect } from "react";
import Video from 'twilio-video';
import Participant from "./Participant";
import Header from '../../components/Header';
import Footer from '../../components/Footer';

const Room = ({ roomName, token, endCall }) => {
  const [room, setRoom] = useState(null);
  const [participants, setParticipants] = useState([]);

  const remoteParticipants = participants.map(participant => (
    <Participant key={participant.sid} participant={participant} />
  ));

  useEffect(() => {
    const participantConnected = participant => {
      setParticipants(prevParticipants => [...prevParticipants, participant]);
    };
    const participantDisconnected = participant => {
      setParticipants(prevParticipants =>
        prevParticipants.filter(p => p !== participant)
      );
    };
    Video.connect(token, {
      name: roomName
    }).then(room => {
      setRoom(room);
      room.on('participantConnected', participantConnected);
      room.on('participantDisconnected', participantDisconnected);
      room.participants.forEach(participantConnected);
    });
    return () => {
      setRoom(currentRoom => {
        if (currentRoom && currentRoom.localParticipant.state === 'connected') {
          currentRoom.localParticipant.tracks.forEach(function(trackPublication) {
            trackPublication.track.stop();
          });
          currentRoom.disconnect();
          return null;
        } else {
          return currentRoom;
        }
      });
    };
  }, [roomName, token]);

  return (
    <div className="h-screen flex flex-col justify-between">
      <Header />

      <div className="bg-slate-700 text-gray-300 text-3xl font-bold p-4">
        Room: {roomName}
      </div>

      <div className="relative flex-1 bg-gray-200">
        {/* Remote Participants */}
        <div className="absolute inset-0">
          <h3 className="text-xl font-semibold p-4">Remote Participants</h3>
          <div className="flex flex-wrap p-4 space-x-4 space-y-4">
            {remoteParticipants}
          </div>
        </div>

        {/* Local Participant Overlay */}
        <div className="absolute bottom-4 right-4">
          {room ? (
            <Participant
              key={room.localParticipant.sid}
              participant={room.localParticipant}
            />
          ) : (
            ''
          )}
        </div>
      </div>
      <button
        onClick={endCall}
        className="bg-red-500 text-white p-2 m-4 rounded-lg hover:bg-red-600"
      >
        End Call
      </button>
    </div>
  );
};

export default Room;
