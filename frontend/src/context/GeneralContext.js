import { createContext, useState } from "react";

const GeneralContext = createContext({});

export const AuthProvider = ({ children }) => {
    const [isLoggedin, setIsLoggedIn] = useState(false);
    const [account, setAccount] = useState("");
    const [JWT, setJWT] = useState("")

    const login = async (data) => {
      
      const account = data.user_type

      setJWT(data.access_token)
      console.log(JWT)

      localStorage.setItem("jwt-token", data.access_token);
      localStorage.setItem("account-type", account);
      localStorage.setItem("user_id", data.id);
    
      setIsLoggedIn(true);
      setAccount(account);
    };
    
    const logout = () => {
      localStorage.clear()

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
