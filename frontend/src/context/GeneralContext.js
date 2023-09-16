import { createContext, useState } from "react";

const GeneralContext = createContext({});

export const AuthProvider = ({ children }) => {
    const [isLoggedin, setIsLoggedIn] = useState(false);
    const [account, setAccount] = useState("");

    const login = (token, account) => {
        localStorage.setItem('token', token);
        localStorage.setItem('account', account);
    
        setIsLoggedIn(true);
        setAccount(account);
    };
    
    const logout = () => {
      localStorage.removeItem('token');
      localStorage.removeItem('account');

      setIsLoggedIn(false);
      setAccount('');
    };
    
    const contextData = { login, logout, isLoggedin, account };

    return (
        <GeneralContext.Provider value={contextData}>
            {children}
        </GeneralContext.Provider>
    );
};

export default GeneralContext;
