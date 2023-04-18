import React from 'react';
import styled from 'styled-components'
import Image from './img/fotoprofile.png'
import './pages.css'

const Container = styled.div`
    background-color: ${({ theme }) => theme.secondary};
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 2rem 0;
    flex-direction: column;

`

const ProfileImg = styled.img`
    height: 10rem;
`
const ProfileName = styled.h1`
    font-size: 2rem;
    font-weight: 300;
    color: ${({ theme }) => theme.textColor};
`

function Profile() {
    return (
        <div className='profile-container'>
            <Container>
                <ProfileImg src={Image} />
                <ProfileName className='text-name'>Edinson</ProfileName>
                <div className='div-info'>
                    <div className='div-interior-info'>
                        <div className='text-attribute'>
                            Nombre
                        </div>

                        <div className='text-value'>
                            Edinson
                        </div>
                    </div>
                    <div className='div-interior-info'>
                        <div className='text-attribute'>
                            Correo
                        </div>

                        <div className='text-value'>
                            email@email.com
                        </div>
                    </div>
                    <div className='div-interior-info'>
                        <div className='text-attribute'>
                            Telefono
                        </div>

                        <div className='text-value'>
                            3101234567
                        </div>
                    </div>
                    <div className='div-interior-info'>
                        <div className='text-attribute'>
                            Programa
                        </div>
                   
                        <div className='text-value'>
                            IngSistemas
                        </div>
                    </div>
                </div>
            </Container>
        </div>

    )
}

export default Profile;