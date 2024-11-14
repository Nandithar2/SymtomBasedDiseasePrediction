<template>
    <nav class="navbar">
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/history">History</router-link></li>
        <li><router-link to="/settings">Settings</router-link></li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'Navbar'
  };
  </script>
  
  <!-- <style scoped>
  .navbar {
    background-color: #0172AD;
    text-decoration-color: #FFFFFF;
    
  }

  ul {
    list-style: none;
    display: flex;
    gap: 0.5rem;
    text-decoration-color: #FFFFFF;
  }
  </style>
   -->
   <style scoped>
   .navbar {
     background-color: #0172AD; /* Blue background */
     color: #FFFFFF; /* White text color */
   }
 
   .navbar ul {
     list-style: none;
     display: flex;
     gap: 0.5rem;
     margin: 0; /* Remove default margin */
     padding: 0; /* Remove default padding */
   }
 
   .navbar li {
     color: #FFFFFF; /* Ensure list items have white text */
   }
 
   .navbar a {
     color: #FFFFFF; /* Ensure links have white text */
     text-decoration: none; /* Remove underline from links */
   }
 
   .navbar a:hover {
     text-decoration: underline; /* Optional: Add underline on hover */
   }
 </style>