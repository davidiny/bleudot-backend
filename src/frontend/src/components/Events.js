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
            <div className="event-container">
            {(category.category === this.props.topic) ?(
            <div className="card">
              <div className="image">
                  <div className="img-container">
                    <img src={Stock}></img>
                    <button className="export">Export Event</button>
                  </div>
           
              </div>
              <div className="card-body">
                <div className="day">
                  <a className="curr-date">{category.date[0]} <br></br> {category.date[1]}</a>  
                </div>
               
                <img src={Line} className="img"></img>
                
                <div className="content">
                  <a className="event-title">
                    {category.name} <br></br>
                  </a>
                  <a className="event-details">
                    Hosted By {category.organization} <br></br>
                  </a>
                  <a className="event-time">
                    {category.start_time + " - " + category.end_time} <br></br>
                  </a>
                </div>
              </div>
            </div>):(<div></div>)}
            </div>
          )
        }))}

      </div>
    );
  }
}

export default Events;