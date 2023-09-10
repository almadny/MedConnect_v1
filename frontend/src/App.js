import { Route, Routes } from 'react-router-dom';
import Home from "./pages/Homepage/Home";
import Login from './pages/Login/Login';
import HospitalSignUp from './pages/SignUp/HospitalSignUp';
import PatientSignUp from './pages/SignUp/PatientSignUp';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/'>
          <Route index element={<Home />} />
          <Route path='PSignUp' element={<PatientSignUp/>} />
          <Route path='HSignUp' element={<HospitalSignUp/>} />
          <Route path='Login' element={<Login/>} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;
