import React from "react";
import { Header } from "./";

const Layout = ({ children, categories }) => {

    return (
        <>
            <Header
                categories={categories}
             />
            {children}
        </>
    )
}

export default Layout;