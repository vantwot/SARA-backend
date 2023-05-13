import React from "react";
import { Link } from "react-router-dom";

import "styles/header.css";

// const categories = [{ name: "Matricular", slug: "matricula" }, { name: "Tabulados", slug: "tabulados" }, { name: "Perfil", slug: "profile" }]

const Header = ({ categories }) => {
    return (
        <div className="header-container">
            {/* <div className="top"> */}
                <div className="left">
                    <Link to="/home" className="link">
                        <span className="header-title">
                            SARA
                        </span>
                    </Link>
                </div>

                <div className="right">
                    {categories.map((category) => (
                        <Link key={category.slug} href={`/category/${category.slug}`} className="link">
                            <span className="header-category">
                                {category.name}
                            </span>
                        </Link>
                    ))}
                </div>
            {/* </div> */}
        </div>
    )
}

export default Header;