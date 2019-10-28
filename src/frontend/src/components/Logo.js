import React from 'react';

const Logo = () => {
  return (
  <div class="search-box">
    <form method="POST">
      Show me <input type="text" placeholder="multicultural, music, cooking..." name="search" />
      In <input type="text" placeholder="Community" name="search" /> <button type="submit" className="search-btn">Search</button>
    </form>
      
  </div>

  );
}

export default Logo;