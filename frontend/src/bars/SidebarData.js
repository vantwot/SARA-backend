import { BiBarChartAlt2, BiUserCircle, BiHive } from "react-icons/bi";
export const SidebarData = [
    {
        title: 'Profile',
        path: '/profile',
        icon: <BiUserCircle/>,
        cName: 'nav-text'
    },
    {
        title: 'Home',
        path: '/home',
        icon: <BiHive />,
        cName: 'nav-text'
    },
    {
        title: 'Stadistics',
        path: '/statistics',
        icon: <BiBarChartAlt2 />,
        cName: 'nav-text'
    }
]