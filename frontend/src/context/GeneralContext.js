import { createContext, useState } from "react";

const GeneralContext = createContext({});

export const AuthProvider = ({ children }) => {
    const [isLoggedin, setIsLoggedIn] = useState(false);
    const [account, setAccount] = useState("");

    const login = async (data) => {
      
      const account = data.user_type

      localStorage.setItem("jwt-token", data.access_token);
      localStorage.setItem("account-type", account);
      localStorage.setItem("user_id", data.id);
    
      setIsLoggedIn(true);
      setAccount(account);
    };
    
    const logout = () => {
      localStorage.removeItem('jwt-token');
      localStorage.removeItem('account-type');
      localStorage.removeItem("user_id");

      setIsLoggedIn(false);
      setAccount('');
    };
    
    const contextData = { login, logout, isLoggedin, setIsLoggedIn, account };

    return (
        <GeneralContext.Provider value={contextData}>
            {children}
        </GeneralContext.Provider>
    );
};

export default GeneralContext;
