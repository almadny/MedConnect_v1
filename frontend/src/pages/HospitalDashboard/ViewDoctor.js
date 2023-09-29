import React, {useState, useEffect} from 'react'
import {CiEdit, CiSaveDown2} from 'react-icons/ci'
import {MdDelete} from 'react-icons/md'
import {FcCancel} from 'react-icons/fc'

const ViewDoctor = () => {
  const [editData, setEditData] = useState(null);

  const handleEdit = (id) => {
    const itemToEdit = data.find((item) => item.id === id);
    setEditData(itemToEdit);
  };

  const handleSaveEdit = () => {
    const indexToEdit = data.findIndex((item) => item.id === editData.id);
    const updatedData = [...data];

    updatedData[indexToEdit] = editData;
    setData(updatedData);
    setEditData(null);
  };

  const handleDelete = (id) => {
    const updatedData = data.filter((item) => item.id !== id);
    setData(updatedData);
  };

  const apiUrl = '/api/users/doctors'
  useEffect = () => {
    fetch(apiUrl, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    })
  }

  const [data, setData] = useState([
    {
      id: 1,
      fullName: 'Indiana Jones',
      contact: 'indijones@gmail.com',
      specialty: 'Opthamologist',
      licenseNumber: '41912',
    },
    {
      id: 2,
      fullName: 'Mamuro Marvelous',
      contact: 'mm@gmail.com',
      specialty: 'Gynaecologist',
      licenseNumber: '41913',
    },
    {
      id: 3,
      fullName: 'Ahmed Almadny',
      contact: 'aa@gmail.com',
      specialty: 'Dentist',
      licenseNumber: '41914',
    },
    {
      id: 4,
      fullName: 'Abdulsamad Raji',
      contact: 'almuhandith1497@gmail.com',
      specialty: 'Dermatologist',
      licenseNumber: '41915',
    },
  ]);
  return (
    <div>
      <div className='flex justify-center p-8 font-bold text-3xl'>
        <h1>Doctors List</h1>
      </div>
      <table className="w-full max-w-6xl mx-auto border-collapse border border-slate-400">
      <thead>
        <tr>
          <th className="border border-slate-300 p-4">Full Name</th>
          <th className="border border-slate-300 p-4">Contact</th>
          <th className="border border-slate-300 p-4">Specialty</th>
          <th className="border border-slate-300 p-4">License Number</th>
          <th className="border border-slate-300 p-4">Actions</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item.id}>
            <td className="border border-slate-300 p-4">
              {editData && editData.id === item.id ? (
                <input
                  type="text"
                  value={editData.fullName}
                  onChange={(e) =>
                    setEditData({ ...editData, fullName: e.target.value })
                  }
                />
              ) : (
                item.fullName
              )}
            </td>
            <td className="border border-slate-300 p-4">
              {editData && editData.id === item.id ? (
                <input
                  type="text"
                  value={editData.contact}
                  onChange={(e) =>
                    setEditData({ ...editData, contact: e.target.value })
                  }
                />
              ) : (
                item.contact
              )}
            </td>
            <td className="border border-slate-300 p-4">
              {editData && editData.id === item.id ? (
                <input
                  type="text"
                  value={editData.specialty}
                  onChange={(e) =>
                    setEditData({ ...editData, specialty: e.target.value })
                  }
                />
              ) : (
                item.specialty
              )}
            </td>
            <td className="border border-slate-300 p-4">
              {editData && editData.id === item.id ? (
                <input
                  type="text"
                  value={editData.licenseNumber}
                  onChange={(e) =>
                    setEditData({
                      ...editData,
                      licenseNumber: e.target.value,
                    })
                  }
                />
              ) : (
                item.licenseNumber
              )}
            </td>
            <td className="border border-slate-300 p-4">
              {editData && editData.id === item.id ? (
                <>
                  <button className='px-4' onClick={handleSaveEdit}><CiSaveDown2/></button>
                  <button onClick={() => setEditData(null)}><FcCancel/></button>
                </>
              ) : (
                <>
                  <button className='px-4' onClick={() => handleEdit(item.id)}><CiEdit/></button>
                  <button onClick={() => handleDelete(item.id)}><MdDelete/></button>
                </>
              )}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
    </div>
  )
}

export default ViewDoctor
