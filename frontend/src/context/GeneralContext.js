import { createContext, useState } from "react";

const GeneralContext = createContext({});

export const AuthProvider = ({ children }) => {
    const [isLoggedin, setIsLoggedIn] = useState(false);
    const [account, setAccount] = useState("");

    const login = async (data) => {
      const account = data.accountType

      localStorage.setItem("jwt-token", data.token);
      localStorage.setItem("account-type", data.accountType);
    
      setIsLoggedIn(true);
      setAccount(account);
    };
    
    const logout = () => {
      localStorage.removeItem('jwt-token');
      localStorage.removeItem('account-type');

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
