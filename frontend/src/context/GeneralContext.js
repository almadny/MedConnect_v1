import { createContext, useState } from "react";
import userPic from "../assets/dashboard-user.svg"
const GeneralContext = createContext({});

export const GeneralProvider = ({ children }) => {
    const links = "https://www.linkedin.com/in/emekarichmond\nemekarichmond@gmail.com\nhttps://www.behance.net/emekarichmond";
    const about = "I provide relatable solutions to everyday user problems by designing visually appealing and easy to use interfaces. I provide relatable solutions to everyday user problems by designing visually appealing and easy to use interfaces.";

    const initialValues = {
        fullName: "Isreal Emeka",
        email: "emekarichmomd@gmail.com",
        country: "Nigeria",
        city: "Ibadan",
        phoneNumber: "+23480123456789",
        resume: { fileName: "Resume.pdf", fileSize: 0, src: "" },
        role: "UI/UX Designer",
        majorSkill: "Figma",
        yoeMajor: 2,
        yoeTotal: 3,
        otherSkills: ["Interactive Design", "Photoshop", "Invision", "Figma", "UX Design", "UI Design", "Research"],
        about,
        contactLinks: links,
        userPic
    };

    const [user, setUser] = useState({ ...initialValues });
    const [isLogin, setIsLogin] = useState(false);
    const [account, setAccount] = useState("talent");

    const contextData = { user, setUser, isLogin, setIsLogin, account, setAccount };

    // const contextData = useMemo(
    //     () => ({
    //         user,
    //         isLogin,
    //         setUser,
    //         setLogin
    //     }),
    //     [user, isLogin]
    // );

    return (
        <GeneralContext.Provider value={contextData}>
            {children}
        </GeneralContext.Provider>
    );
};

// const useGeneralStore = () => {
//     return useContext(GeneralContext);
// }

export default GeneralContext;
