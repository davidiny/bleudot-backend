
import React, { Component } from 'react';
import PropTypes from "prop-types";
import Events from './Events';
import Logo from './Logo';

class Discover extends Component {
  static propTypes = {
    data: PropTypes.array.isRequired,
  };

  constructor(props) {
    super(props);
    this.state = {
      /*
      upcoming: ["SWE", "ECE", "IEEE", "Build", "5", "6"],
      trending: ["1", "2", "3", "4", "5", "6"],
      near: ["1", "2", "3", "4"],
      event_upcoming: {
        title: ["Korean Food Sale", "ASA Boba Sale", "3 Sale", "4 Sale", "5 Sale", "6 Sale"],
        org: ["Korean Student Association", "Asian Student Organization", "3 Org", "4 Org", "5 Org", "6 Org"],
        day: ["28th", "29th", "30th", "31th", "32th", "33th"],
        month: ["OCT", "OCT", "OCT", "OCT", "OCT", "OCT"],
        time: ["10 AM - 2 PM", "1PM - 3PM", "3PM - 5PM", "6PM- 8PM", "8PM - 10PM", "11PM - 1AM"],
      },
      event_trending: {
        title: ["Korean Food Sale", "ASA Boba Sale", "3 Sale", "4 Sale", "5 Sale", "6 Sale"],
        org: ["Korean Student Association", "Asian Student Organization", "3 Org", "4 Org", "5 Org", "6 Org"],
        day: ["28th", "29th", "30th", "31th", "32th", "33th"],
        month: ["OCT", "OCT", "OCT", "OCT", "OCT", "OCT"],
        time: ["10 AM - 2 PM", "1PM - 3PM", "3PM - 5PM", "6PM- 8PM", "8PM - 10PM", "11PM - 1AM"],
      },
      event_: {
        title: ["Korean Food Sale", "ASA Boba Sale", "3 Sale", "4 Sale", "5 Sale", "6 Sale"],
        org: ["Korean Student Association", "Asian Student Organization", "3 Org", "4 Org", "5 Org", "6 Org"],
        day: ["28th", "29th", "30th", "31th", "32th", "33th"],
        month: ["OCT", "OCT", "OCT", "OCT", "OCT", "OCT"],
        time: ["10 AM - 2 PM", "1PM - 3PM", "3PM - 5PM", "6PM- 8PM", "8PM - 10PM", "11PM - 1AM"],
      },
      */
    };
    //this.parse_data(this.props.data)
  }
 
  render() {
    let categories = ["Upcoming Events", "Trending", "Happening Near You"]
    return (        
      <div className="container">
        <Logo />
        
{/*     <div>
          {this.props.data.toString()}
        </div> */}

        <div className="filter-btns">
          <button className="filter-btn">Organizations</button>
          <button className="filter-btn">Events</button>
        </div>
        {categories.map(((category, id) => {
          return (
            <div className="category">
              <div className="title">{category}</div>
              {(id === 0) ?
                (
                  <Events type="upcoming" categoryName={this.props.data} topic="upcoming"></Events>
                ) :
                (<div></div>)
              }             
              {(id === 1) ?
                (
                  <Events categoryName={this.props.data} topic="trending"></Events>
                ) :
                (<div></div>)
              }
              {(id === 2) ?
                (
                  <Events categoryName={this.props.data} topic="near"></Events>
                ) :
                (<div></div>)
              } 
            </div>
          )
        }))}

      </div>
    );
  }
}

export default Discover;