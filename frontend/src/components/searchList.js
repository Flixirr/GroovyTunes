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
                    <div >
                        <img className="album-cover" src={item[1]['photo_song']} />
                    </div>
                    <div className="search-item-info">
                        <p>Title: {item[1]['title']}</p>
                        <p>Artist: {item[0]['name']}</p> 
                        {item[1].album && <p>Album: {item[1].album.name}</p>} 
                        {item[1].featured_artists.length != 0 && <p>Featured: {item[1].featured_artists.map(e => e.name).join(' ')}</p>} 
                        {item[1].producer_artists && <p>Producers: {item[1].producer_artists.join(' ')}</p>}
                        <p>Released: {item[1]['release_date']}</p> 
                    </div>
            </div>
        )
    });

    return (
        <div>{renderList}</div>
    );
}