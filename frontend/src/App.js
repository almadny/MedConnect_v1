import { Route, Routes } from 'react-router-dom';
import Blog from './pages/Blog/Blog';
import FindHospital from './pages/FindHospital/FindHospital';
import Home from "./pages/Homepage/Home";
import Login from './pages/Login/Login';
import HospitalSignUp from './pages/SignUp/HospitalSignUp';
import PatientSignUp from './pages/SignUp/PatientSignUp';
import FindADoctor from './pages/Dashboard/FindADoctor';
import DashboardLayout from './layout/DashboardLayout';
import Appointment from './pages/Dashboard/Appointment';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/'>
          <Route index element={<Home />} />
          <Route path='PSignUp' element={<PatientSignUp/>} />
          <Route path='HSignUp' element={<HospitalSignUp/>} />
          <Route path='Login' element={<Login/>} />
          <Route path='Blog' element={<Blog/>} />
          <Route path='FindHospital' element={<FindHospital/>} />
          <Route path='patient_dashboard' element={<DashboardLayout />}>
            <Route path='find_a_doctor' element={<FindADoctor />} />
            <Route path='appointment' element={<Appointment />} />
          </Route>
        </Route>
      </Routes>
    </div>
  );
}

export default App;
