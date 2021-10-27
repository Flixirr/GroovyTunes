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
                        <img className="album-cover" src={item['photo_song']} />
                    </div>
                    <div className="search-item-info">
                        <p>Title: {item['title']}</p>
                        <p>Artist: {item['name']}</p> 
                        {item.album && <p>Album: {item.album.name}</p>} 
                        {item.featured_artists.length != 0 && <p>Featured: {item.featured_artists.map(e => e.name).join(' ')}</p>} 
                        {item.producer_artists && <p>Producers: {item.producer_artists.join(' ')}</p>}
                        <p>Released: {item['release_date']}</p> 
                    </div>
            </div>
        )
    });

    return (
        <div>{renderList}</div>
    );
}