import React from 'react';
import PropTypes from 'prop-types';
import Navbar from './Nav';

function Home(props) {
  return (
  <Navbar/>

  );
}

Home.propTypes = {
  window: PropTypes.func,
};

export default Home;