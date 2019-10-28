import React, { Component } from 'react';
import Stock from "../images/stock.png";
import Line from "../images/line.png"

class Events extends Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }

  render() {
    return (
      <div>
        {this.props.categoryName.map(((category, id) => {
          return (
            <div className="card">
              <div className="image">
                  <div className="img-container">
                    <img src={Stock}></img>
                    <button className="export">Export Event</button>
                  </div>
           
              </div>
              <div className="card-body">
                <div className="day">
                  <a className="curr-date">{this.props.event.day[id]} <br></br> {this.props.event.month[id]}</a>  
                </div>
               
                <img src={Line} className="img"></img>
                
                <div className="content">
                  <a className="event-title">
                    {this.props.event.title[id]} <br></br>
                  </a>
                  <a className="event-details">
                    Hosted By {this.props.event.org[id]} <br></br>
                  </a>
                  <a className="event-time">
                    {this.props.event.time[id]} <br></br>
                  </a>
                </div>
              </div>
            </div>
          )
        }))}

      </div>
    );
  }
}

export default Events;