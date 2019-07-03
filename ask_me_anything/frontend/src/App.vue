<template>
  <div id="app">
    <navbar-component></navbar-component>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view />
  </div>
</template>


<script>
import NavbarComponent from "./components/NavBar";
export default {
  
  name:"App",
  components:{
      NavbarComponent
  }
  
}
</script>

<style>



</style>
