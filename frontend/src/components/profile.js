import React, { useEffect } from "react";
import { Link } from "react-router-dom";
import { Button, Segment } from "semantic-ui-react";

import Cookies from 'js-cookie';

import logo from "../img/blank-profile-picture-973460_1280.png";

import { authUrl } from "./spotifyAuth";

export function Profile(props) {

    const profileData = props.profile;
    
    const profilePicture = () => {
        
        if (props.profile.spotify_image) {
            if (props.profile.spotify_image.length > 0) {
                return props.profile.spotify_image[0].url;
            }
            else {
                return logo;
            }
        } else {
            return logo;
        }
    }

    if(props.isLoggedIn) {
        return (
            <div className="profile-layout">
                <img className="profile-pic" src={profilePicture()} alt="Profile picture" />
                <br />
                <div className="profile-info">
                    <p>USERNAME</p>
                        <input type="text" value={profileData.username} className="input-field"
                        style={{ fontSize: '1em'}} readOnly />
                    <br />
                    <p>E-MAIL </p>
                        <input type="text" value={profileData.email} className="input-field"
                        style={{ fontSize: '1em'}} readOnly />
                    <br />
                    <p>FIRST NAME (optional)</p>
                        <input type="text" value={profileData.first_name} className="input-field"
                        style={{ fontSize: '1em'}} readOnly />
                    <br />
                    <p>LAST NAME (optional)</p>
                        <input type="text" value={profileData.last_name} className="input-field"
                        style={{ fontSize: '1em'}} readOnly />
                    <br />
                    <br />
                </div>

                <Segment inverted>
                    <Link to="/users/data/change">
                        <Button inverted color="green">
                            CHANGE DATA
                        </Button>
                    </Link>

                    <Link to="/users/data/change/password">
                        <Button inverted color="green">
                            CHANGE PASSWORD
                        </Button>
                    </Link>

                    <a href={authUrl}>
                        <Button inverted color="green">
                            SIGN IN WITH SPOTIFY
                        </Button>
                    </a>
                </Segment>

                
            </div>
        );
    } else {
        return (
            <div className="profile-layout">
                <p style={{color: 'white', fontSize: '4vh'}}>Seems you don't have a profile yet. Do you want to <Link to="/register" className="text-link">create one?</Link></p>
            </div>
            
        );
    }

}
