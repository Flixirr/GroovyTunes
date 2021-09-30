import React from "react";

export function SearchList(props) {
    const items = props.items;

    const renderList = items.map((item) => {
        return <li>
            Artist: {item[0][0]} <br />
            Song: {item[1][0]} <br />
            Released: {item[1][2]} <br />
            Featured artists: { [].concat.apply([], item[1][3]).filter((link, index) => {return index%2 === 0}).join(', ') } <br />
            Producers: { [].concat.apply([], item[1][4]).filter((link, index) => {return index%2 === 0}).join(', ')} 
            <br /><br />
        </li>
        
    });

    return (
        <ul>{renderList}</ul>
    );
}