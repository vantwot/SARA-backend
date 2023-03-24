import React, { useState } from "react";
import { Link } from 'react-router-dom';
import * as FaIcons from 'react-icons/fa';
import * as AiCons from 'react-icons/ai';
import { SidebarData } from "./SidebarData";
import './Navbar.css';
import styled from 'styled-components'
import { IconContext } from "react-icons";
import Image from '../pages/img/fotoprofile.png'

const Container = styled.div`
    margin-top: 2rem;
    align-items: center;
    display: flex;
    margin-left: 0rem;
    flex-direction: column;
    padding-bottom: 1em;
`

const ProfileImg = styled.img`
    height: 11rem;
`
const ProfileName = styled.h1`
text-decoration: none;
  color: #f5f5f5;
  font-size: 18px;

  display: flex;
  align-items: center;

`


export function Navbar() {
    const [sidebar, setSidebar] = useState(false);
    const showSidebar = () => setSidebar(!sidebar);

    return (
        <>
            <IconContext.Provider value={{ color: 'white' }}>
                <div className="navbar">
                    <Link to="#" className='menu-bars'>
                        <FaIcons.FaBars onClick={showSidebar} />
                    </Link>
                </div>
                <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}>
                    <ul className='nav-menu-items' onClick={showSidebar}>
                        <div className="navbar">
                            <Link to="#" className='menu-bars'>
                                <FaIcons.FaBars onClick={showSidebar} />
                            </Link>
                        </div>
                        <Container>
                <ProfileImg src={Image} />
                <ProfileName>Edinson</ProfileName>
                </Container>
                        {SidebarData.map((item, index) => {
                            return (
                                <li key={index} className={item.cName}>
                                    <Link to={item.path}>
                                        {item.icon}
                                        <span>{item.title}</span>
                                    </Link>
                                </li>
                            )
                        })}
                    </ul>
                </nav>
            </IconContext.Provider>
        </>
    )
}

