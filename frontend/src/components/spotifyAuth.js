export const authEndpoint = "https://accounts.spotify.com/authorize";

const redirectUri = "http://127.0.0.1:3000/main";

const clientID = '7c8a05fef0d349cc9e60cde70c426248';

const scopes = [
    'playlist-modify-private',
    'playlist-read-private',
    'playlist-modify-public',
    'playlist-read-collaborative'
]

export const authUrl = `${authEndpoint}
?client_id=${clientID}
&redirect_uri=${redirectUri}
&scope=${scopes.join("%20")}
&response_type=token
&show_dialog=true`;

export const getTokenFromUrl = () => {
    return window.location.hash
        .substring(1)
        .split('&')
        .reduce((initial, item) => {
            let parts = item.split("=");
            initial[parts[0]] = decodeURIComponent(parts[1]);

            return initial;
        }, {});
};