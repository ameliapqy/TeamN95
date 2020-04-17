import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';

const AnyReactComponent = ({ text }) => <div>{text}</div>;


const defaultProps = {
    center: {
      lat: 59.95,
      lng: 30.33
    },
    zoom: 11
};

export default function Map() {
  
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '80vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: "AIzaSyAzUo90Rd0epMZOcEV89O9d7NfdxF7-Y4I" }}
          defaultCenter={defaultProps.center}
          defaultZoom={defaultProps.zoom}
        >
          <AnyReactComponent
            lat={59.955413}
            lng={30.337844}
            text="Test Marker"
          />
        </GoogleMapReact>
      </div>
    );
};
