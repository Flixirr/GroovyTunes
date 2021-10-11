import React from "react";


{/* structure of search result item
<div className="search-item">
    <div className="album-cover"></div>
    <div className="search-item-info">asdasdasd</div>
</div> */}
export function SearchList(props) {
    const items = props.items;

    const renderList = items.map((item) => {
        return (
            <div className="search-item">
                <div className="album-cover"></div>
                <div className="search-item-info">
                    Artist: {item[0][0]} <br />
                    Song: {item[1][0]} <br />
                    Released: {item[1][2]} <br />
                    Featured artists: { [].concat.apply([], item[1][3]).filter((link, index) => {return index%2 === 0}).join(', ') } <br />
                    Producers: { [].concat.apply([], item[1][4]).filter((link, index) => {return index%2 === 0}).join(', ')} 
                    <br /><br />
                </div>
            </div>
        )
    });

    return (
        <div>{renderList}</div>
    );
}