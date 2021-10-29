import React from "react";
import playlistImage from "../img/playlist-template.png";
import { Button, Segment } from "semantic-ui-react";
import { Link } from "react-router-dom";

{/* structure of search result item
<div className="search-item">
    <div className="album-cover"></div>
    <div className="search-item-info">asdasdasd</div>
</div> */}
export function Playlists(props) {
    const userPK = props.pk;

    const playlists = props.playlists;

    console.log(playlists);
    const renderPlaylists = playlists.items.map((items) => {
        return (
            <div className="playlist-item">
                <img src={items.images.length === 0 ? playlistImage : items.images[0].url}></img>
                <span>{items.name}</span>
                <br />
                <Link to={`/playlist/${items.id}`}>
                    <Button className="btn" inverted color="green">
                        DETAILS
                    </Button>
                </Link>
            </div>
        )
    });

    return (
        <div>
            <div className="playlist-options">
                <div class="ui buttons">
                    <button class="ui green button">My playlists</button>
                    <div class="or"></div>
                    <button class="ui green button">All playlists</button>
                </div>
            </div>
            <div className="playlist-grid">
                {renderPlaylists}
            </div>
        </div>
    );
}