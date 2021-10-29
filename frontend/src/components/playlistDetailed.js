import React, { useEffect, useState } from "react";
import { Button, Segment } from "semantic-ui-react";
import { Link } from "react-router-dom";
import { useParams } from 'react-router-dom';

import playlistImage from "../img/playlist-template.png";

import SpotifyWebApi from 'spotify-web-api-js';
{/* structure of search result item
<div className="search-item">
    <div className="album-cover"></div>
    <div className="search-item-info">asdasdasd</div>
</div> */}
export function PlaylistDetails(props) {
    let { id } = useParams();

    const [playlistData, setPlaylist] = useState([]);

    const [playlistTitle, setTitle] = useState("No name");
    const [playlistDesc, setDesc] = useState("No description");
    const [playlistImg, setImg] = useState(playlistImage);

    const spotifyApi = new SpotifyWebApi();

    const millisToMinutesAndSeconds = (millis) => {
        var minutes = Math.floor(millis / 60000);
        var seconds = ((millis % 60000) / 1000).toFixed(0);
        return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
    }

    useEffect(() => {
        spotifyApi.getPlaylist(id).then((data) => {
            setPlaylist(data.tracks.items);
            if(data.images.length > 0)
                setImg(data.images[0].url);
            setDesc(data.description);
            setTitle(data.name)
        }, (err) => {
            console.error(err);
        });
    })
    

    

    const generateTable = playlistData.map((item) => {
        return (
            <tr>
                <td>{item.track.name}</td>
                <td>{millisToMinutesAndSeconds(item.track.duration_ms)}</td>
                //{item.track.artists.length != 0 && <td>{item.track.artists.map(e => e.name).join(' ')}</td>}
            </tr>
        )
    });

    return (
        <div className="playlist-details">
            <img src={playlistImg}></img>
            <div className="details">
                <span className="title">{playlistTitle}</span>
                <p>{playlistDesc}</p>
                <Button className="btn" inverted color="green">
                    MAKE PUBLIC
                </Button>
            </div>
            <div className="content-table">
                <table className="table">
                    <tr>
                        <td>Song</td>
                        <td>Duration</td>
                        <td>Artist</td>
                    </tr>
                    {generateTable}
                </table>
            </div>
        </div>
    );
}